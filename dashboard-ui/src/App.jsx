import { useEffect, useMemo, useState } from "react";

const DEFAULT_API_BASE =
  typeof window !== "undefined"
    ? `${window.location.protocol}//${window.location.hostname}:8000`
    : "http://127.0.0.1:8000";
const API_BASE = import.meta.env.VITE_API_BASE || DEFAULT_API_BASE;

async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`, {
    credentials: "include",
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Request failed: ${res.status}`);
  }
  return res.json();
}

async function apiPost(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Request failed: ${res.status}`);
  }
  return res.json();
}

async function apiDelete(path) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "DELETE",
    credentials: "include",
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Request failed: ${res.status}`);
  }
  return res.json();
}

function toQuery(params) {
  const query = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (value !== null && value !== undefined && value !== "") {
      query.set(key, String(value));
    }
  });
  const payload = query.toString();
  return payload ? `?${payload}` : "";
}

function pretty(obj) {
  return JSON.stringify(obj, null, 2);
}

function formatMetric(value) {
  if (value === null || value === undefined || value === "") return "-";
  if (typeof value === "number") return value.toFixed(4);
  return String(value);
}

export default function App() {
  const [activeTab, setActiveTab] = useState("traces");
  const [evalSubTab, setEvalSubTab] = useState("run");
  const [runs, setRuns] = useState([]);
  const [runTotal, setRunTotal] = useState(0);
  const [runPage, setRunPage] = useState(1);
  const [selectedRunId, setSelectedRunId] = useState("");
  const [runDetail, setRunDetail] = useState(null);
  const [runLoading, setRunLoading] = useState(false);
  const [runsLoading, setRunsLoading] = useState(false);

  const [evals, setEvals] = useState([]);
  const [evalTotal, setEvalTotal] = useState(0);
  const [evalPage, setEvalPage] = useState(1);
  const [selectedEvalId, setSelectedEvalId] = useState("");
  const [evalDetail, setEvalDetail] = useState(null);
  const [evalLoading, setEvalLoading] = useState(false);
  const [evalsLoading, setEvalsLoading] = useState(false);

  const [filters, setFilters] = useState({
    thread_id: "",
    knowledgebase_id: "",
    rag_type: "",
  });
  const [error, setError] = useState("");
  const [traceFilePath, setTraceFilePath] = useState("");
  const [traceSamples, setTraceSamples] = useState([]);
  const [referenceAnswersByTraceIndex, setReferenceAnswersByTraceIndex] = useState({});
  const [traceFiles, setTraceFiles] = useState([]);
  const [runningEval, setRunningEval] = useState(false);
  const [runEvalMessage, setRunEvalMessage] = useState("");

  const runPageSize = 20;
  const evalPageSize = 20;

  const runQuery = useMemo(
    () =>
      toQuery({
        page: runPage,
        page_size: runPageSize,
        ...filters,
      }),
    [runPage, filters]
  );
  const evalQuery = useMemo(
    () =>
      toQuery({
        page: evalPage,
        page_size: evalPageSize,
      }),
    [evalPage]
  );

  useEffect(() => {
    async function loadRuns() {
      setRunsLoading(true);
      setError("");
      try {
        const data = await apiGet(`/api/eval/runs${runQuery}`);
        setRuns(data.items || []);
        setRunTotal(data.total || 0);
      } catch (err) {
        setError(err.message);
      } finally {
        setRunsLoading(false);
      }
    }
    loadRuns();
  }, [runQuery]);

  useEffect(() => {
    async function loadEvals() {
      setEvalsLoading(true);
      setError("");
      try {
        const data = await apiGet(`/api/eval/results${evalQuery}`);
        setEvals(data.items || []);
        setEvalTotal(data.total || 0);
      } catch (err) {
        setError(err.message);
      } finally {
        setEvalsLoading(false);
      }
    }
    loadEvals();
  }, [evalQuery]);

  useEffect(() => {
    async function loadTraceFiles() {
      try {
        const data = await apiGet("/api/eval/trace-files");
        const items = data.items || [];
        setTraceFiles(items);
        if (!traceFilePath && items.length > 0) {
          setTraceFilePath(items[0].path);
        }
      } catch (err) {
        setError(err.message);
      }
    }
    loadTraceFiles();
  }, []);

  useEffect(() => {
    async function loadTraceSamples() {
      if (!traceFilePath.trim()) {
        setTraceSamples([]);
        setReferenceAnswersByTraceIndex({});
        return;
      }
      try {
        const data = await apiGet(
          `/api/eval/trace-samples${toQuery({ trace_file: traceFilePath.trim() })}`
        );
        const samples = data.samples || [];
        setTraceSamples(samples);
        setReferenceAnswersByTraceIndex((prev) => {
          const next = {};
          samples.forEach((sample) => {
            const idx = sample.trace_index;
            const existing = prev[idx];
            next[idx] = existing ?? sample.ground_truth ?? "";
          });
          return next;
        });
      } catch (err) {
        setError(err.message);
      }
    }
    loadTraceSamples();
  }, [traceFilePath]);

  async function runOfflineEvaluation() {
    if (!traceFilePath.trim()) {
      setRunEvalMessage("Please provide a trace JSONL file path.");
      return;
    }
    if (traceSamples.length > 0) {
      const missingSamples = traceSamples.filter(
        (sample) => !(referenceAnswersByTraceIndex[sample.trace_index] || "").trim()
      );
      if (missingSamples.length > 0) {
        setRunEvalMessage(
          `Please provide a reference answer for each trace. Missing rows: ${missingSamples
            .slice(0, 10)
            .map((s) => s.trace_index + 1)
            .join(", ")}${missingSamples.length > 10 ? "..." : ""}`
        );
        return;
      }
    }
    const referenceAnswers = traceSamples.map(
      (sample) => (referenceAnswersByTraceIndex[sample.trace_index] || "").trim()
    );
    setRunningEval(true);
    setError("");
    setRunEvalMessage("");
    try {
      const payload = await apiPost("/api/eval/run-offline", {
        trace_file: traceFilePath.trim(),
        reference_answers: referenceAnswers,
      });
      setRunEvalMessage(
        `Evaluation created: ${payload?.result?.eval_id || "unknown eval id"}`
      );
      const list = await apiGet(`/api/eval/results${evalQuery}`);
      setEvals(list.items || []);
      setEvalTotal(list.total || 0);
      if (payload?.result?.eval_id) {
        setSelectedEvalId(payload.result.eval_id);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setRunningEval(false);
    }
  }

  useEffect(() => {
    async function loadRunDetail() {
      if (!selectedRunId) return;
      setRunLoading(true);
      setError("");
      try {
        const data = await apiGet(`/api/eval/runs/${selectedRunId}`);
        setRunDetail(data.run || null);
      } catch (err) {
        setError(err.message);
      } finally {
        setRunLoading(false);
      }
    }
    loadRunDetail();
  }, [selectedRunId]);

  useEffect(() => {
    async function loadEvalDetail() {
      if (!selectedEvalId) return;
      setEvalLoading(true);
      setError("");
      try {
        const data = await apiGet(`/api/eval/results/${selectedEvalId}`);
        setEvalDetail(data.result || null);
      } catch (err) {
        setError(err.message);
      } finally {
        setEvalLoading(false);
      }
    }
    loadEvalDetail();
  }, [selectedEvalId]);

  async function deleteRun(runId) {
    const confirmed = window.confirm(`Delete trace run ${runId}?`);
    if (!confirmed) return;
    setError("");
    try {
      await apiDelete(`/api/eval/runs/${runId}`);
      if (selectedRunId === runId) {
        setSelectedRunId("");
        setRunDetail(null);
      }
      const data = await apiGet(`/api/eval/runs${runQuery}`);
      setRuns(data.items || []);
      setRunTotal(data.total || 0);
    } catch (err) {
      setError(err.message);
    }
  }

  async function deleteEval(evalId) {
    const confirmed = window.confirm(`Delete evaluation ${evalId}?`);
    if (!confirmed) return;
    setError("");
    try {
      await apiDelete(`/api/eval/results/${evalId}`);
      if (selectedEvalId === evalId) {
        setSelectedEvalId("");
        setEvalDetail(null);
      }
      const data = await apiGet(`/api/eval/results${evalQuery}`);
      setEvals(data.items || []);
      setEvalTotal(data.total || 0);
    } catch (err) {
      setError(err.message);
    }
  }

  const metricRows = useMemo(() => {
    if (!evalDetail) return [];
    const rows = [];
    const metrics = evalDetail.metrics || {};
    Object.keys(metrics).forEach((key) => {
      rows.push({ name: key, value: metrics[key], group: "metrics" });
    });
    const diagnostics = evalDetail.diagnostics || {};
    Object.keys(diagnostics).forEach((key) => {
      rows.push({ name: key, value: diagnostics[key], group: "diagnostics" });
    });
    [
      "eval_id",
      "status",
      "created_at",
      "sample_count",
      "source_file",
      "reference_answer_provided",
      "reference_answers_count",
      "llm_model",
      "embedding_model",
    ].forEach((key) => {
      if (evalDetail[key] !== undefined) {
        rows.push({ name: key, value: evalDetail[key], group: "meta" });
      }
    });
    return rows;
  }, [evalDetail]);

  const sampleMetricKeys = useMemo(() => {
    const samples = evalDetail?.samples || [];
    const keys = new Set();
    samples.forEach((sample) => {
      Object.keys(sample || {}).forEach((key) => {
        if (!["run_id", "question", "user_input", "diagnostics"].includes(key)) {
          keys.add(key);
        }
      });
    });
    return Array.from(keys);
  }, [evalDetail]);

  useEffect(() => {
    if (activeTab === "evals" && evalSubTab === "results") {
      // Ensure results list is loaded when entering results tab
      // (eval list is also loaded by evalQuery effect, so this just keeps UX snappy)
      setEvalPage((p) => p || 1);
    }
  }, [activeTab, evalSubTab]);

  return (
    <div className="app">
      <header className="topbar">
        <h1>Metis Trace & RAGAS Dashboard</h1>
        <div className="api-base">API: {API_BASE}</div>
      </header>
      {error ? <div className="error">{error}</div> : null}

      <div className="main-layout">
        <aside className="tabs left-tabs">
          <button
            className={`tab-btn ${activeTab === "traces" ? "active" : ""}`}
            onClick={() => setActiveTab("traces")}
          >
            Traces
          </button>
          <button
            className={`tab-btn ${activeTab === "evals" ? "active" : ""}`}
            onClick={() => setActiveTab("evals")}
          >
            Evals
          </button>
        </aside>

        {activeTab === "traces" ? (
          <section className="panel">
          <div className="filters">
            <input
              placeholder="thread_id"
              value={filters.thread_id}
              onChange={(e) => setFilters((prev) => ({ ...prev, thread_id: e.target.value }))}
            />
            <input
              placeholder="knowledgebase_id"
              value={filters.knowledgebase_id}
              onChange={(e) =>
                setFilters((prev) => ({ ...prev, knowledgebase_id: e.target.value }))
              }
            />
            <select
              value={filters.rag_type}
              onChange={(e) => setFilters((prev) => ({ ...prev, rag_type: e.target.value }))}
            >
              <option value="">all rag types</option>
              <option value="simple">simple</option>
              <option value="query_refined">query_refined</option>
              <option value="fusion">fusion</option>
              <option value="rerank">rerank</option>
              <option value="agentic">agentic</option>
            </select>
            <button onClick={() => setRunPage(1)}>Apply</button>
          </div>
          <div className="meta-row">
            <span>Total: {runTotal}</span>
            <div>
              <button disabled={runPage <= 1} onClick={() => setRunPage((p) => p - 1)}>
                Prev
              </button>
              <span className="page-indicator">{runPage}</span>
              <button
                disabled={runPage * runPageSize >= runTotal}
                onClick={() => setRunPage((p) => p + 1)}
              >
                Next
              </button>
            </div>
          </div>
          {runsLoading ? <div className="loading">Loading traces...</div> : null}
          <div className="table-wrap">
            <table className="data-table traces-table">
              <thead>
                <tr>
                  <th>run_id</th>
                  <th>rag_type</th>
                  <th>timestamp</th>
                  <th>query</th>
                  <th>retrieval_count</th>
                  <th>actions</th>
                </tr>
              </thead>
              <tbody>
                {runs.map((item) => (
                  <tr
                    key={item.run_id}
                    className={selectedRunId === item.run_id ? "row-active" : ""}
                  >
                    <td>
                      <button
                        className="link-btn"
                        onClick={() => setSelectedRunId(item.run_id)}
                      >
                        {item.run_id}
                      </button>
                    </td>
                    <td>{item.rag_type || "-"}</td>
                    <td>{item.timestamp || "-"}</td>
                    <td className="wrap-cell">{item.query || "-"}</td>
                    <td>{formatMetric(item.retrieval_count)}</td>
                    <td>
                      <button className="small-btn" onClick={() => setSelectedRunId(item.run_id)}>
                        View
                      </button>
                      <button className="small-btn danger" onClick={() => deleteRun(item.run_id)}>
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
                {runs.length === 0 && !runsLoading ? (
                  <tr>
                    <td colSpan={6} className="empty">
                      No traces found.
                    </td>
                  </tr>
                ) : null}
              </tbody>
            </table>
          </div>
          <div className="detail detail-below">
            {runLoading ? <div className="loading">Loading trace details...</div> : null}
            {!runLoading && runDetail ? (
              <>
                <h3>Trace Details</h3>
                <pre>{pretty(runDetail)}</pre>
              </>
            ) : (
              <div className="empty">Select a trace to view details.</div>
            )}
          </div>
          </section>
        ) : (
          <section className="panel">
            <div className="subtabs">
              <button
                className={`subtab-btn ${evalSubTab === "run" ? "active" : ""}`}
                onClick={() => setEvalSubTab("run")}
              >
                Run
              </button>
              <button
                className={`subtab-btn ${evalSubTab === "results" ? "active" : ""}`}
                onClick={() => setEvalSubTab("results")}
              >
                Results
              </button>
            </div>

            {evalSubTab === "run" ? (
              <>
          <div className="filters">
            <select value={traceFilePath} onChange={(e) => setTraceFilePath(e.target.value)}>
              <option value="">select trace file</option>
              {traceFiles.map((file) => (
                <option key={file.path} value={file.path}>
                  {file.name}
                </option>
              ))}
            </select>
            <input
              placeholder="trace file path (JSONL)"
              value={traceFilePath}
              onChange={(e) => setTraceFilePath(e.target.value)}
            />
            <button onClick={runOfflineEvaluation} disabled={runningEval}>
              {runningEval ? "Running..." : "Run Offline Evaluation"}
            </button>
          </div>
          {traceSamples.length > 0 ? (
            <div className="table-wrap">
              <table className="data-table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>Run ID</th>
                    <th>Question</th>
                    <th>Reference Answer</th>
                  </tr>
                </thead>
                <tbody>
                  {traceSamples.map((sample) => (
                    <tr key={`trace-${sample.trace_index}`}>
                      <td>{sample.trace_index + 1}</td>
                      <td>{sample.run_id || "-"}</td>
                      <td className="wrap-cell">{sample.question || "-"}</td>
                      <td>
                        <textarea
                          className="table-textarea"
                          value={referenceAnswersByTraceIndex[sample.trace_index] || ""}
                          onChange={(e) =>
                            setReferenceAnswersByTraceIndex((prev) => ({
                              ...prev,
                              [sample.trace_index]: e.target.value,
                            }))
                          }
                          placeholder="Required for this trace"
                        />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : null}
          {runEvalMessage ? <div className="info">{runEvalMessage}</div> : null}
              </>
            ) : null}

            {evalSubTab === "results" ? (
              <div className="content-grid">
            <div className="list">
              <div className="meta-row">
                <span>Total: {evalTotal}</span>
                <div>
                  <button disabled={evalPage <= 1} onClick={() => setEvalPage((p) => p - 1)}>
                    Prev
                  </button>
                  <span className="page-indicator">{evalPage}</span>
                  <button
                    disabled={evalPage * evalPageSize >= evalTotal}
                    onClick={() => setEvalPage((p) => p + 1)}
                  >
                    Next
                  </button>
                </div>
              </div>
              {evalsLoading ? <div className="loading">Loading evals...</div> : null}
              {evals.map((item) => (
                <div key={item.eval_id} className="list-row">
                  <button
                    className={`list-item ${selectedEvalId === item.eval_id ? "active" : ""}`}
                    onClick={() => setSelectedEvalId(item.eval_id)}
                  >
                    <div className="run-head">
                      <strong>{item.eval_id}</strong>
                      <span>{item.sample_count} samples</span>
                    </div>
                    <div className="run-sub">{item.created_at}</div>
                  </button>
                  <button className="delete-btn" onClick={() => deleteEval(item.eval_id)}>
                    Delete
                  </button>
                </div>
              ))}
            </div>
            <div className="detail">
              {evalLoading ? <div className="loading">Loading eval details...</div> : null}
              {!evalLoading && evalDetail ? (
                <>
                  <h3>Statistics</h3>
                  <div className="table-wrap">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Group</th>
                          <th>Name</th>
                          <th>Value</th>
                        </tr>
                      </thead>
                      <tbody>
                        {metricRows.map((row) => (
                          <tr key={`${row.group}-${row.name}`}>
                            <td>{row.group}</td>
                            <td>{row.name}</td>
                            <td>{formatMetric(row.value)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  <h3>Record Details</h3>
                  <div className="table-wrap">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>run_id</th>
                          <th>question</th>
                          {sampleMetricKeys.map((key) => (
                            <th key={key}>{key}</th>
                          ))}
                          <th>context_count</th>
                          <th>context_total_chars</th>
                        </tr>
                      </thead>
                      <tbody>
                        {(evalDetail.samples || []).map((sample, idx) => (
                          <tr key={`${sample.run_id || "sample"}-${idx}`}>
                            <td>{sample.run_id || "-"}</td>
                            <td className="wrap-cell">
                              {sample.question || sample.user_input || "-"}
                            </td>
                            {sampleMetricKeys.map((key) => (
                              <td key={`${idx}-${key}`}>{formatMetric(sample[key])}</td>
                            ))}
                            <td>{formatMetric(sample?.diagnostics?.context_count)}</td>
                            <td>{formatMetric(sample?.diagnostics?.context_total_chars)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </>
              ) : (
                <div className="empty">Select an evaluation to view details.</div>
              )}
            </div>
          </div>
            ) : null}
          </section>
        )}
      </div>
    </div>
  );
}

