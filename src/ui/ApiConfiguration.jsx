import React, { useState, useEffect } from 'react';
import useChatStore, { fetchWithAuth } from './store';
import './ApiConfiguration.css';

const ApiConfiguration = ({ isOpen, onClose }) => {
  const [config, setConfig] = useState({
    api_key: '',
    llm_model: '',
    embedding_model: '',
    model_provider: '',
    api_base_url: ''
  });
  const [isLoading, setIsLoading] = useState(false);
  const [isSaving, setIsSaving] = useState(false);
  const [message, setMessage] = useState(null);

  // Fetch configuration when modal opens
  useEffect(() => {
    if (isOpen) {
      fetchConfig();
    }
  }, [isOpen]);

  // Fetch user configuration from API
  const fetchConfig = async () => {
    try {
      setIsLoading(true);
      setMessage(null);
      
      const response = await fetchWithAuth('/api/users/config');
      
      if (response.ok) {
        const data = await response.json();
        if (data.config) {
          setConfig({
            api_key: data.config.api_key || '',
            llm_model: data.config.llm_model || '',
            embedding_model: data.config.embedding_model || '',
            model_provider: data.config.model_provider || '',
            api_base_url: data.config.api_base_url || ''
          });
        }
      } else {
        setMessage({ type: 'error', text: 'Failed to fetch configuration' });
      }
    } catch (error) {
      console.error('Error fetching configuration:', error);
      setMessage({ type: 'error', text: 'Error fetching configuration' });
    } finally {
      setIsLoading(false);
    }
  };

  // Save user configuration to API
  const handleSave = async () => {
    try {
      setIsSaving(true);
      setMessage(null);
      
      const response = await fetchWithAuth('/api/users/config', {
        method: 'PATCH',
        body: JSON.stringify(config)
      });
      
      if (response.ok) {
        const data = await response.json();
        setMessage({ type: 'success', text: 'Configuration saved successfully' });
        
        // Update local config with the response
        if (data.config) {
          setConfig({
            api_key: data.config.api_key || '',
            llm_model: data.config.llm_model || '',
            embedding_model: data.config.embedding_model || '',
            model_provider: data.config.model_provider || '',
            api_base_url: data.config.api_base_url || ''
          });
        }
      } else {
        setMessage({ type: 'error', text: 'Failed to save configuration' });
      }
    } catch (error) {
      console.error('Error saving configuration:', error);
      setMessage({ type: 'error', text: 'Error saving configuration' });
    } finally {
      setIsSaving(false);
    }
  };

  // Handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setConfig(prev => ({
      ...prev,
      [name]: value
    }));
  };

  if (!isOpen) return null;

  return (
    <div className="api-config-modal-overlay">
      <div className="api-config-modal">
        <div className="api-config-modal-header">
          <h2>API Configuration</h2>
          <button 
            className="api-config-close-btn"
            onClick={onClose}
            disabled={isSaving}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
        
        <div className="api-config-modal-content">
          {message && (
            <div className={`api-config-message ${message.type}`}>
              {message.text}
            </div>
          )}
          
          {isLoading ? (
            <div className="api-config-loading">Loading configuration...</div>
          ) : (
            <div className="api-config-form">
              <div className="api-config-form-group">
                <label htmlFor="api_key">API Key</label>
                <input
                  type="password"
                  id="api_key"
                  name="api_key"
                  value={config.api_key}
                  onChange={handleInputChange}
                  placeholder="Enter API key"
                  disabled={isSaving}
                />
              </div>
              
              <div className="api-config-form-group">
                <label htmlFor="llm_model">LLM Model</label>
                <input
                  type="text"
                  id="llm_model"
                  name="llm_model"
                  value={config.llm_model}
                  onChange={handleInputChange}
                  placeholder="e.g., gpt-4"
                  disabled={isSaving}
                />
              </div>
              
              <div className="api-config-form-group">
                <label htmlFor="embedding_model">Embedding Model</label>
                <input
                  type="text"
                  id="embedding_model"
                  name="embedding_model"
                  value={config.embedding_model}
                  onChange={handleInputChange}
                  placeholder="e.g., text-embedding-ada-002"
                  disabled={isSaving}
                />
              </div>
              
              <div className="api-config-form-group">
                <label htmlFor="model_provider">Model Provider</label>
                <input
                  type="text"
                  id="model_provider"
                  name="model_provider"
                  value={config.model_provider}
                  onChange={handleInputChange}
                  placeholder="e.g., openai"
                  disabled={isSaving}
                />
              </div>
              
              <div className="api-config-form-group">
                <label htmlFor="api_base_url">API Base URL</label>
                <input
                  type="text"
                  id="api_base_url"
                  name="api_base_url"
                  value={config.api_base_url}
                  onChange={handleInputChange}
                  placeholder="e.g., https://api.openai.com/v1"
                  disabled={isSaving}
                />
              </div>
            </div>
          )}
        </div>
        
        <div className="api-config-modal-footer">
          <button 
            className="api-config-cancel-btn"
            onClick={onClose}
            disabled={isSaving}
          >
            Cancel
          </button>
          <button 
            className="api-config-save-btn"
            onClick={handleSave}
            disabled={isSaving}
          >
            {isSaving ? 'Saving...' : 'Save'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ApiConfiguration;