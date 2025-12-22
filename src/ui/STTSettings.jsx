import React, { useState, useEffect } from 'react';

/**
 * STT Settings Component
 * Provides UI for configuring Speech-to-Text settings including:
 * - Language selection
 * - Wake word configuration (enable/disable, selection with preview)
 * - Model selection
 * - VAD sensitivity
 */
const STTSettings = ({ onSettingsChange, initialSettings = {}, isVisible, onClose }) => {
  const [settings, setSettings] = useState({
    language: initialSettings.language || 'en',
    enable_wake_word: initialSettings.enable_wake_word || false,
    wake_words: initialSettings.wake_words || 'alexa',
    wakeword_backend: initialSettings.wakeword_backend || 'pvporcupine',
    model: initialSettings.model || 'base',
    silero_sensitivity: initialSettings.silero_sensitivity || 0.6,
    webrtc_sensitivity: initialSettings.webrtc_sensitivity || 3,
    post_speech_silence_duration: initialSettings.post_speech_silence_duration || 0.5,
    ...initialSettings
  });

  const [languages, setLanguages] = useState([]);
  const [wakeWords, setWakeWords] = useState([]);
  const [hoveredWakeWord, setHoveredWakeWord] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch languages and wake words from API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [langRes, wakeWordRes] = await Promise.all([
          fetch('/stt/languages'),
          fetch('/stt/wake-words')
        ]);

        if (langRes.ok) {
          const langData = await langRes.json();
          setLanguages(langData.languages || []);
        }

        if (wakeWordRes.ok) {
          const wakeWordData = await wakeWordRes.json();
          setWakeWords(wakeWordData.wake_words || []);
        }
      } catch (error) {
        console.error('Error fetching STT settings data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  // Fetch current settings from API
  useEffect(() => {
    const fetchSettings = async () => {
      try {
        const response = await fetch('/stt/settings');
        if (response.ok) {
          const data = await response.json();
          setSettings(prev => ({ ...prev, ...data }));
        }
      } catch (error) {
        console.error('Error fetching STT settings:', error);
      }
    };

    fetchSettings();
  }, []);

  // Conditionally render if not visible
  if (!isVisible) {
    return null;
  }

  const handleSettingChange = async (key, value) => {
    const newSettings = { ...settings, [key]: value };
    setSettings(newSettings);

    // Update backend
    try {
      const updatePayload = { [key]: value };
      const response = await fetch('/stt/settings', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatePayload),
      });

      if (response.ok) {
        // Notify parent component
        if (onSettingsChange) {
          onSettingsChange(newSettings);
        }
      } else {
        console.error('Failed to update STT settings');
        // Revert on error
        setSettings(settings);
      }
    } catch (error) {
      console.error('Error updating STT settings:', error);
      // Revert on error
      setSettings(settings);
    }
  };

  const handleLanguageChange = (e) => {
    const languageCode = e.target.value;
    handleSettingChange('language', languageCode);
  };

  const handleWakeWordToggle = (e) => {
    const enabled = e.target.checked;
    handleSettingChange('enable_wake_word', enabled);
  };

  const handleWakeWordChange = (e) => {
    const wakeWord = e.target.value;
    handleSettingChange('wake_words', wakeWord);
  };

  const handleModelChange = (e) => {
    const model = e.target.value;
    handleSettingChange('model', model);
  };

  const handleSileroSensitivityChange = (e) => {
    const sensitivity = parseFloat(e.target.value);
    handleSettingChange('silero_sensitivity', sensitivity);
  };

  const handleWebRTCSensitivityChange = (e) => {
    const sensitivity = parseInt(e.target.value);
    handleSettingChange('webrtc_sensitivity', sensitivity);
  };

  const handlePostSpeechSilenceChange = (e) => {
    const duration = parseFloat(e.target.value);
    handleSettingChange('post_speech_silence_duration', duration);
  };

  const selectedWakeWordPreview = wakeWords.find(ww => ww.value === settings.wake_words)?.preview || '';

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      zIndex: 1000,
      padding: '20px'
    }}>
      <div style={{
        backgroundColor: 'white',
        borderRadius: '8px',
        padding: '24px',
        width: '100%',
        maxWidth: '600px',
        maxHeight: '90vh',
        overflowY: 'auto',
        position: 'relative',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.15)'
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '20px',
          borderBottom: '1px solid #e0e0e0',
          paddingBottom: '12px'
        }}>
          <h2 style={{ margin: 0, fontSize: '1.5rem', color: '#333' }}>Speech-to-Text Settings</h2>
          <button
            onClick={onClose}
            style={{
              background: 'none',
              border: 'none',
              fontSize: '1.5rem',
              cursor: 'pointer',
              color: '#666',
              padding: '0',
              width: '30px',
              height: '30px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
            aria-label="Close"
          >
            ×
          </button>
        </div>
        {loading ? (
          <div style={{ textAlign: 'center', padding: '20px' }}>Loading STT settings...</div>
        ) : (
          <>
            {/* Language Selection */}
            <div style={{ marginBottom: '24px' }}>
              <label style={{
                display: 'block',
                marginBottom: '8px',
                fontSize: '1rem',
                fontWeight: 600,
                color: '#39485a',
              }}>
                Language
              </label>
              <select
                value={settings.language}
                onChange={handleLanguageChange}
                style={{
                  width: '100%',
                  padding: '12px 16px',
                  border: '1.5px solid #DBE7F8',
                  borderRadius: '12px',
                  fontSize: '1rem',
                  backgroundColor: '#fff',
                  color: '#2E3C54',
                  cursor: 'pointer',
                  outline: 'none',
                  transition: 'border-color 0.2s',
                }}
                onFocus={(e) => e.target.style.borderColor = '#7bb8ff'}
                onBlur={(e) => e.target.style.borderColor = '#DBE7F8'}
              >
                {languages.map(lang => (
                  <option key={lang.code} value={lang.code}>
                    {lang.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Model Selection */}
            <div style={{ marginBottom: '24px' }}>
              <label style={{
                display: 'block',
                marginBottom: '8px',
                fontSize: '1rem',
                fontWeight: 600,
                color: '#39485a',
              }}>
                Model Size
              </label>
              <select
                value={settings.model}
                onChange={handleModelChange}
                style={{
                  width: '100%',
                  padding: '12px 16px',
                  border: '1.5px solid #DBE7F8',
                  borderRadius: '12px',
                  fontSize: '1rem',
                  backgroundColor: '#fff',
                  color: '#2E3C54',
                  cursor: 'pointer',
                  outline: 'none',
                  transition: 'border-color 0.2s',
                }}
                onFocus={(e) => e.target.style.borderColor = '#7bb8ff'}
                onBlur={(e) => e.target.style.borderColor = '#DBE7F8'}
              >
                <option value="tiny">Tiny (Fastest, Lower Accuracy)</option>
                <option value="base">Base (Balanced)</option>
                <option value="small">Small (Better Accuracy)</option>
                <option value="medium">Medium (High Accuracy)</option>
                <option value="large">Large (Best Accuracy, Slowest)</option>
              </select>
            </div>

            {/* Wake Word Section */}
            <div style={{
              marginBottom: '24px',
              padding: '20px',
              backgroundColor: '#fff',
              borderRadius: '12px',
              border: '1.5px solid #E7EFFC',
            }}>
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                marginBottom: '16px',
              }}>
                <label style={{
                  fontSize: '1rem',
                  fontWeight: 600,
                  color: '#39485a',
                  cursor: 'pointer',
                }}>
                  Enable Wake Word Detection
                </label>
                <label style={{
                  position: 'relative',
                  display: 'inline-block',
                  width: '48px',
                  height: '24px',
                  cursor: 'pointer',
                }}>
                  <input
                    type="checkbox"
                    checked={settings.enable_wake_word}
                    onChange={handleWakeWordToggle}
                    style={{
                      opacity: 0,
                      width: 0,
                      height: 0,
                    }}
                  />
                  <span style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    bottom: 0,
                    backgroundColor: settings.enable_wake_word ? '#7bb8ff' : '#ccc',
                    borderRadius: '24px',
                    transition: 'background-color 0.3s',
                  }}>
                    <span style={{
                      position: 'absolute',
                      content: '""',
                      height: '18px',
                      width: '18px',
                      left: settings.enable_wake_word ? '26px' : '3px',
                      bottom: '3px',
                      backgroundColor: 'white',
                      borderRadius: '50%',
                      transition: 'left 0.3s',
                      boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
                    }} />
                  </span>
                </label>
              </div>

              {settings.enable_wake_word && (
                <div>
                  <label style={{
                    display: 'block',
                    marginBottom: '8px',
                    fontSize: '0.95rem',
                    fontWeight: 500,
                    color: '#5F6368',
                  }}>
                    Wake Word
                  </label>
                  <div style={{ position: 'relative' }}>
                    <select
                      value={settings.wake_words}
                      onChange={handleWakeWordChange}
                      onMouseEnter={(e) => setHoveredWakeWord(settings.wake_words)}
                      onMouseLeave={() => setHoveredWakeWord(null)}
                      style={{
                        width: '100%',
                        padding: '12px 16px',
                        border: '1.5px solid #DBE7F8',
                        borderRadius: '12px',
                        fontSize: '1rem',
                        backgroundColor: '#fff',
                        color: '#2E3C54',
                        cursor: 'pointer',
                        outline: 'none',
                        transition: 'border-color 0.2s',
                      }}
                      onFocus={(e) => e.target.style.borderColor = '#7bb8ff'}
                      onBlur={(e) => e.target.style.borderColor = '#DBE7F8'}
                    >
                      {wakeWords.map(ww => (
                        <option key={ww.value} value={ww.value}>
                          {ww.value}
                        </option>
                      ))}
                    </select>
                    {/* Wake word preview */}
                    {hoveredWakeWord === settings.wake_words && selectedWakeWordPreview && (
                      <div style={{
                        position: 'absolute',
                        top: '100%',
                        left: 0,
                        right: 0,
                        marginTop: '8px',
                        padding: '12px',
                        backgroundColor: '#fff',
                        border: '1.5px solid #DBE7F8',
                        borderRadius: '8px',
                        boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
                        fontSize: '0.9rem',
                        color: '#5F6368',
                        zIndex: 100,
                      }}>
                        {selectedWakeWordPreview}
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>

            {/* VAD Sensitivity */}
            <div style={{ marginBottom: '24px' }}>
              <label style={{
                display: 'block',
                marginBottom: '8px',
                fontSize: '1rem',
                fontWeight: 600,
                color: '#39485a',
              }}>
                Silero VAD Sensitivity: {settings.silero_sensitivity.toFixed(1)}
              </label>
              <input
                type="range"
                min="0"
                max="1"
                step="0.1"
                value={settings.silero_sensitivity}
                onChange={handleSileroSensitivityChange}
                style={{
                  width: '100%',
                  height: '8px',
                  borderRadius: '4px',
                  outline: 'none',
                  cursor: 'pointer',
                }}
              />
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                marginTop: '4px',
                fontSize: '0.85rem',
                color: '#738091',
              }}>
                <span>Less Sensitive</span>
                <span>More Sensitive</span>
              </div>
            </div>

            {/* WebRTC Sensitivity */}
            <div style={{ marginBottom: '24px' }}>
              <label style={{
                display: 'block',
                marginBottom: '8px',
                fontSize: '1rem',
                fontWeight: 600,
                color: '#39485a',
              }}>
                WebRTC VAD Sensitivity: {settings.webrtc_sensitivity}
              </label>
              <input
                type="range"
                min="0"
                max="3"
                step="1"
                value={settings.webrtc_sensitivity}
                onChange={handleWebRTCSensitivityChange}
                style={{
                  width: '100%',
                  height: '8px',
                  borderRadius: '4px',
                  outline: 'none',
                  cursor: 'pointer',
                }}
              />
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                marginTop: '4px',
                fontSize: '0.85rem',
                color: '#738091',
              }}>
                <span>Most Sensitive</span>
                <span>Least Sensitive</span>
              </div>
            </div>

            {/* Post Speech Silence Duration */}
            <div>
              <label style={{
                display: 'block',
                marginBottom: '8px',
                fontSize: '1rem',
                fontWeight: 600,
                color: '#39485a',
              }}>
                Post Speech Silence Duration: {settings.post_speech_silence_duration.toFixed(1)}s
              </label>
              <input
                type="range"
                min="0.1"
                max="2"
                step="0.1"
                value={settings.post_speech_silence_duration}
                onChange={handlePostSpeechSilenceChange}
                style={{
                  width: '100%',
                  height: '8px',
                  borderRadius: '4px',
                  outline: 'none',
                  cursor: 'pointer',
                }}
              />
              <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                marginTop: '4px',
                fontSize: '0.85rem',
                color: '#738091',
              }}>
                <span>Shorter</span>
                <span>Longer</span>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default STTSettings;

