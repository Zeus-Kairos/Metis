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

export default function App() {
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

  async function runOfflineEvaluation() {
    if (!traceFilePath.trim()) {
      setRunEvalMessage("Please provide a trace JSONL file path.");
      return;
    }
    setRunningEval(true);
    setError("");
    setRunEvalMessage("");
    try {
      const payload = await apiPost("/api/eval/run-offline", {
        trace_file: traceFilePath.trim(),
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

  return (
    <div className="app">
      <header className="topbar">
        <h1>Metis Trace & RAGAS Dashboard</h1>
        <div className="api-base">API: {API_BASE}</div>
      </header>
      {error ? <div className="error">{error}</div> : null}

      <section className="panel">
        <h2>Runs</h2>
        <div className="filters">
          <input
            placeholder="thread_id"
            value={filters.thread_id}
            onChange={(e) => setFilters((prev) => ({ ...prev, thread_id: e.target.value }))}
          />
          <input
            placeholder="knowledgebase_id"
            value={filters.knowledgebase_id}
            onChange={(e) => setFilters((prev) => ({ ...prev, knowledgebase_id: e.target.value }))}
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
        <div className="content-grid">
          <div className="list">
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
            {runsLoading ? <div className="loading">Loading runs...</div> : null}
            {runs.map((item) => (
              <div key={item.run_id} className="list-row">
                <button
                  className={`list-item ${selectedRunId === item.run_id ? "active" : ""}`}
                  onClick={() => setSelectedRunId(item.run_id)}
                >
                  <div className="run-head">
                    <strong>{item.run_id}</strong>
                    <span>{item.rag_type}</span>
                  </div>
                  <div className="run-sub">{item.timestamp}</div>
                  <div className="run-sub">{item.query}</div>
                </button>
                <button className="delete-btn" onClick={() => deleteRun(item.run_id)}>
                  Delete
                </button>
              </div>
            ))}
          </div>
          <div className="detail">
            {runLoading ? <div className="loading">Loading run details...</div> : null}
            {!runLoading && runDetail ? (
              <>
                <h3>Run Details</h3>
                <pre>{pretty(runDetail)}</pre>
              </>
            ) : (
              <div className="empty">Select a run to view details.</div>
            )}
          </div>
        </div>
      </section>

      <section className="panel">
        <h2>Evaluation Results</h2>
        <div className="filters">
          <select
            value={traceFilePath}
            onChange={(e) => setTraceFilePath(e.target.value)}
          >
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
        {runEvalMessage ? <div className="info">{runEvalMessage}</div> : null}
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
                <h3>Evaluation Details</h3>
                <pre>{pretty(evalDetail)}</pre>
              </>
            ) : (
              <div className="empty">Select an evaluation to view details.</div>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}

