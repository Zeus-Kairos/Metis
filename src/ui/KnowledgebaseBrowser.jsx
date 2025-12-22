import React, { useState, useEffect } from 'react';
import { fetchWithAuth } from './store';
import useChatStore from './store';
import './KnowledgebaseBrowser.css';

const KnowledgebaseBrowser = () => {
  const { knowledgebases, setActiveKnowledgebase } = useChatStore();
  const [currentKnowledgebase, setCurrentKnowledgebase] = useState(knowledgebases.find(kb => kb.is_active)?.name || 'default');
  const [currentPath, setCurrentPath] = useState(['']);
  const [folders, setFolders] = useState([]);
  const [files, setFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [showNewFolderInput, setShowNewFolderInput] = useState(false);
  const [newFolderName, setNewFolderName] = useState('');
  const [showUploadDialog, setShowUploadDialog] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState([]);
  
  // Update currentKnowledgebase when knowledgebases change
  useEffect(() => {
    const activeKB = knowledgebases.find(kb => kb.is_active);
    if (activeKB) {
      setCurrentKnowledgebase(activeKB.name);
    }
  }, [knowledgebases]);

  // Fetch directory contents
  const fetchDirectoryContents = async (path) => {
    setIsLoading(true);
    setError('');
    try {
      const response = await fetchWithAuth(`/api/knowledgebase/list?path=${encodeURIComponent(path)}&knowledge_base=${encodeURIComponent(currentKnowledgebase)}`);
      if (!response.ok) {
        throw new Error('Failed to fetch directory contents');
      }
      const data = await response.json();
      setFolders(data.folders || []);
      setFiles(data.files || []);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Navigate to a folder
  const navigateToFolder = (folderName) => {
    const newPath = [...currentPath, folderName];
    setCurrentPath(newPath);
  };

  // Navigate up one level
  const navigateUp = () => {
    if (currentPath.length > 1) {
      setCurrentPath(currentPath.slice(0, -1));
    }
  };

  // Create a new folder
  const createFolder = async () => {
    if (!newFolderName.trim()) return;

    setIsLoading(true);
    setError('');
    try {
      const fullPath = currentPath.join('/');
      const response = await fetchWithAuth('/api/knowledgebase/folder', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: newFolderName,
          parentPath: fullPath,
          knowledge_base: currentKnowledgebase,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to create folder');
      }

      // Refresh directory contents
      fetchDirectoryContents(fullPath);
      setShowNewFolderInput(false);
      setNewFolderName('');
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Delete a folder
  const deleteFolder = async (folderName) => {
    if (!window.confirm(`Are you sure you want to delete folder "${folderName}"?`)) {
      return;
    }

    setIsLoading(true);
    setError('');
    try {
      const fullPath = [...currentPath, folderName].join('/');
      const response = await fetchWithAuth('/api/knowledgebase/folder', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          path: fullPath,
          knowledge_base: currentKnowledgebase,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to delete folder');
      }

      // Refresh directory contents
      fetchDirectoryContents(currentPath.join('/'));
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Delete a file
  const deleteFile = async (fileName) => {
    if (!window.confirm(`Are you sure you want to delete file "${fileName}"?`)) {
      return;
    }

    setIsLoading(true);
    setError('');
    try {
      const fullPath = [...currentPath, fileName].join('/');
      const response = await fetchWithAuth('/api/knowledgebase/file', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          path: fullPath,
          knowledge_base: currentKnowledgebase,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to delete file');
      }

      // Refresh directory contents
      fetchDirectoryContents(currentPath.join('/'));
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Handle file selection for upload
  const handleFileSelect = (e) => {
    setSelectedFiles(Array.from(e.target.files));
  };

  // Upload files to the current directory
  const uploadFiles = async () => {
    if (selectedFiles.length === 0) return;

    setIsLoading(true);
    setError('');
    try {
      const formData = new FormData();
      const fullPath = currentPath.join('/');
      
      formData.append('knowledge_base', currentKnowledgebase);
      formData.append('directory', fullPath);
      
      selectedFiles.forEach((file) => {
        formData.append('files', file);
      });

      // Use the fixed fetchWithAuth function which now handles FormData correctly
      const response = await fetchWithAuth('/api/upload', {
        method: 'POST',
        body: formData,
        headers: {} // Empty headers to let fetchWithAuth handle it automatically
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to upload files');
      }

      // Refresh directory contents
      fetchDirectoryContents(fullPath);
      setShowUploadDialog(false);
      setSelectedFiles([]);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Fetch directory contents when currentPath changes
  useEffect(() => {
    fetchDirectoryContents(currentPath.join('/'));
  }, [currentPath]);

  return (
    <div className="knowledgebase-browser">
      <div className="kb-header">
        <h2>Knowledge Base</h2>
        <div className="kb-actions">
          <button 
            onClick={() => setShowNewFolderInput(true)} 
            className="kb-btn kb-btn-primary"
            disabled={isLoading}
          >
            New Folder
          </button>
          <button 
            onClick={() => setShowUploadDialog(true)} 
            className="kb-btn kb-btn-secondary"
            disabled={isLoading}
          >
            Upload Files
          </button>
        </div>
      </div>

      {error && <div className="kb-error">{error}</div>}

      {/* Knowledgebase Selector */}
      <div className="kb-knowledgebase-selector">
        <div className="kb-knowledgebase-label">Knowledgebase:</div>
        <div className="kb-knowledgebase-list">
          {knowledgebases.map((kb) => (
            <div 
              key={kb.id}
              className={`kb-knowledgebase-item ${kb.is_active ? 'active' : ''}`}
              onClick={() => {
                setActiveKnowledgebase(kb.id);
              }}
            >
              {kb.name}
              {kb.is_active && <span className="kb-knowledgebase-active-indicator">✓</span>}
            </div>
          ))}
        </div>
      </div>

      {/* Breadcrumb Navigation */}
      <div className="kb-breadcrumb">
        <span 
          className="breadcrumb-item"
          onClick={() => setCurrentPath([''])}
        >
          Root
        </span>
        {currentPath.slice(1).map((folder, index) => (
          <React.Fragment key={index}>
            <span className="breadcrumb-separator">/</span>
            <span 
              className="breadcrumb-item"
              onClick={() => setCurrentPath(currentPath.slice(0, index + 2))}
            >
              {folder}
            </span>
          </React.Fragment>
        ))}
      </div>

      {/* New Folder Input */}
      {showNewFolderInput && (
        <div className="new-folder-input">
          <input
            type="text"
            placeholder="Enter folder name"
            value={newFolderName}
            onChange={(e) => setNewFolderName(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && createFolder()}
            autoFocus
          />
          <div className="input-actions">
            <button onClick={createFolder} disabled={isLoading || !newFolderName.trim()}>
              Create
            </button>
            <button onClick={() => {
              setShowNewFolderInput(false);
              setNewFolderName('');
            }} disabled={isLoading}>
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Directory Contents */}
      <div className="kb-contents">
        {isLoading ? (
          <div className="kb-loading">Loading...</div>
        ) : (
          <div className="kb-section">
            {folders.length + files.length === 0 ? (
              <div className="kb-empty">No items found</div>
            ) : (
              <div className="kb-items">
                {/* Combine folders and files into a single list, sorted with folders first */}
                {[
                  ...folders.map(name => ({ name, type: 'folder' })),
                  ...files.map(name => ({ name, type: 'file' }))
                ].map((item) => (
                  <div 
                    key={`${item.type}-${item.name}`} 
                    className={`kb-item ${item.type}-item`}
                  >
                    <div 
                      className="item-content"
                      onClick={item.type === 'folder' ? () => navigateToFolder(item.name) : undefined}
                    >
                      <span className={`item-icon ${item.type}-icon`}>
                        {item.type === 'folder' ? '📁' : '📄'}
                      </span>
                      <span className="item-name">{item.name}</span>
                    </div>
                    <button 
                      className="item-action delete-action"
                      onClick={() => {
                        if (item.type === 'folder') {
                          deleteFolder(item.name);
                        } else {
                          deleteFile(item.name);
                        }
                      }}
                      title={`Delete ${item.type}`}
                    >
                      🗑️
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>

      {/* Upload Dialog */}
      {showUploadDialog && (
        <div className="kb-dialog-overlay">
          <div className="kb-dialog">
            <div className="dialog-header">
              <h3>Upload Files</h3>
              <button 
                className="dialog-close"
                onClick={() => {
                  setShowUploadDialog(false);
                  setSelectedFiles([]);
                }}
              >
                ×
              </button>
            </div>
            <div className="dialog-body">
              <input
                type="file"
                multiple
                onChange={handleFileSelect}
                className="file-input"
              />
              {selectedFiles.length > 0 && (
                <div className="selected-files">
                  <p>Selected files ({selectedFiles.length}):</p>
                  <ul>
                    {selectedFiles.map((file, index) => (
                      <li key={index}>{file.name}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
            <div className="dialog-footer">
              <button 
                onClick={() => {
                  setShowUploadDialog(false);
                  setSelectedFiles([]);
                }}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                onClick={uploadFiles}
                className="dialog-primary"
                disabled={isLoading || selectedFiles.length === 0}
              >
                Upload
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default KnowledgebaseBrowser;