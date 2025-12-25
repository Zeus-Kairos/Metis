import React, { useState, useEffect, useCallback } from 'react';
import { fetchWithAuth } from './store';
import useChatStore from './store';
import './KnowledgebaseBrowser.css';

const KnowledgebaseBrowser = () => {
  const { knowledgebases, setActiveKnowledgebase, refreshFileBrowser } = useChatStore();
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
  // New state variables for knowledgebase management
  const [showCreateKBModal, setShowCreateKBModal] = useState(false);
  const [newKBName, setNewKBName] = useState('');
  const [newKBDescription, setNewKBDescription] = useState('');
  const [showRenameKBModal, setShowRenameKBModal] = useState(false);
  const [kbToRename, setKBToRename] = useState(null);
  const [renameKBName, setRenameKBName] = useState('');
  // State variables for editing knowledgebase descriptions
  const [showEditKBDescriptionModal, setShowEditKBDescriptionModal] = useState(false);
  const [kbToEditDescription, setKBToEditDescription] = useState(null);
  const [editKBDescription, setEditKBDescription] = useState('');
  
  // Update currentKnowledgebase when knowledgebases change
  useEffect(() => {
    const activeKB = knowledgebases.find(kb => kb.is_active);
    if (activeKB) {
      setCurrentKnowledgebase(activeKB.name);
    }
  }, [knowledgebases]);

  // Fetch directory contents - memoized with useCallback to prevent infinite loops
  const fetchDirectoryContents = useCallback(async (path) => {
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
  }, [currentKnowledgebase]);

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
      const fullPath = currentPath.join('/').replace(/^\//, '');
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
      refreshFileBrowser(); // Trigger sidebar refresh
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
      const fullPath = [...currentPath, folderName].join('/').replace(/^\//, '');
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
      fetchDirectoryContents(currentPath.join('/').replace(/^\//, ''));
      refreshFileBrowser(); // Trigger sidebar refresh
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
      const fullPath = [...currentPath, fileName].join('/').replace(/^\//, '');
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
      fetchDirectoryContents(currentPath.join('/').replace(/^\//, ''));
      refreshFileBrowser(); // Trigger sidebar refresh
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
      const fullPath = currentPath.join('/').replace(/^\//, '');
      
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

      // Always parse the JSON response body
      const responseData = await response.json();
      
      // Handle error response format
      if (responseData.detail) {
        throw new Error(responseData.detail);
      }
      
      // Show detailed error message if any files failed
      const failedFiles = responseData.files ? responseData.files.filter(file => file.status === 'failed') : [];
      if (failedFiles.length > 0) {
        const errorMessages = failedFiles.map(file => `${file.filename}: ${file.error || 'Unknown error'}`);
        throw new Error(`Upload failed for ${failedFiles.length} file(s):\n${errorMessages.join('\n')}`);
      }

      // Refresh directory contents
      fetchDirectoryContents(fullPath);
      refreshFileBrowser(); // Trigger sidebar refresh
      setShowUploadDialog(false);
      setSelectedFiles([]);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Create a new knowledgebase
  const createKnowledgebase = async () => {
    if (!newKBName.trim()) return;

    setIsLoading(true);
    setError('');
    try {
      const response = await fetchWithAuth('/api/knowledgebase', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: newKBName,
          description: newKBDescription,
          navigation: {}
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to create knowledgebase');
      }

      // Refresh knowledgebases by setting the newly created one as active
      const result = await response.json();
      setActiveKnowledgebase(result.knowledgebase_id);
      
      // Reset form
      setShowCreateKBModal(false);
      setNewKBName('');
      setNewKBDescription('');
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Rename a knowledgebase
  const renameKnowledgebase = async () => {
    if (!renameKBName.trim() || !kbToRename) return;

    setIsLoading(true);
    setError('');
    try {
      const response = await fetchWithAuth(`/api/knowledgebase/${kbToRename.id}/rename`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: renameKBName
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to rename knowledgebase');
      }

      // Refresh knowledgebases by fetching them again
      const kbsResponse = await fetchWithAuth('/api/knowledgebase');
      if (kbsResponse.ok) {
        const kbsData = await kbsResponse.json();
        // Update the store's knowledgebases directly
        useChatStore.setState({ knowledgebases: kbsData.knowledgebases || [] });
        
        // Set the active knowledgebase if one exists
        const activeKB = kbsData.knowledgebases.find(kb => kb.is_active);
        if (activeKB) {
          setActiveKnowledgebase(activeKB.id);
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Edit knowledgebase description
  const editKnowledgebaseDescription = async () => {
    if (!kbToEditDescription) return;

    setIsLoading(true);
    setError('');
    try {
      const response = await fetchWithAuth(`/api/knowledgebase/${kbToEditDescription.id}/description`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          description: editKBDescription
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to update knowledgebase description');
      }

      // Refresh knowledgebases by fetching them again
      const kbsResponse = await fetchWithAuth('/api/knowledgebase');
      if (kbsResponse.ok) {
        const kbsData = await kbsResponse.json();
        // Update the store's knowledgebases directly
        useChatStore.setState({ knowledgebases: kbsData.knowledgebases || [] });
        
        // Set the active knowledgebase if one exists
        const activeKB = kbsData.knowledgebases.find(kb => kb.is_active);
        if (activeKB) {
          setActiveKnowledgebase(activeKB.id);
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Delete a knowledgebase
  const deleteKnowledgebase = async (kbId, kbName) => {
    // Prevent deletion if this is the only knowledgebase
    if (knowledgebases.length <= 1) {
      window.alert('Cannot delete the only knowledgebase.');
      return;
    }

    if (!window.confirm(`Are you sure you want to delete knowledgebase "${kbName}"? This action cannot be undone.`)) {
      return;
    }

    setIsLoading(true);
    setError('');
    try {
      const response = await fetchWithAuth(`/api/knowledgebase/${kbId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to delete knowledgebase');
      }

      // Refresh knowledgebases by fetching them again
      const kbsResponse = await fetchWithAuth('/api/knowledgebase');
      if (kbsResponse.ok) {
        const kbsData = await kbsResponse.json();
        // Update the store's knowledgebases directly
        useChatStore.setState({ knowledgebases: kbsData.knowledgebases || [] });
        
        // Set the active knowledgebase if one exists
        const activeKB = kbsData.knowledgebases.find(kb => kb.is_active);
        if (activeKB) {
          setActiveKnowledgebase(activeKB.id);
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Fetch directory contents when currentPath changes
  useEffect(() => {
    fetchDirectoryContents(currentPath.join('/').replace(/^\//, ''));
  }, [currentPath, fetchDirectoryContents]);

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
        <div className="kb-knowledgebase-list-wrapper">
          <div className="kb-knowledgebase-list">
            {knowledgebases.map((kb) => (
              <div 
              key={kb.id}
              className={`kb-knowledgebase-item ${kb.is_active ? 'active' : ''}`}
            >
              <div 
                className="kb-knowledgebase-name"
                onClick={() => {
                  setActiveKnowledgebase(kb.id);
                }}
              >
                {kb.name}
                {kb.is_active && <span className="kb-knowledgebase-active-indicator">✓</span>}
              </div>
              <div className="kb-knowledgebase-actions">
                <button 
                  className="kb-knowledgebase-edit-btn"
                  onClick={(e) => {
                    e.stopPropagation();
                    setKBToEditDescription(kb);
                    setEditKBDescription(kb.description || '');
                    setShowEditKBDescriptionModal(true);
                  }}
                  title="Edit knowledgebase description"
                >
                  ✎
                </button>
                <button 
                  className="kb-knowledgebase-delete-btn"
                  onClick={(e) => {
                    e.stopPropagation();
                    if (knowledgebases.length <= 1) {
                      window.alert('Cannot delete the only knowledgebase.');
                      return;
                    }
                    deleteKnowledgebase(kb.id, kb.name);
                  }}
                  disabled={knowledgebases.length <= 1}
                  title={knowledgebases.length <= 1 ? 'Cannot delete the only knowledgebase' : 'Delete knowledgebase'}
                >
                  🗑️
                </button>
              </div>
            </div>
            ))}
          </div>
          <button 
            onClick={() => setShowCreateKBModal(true)} 
            className="kb-btn kb-btn-tertiary kb-new-kb-btn"
            disabled={isLoading}
            title="Create new knowledgebase"
          >
            +
          </button>
        </div>
      </div>

      {/* Active Knowledgebase Description */}
      {(() => {
        const activeKB = knowledgebases.find(kb => kb.is_active);
        if (activeKB && activeKB.description) {
          return (
            <div className="kb-active-description">
              <div className="kb-active-description-title">Description:</div>
              <div className="kb-active-description-content">
                {activeKB.description}
              </div>
            </div>
          );
        }
        return null;
      })()}

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

      {/* Create Knowledgebase Modal */}
      {showCreateKBModal && (
        <div className="kb-dialog-overlay">
          <div className="kb-dialog">
            <div className="dialog-header">
              <h3>Create New Knowledgebase</h3>
              <button 
                className="dialog-close"
                onClick={() => {
                  setShowCreateKBModal(false);
                  setNewKBName('');
                  setNewKBDescription('');
                }}
              >
                ×
              </button>
            </div>
            <div className="dialog-body">
              <div className="form-group">
                <label htmlFor="new-kb-name">Name *</label>
                <input
                  type="text"
                  id="new-kb-name"
                  value={newKBName}
                  onChange={(e) => setNewKBName(e.target.value)}
                  placeholder="Enter knowledgebase name"
                  autoFocus
                />
              </div>
              <div className="form-group">
                <label htmlFor="new-kb-description">Description</label>
                <textarea
                  id="new-kb-description"
                  value={newKBDescription}
                  onChange={(e) => setNewKBDescription(e.target.value)}
                  placeholder="Enter knowledgebase description (optional)"
                  rows="3"
                />
              </div>
            </div>
            <div className="dialog-footer">
              <button 
                onClick={() => {
                  setShowCreateKBModal(false);
                  setNewKBName('');
                  setNewKBDescription('');
                }}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                onClick={createKnowledgebase}
                className="dialog-primary"
                disabled={isLoading || !newKBName.trim()}
              >
                Create
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Edit Knowledgebase Description Modal */}
      {showEditKBDescriptionModal && kbToEditDescription && (
        <div className="kb-dialog-overlay">
          <div className="kb-dialog">
            <div className="dialog-header">
              <h3>Edit Knowledgebase Description</h3>
              <button 
                className="dialog-close"
                onClick={() => {
                  setShowEditKBDescriptionModal(false);
                  setKBToEditDescription(null);
                  setEditKBDescription('');
                }}
              >
                ×
              </button>
            </div>
            <div className="dialog-body">
              <div className="form-group">
                <label htmlFor="edit-kb-name">Knowledgebase</label>
                <input
                  type="text"
                  id="edit-kb-name"
                  value={kbToEditDescription.name}
                  readOnly
                  className="read-only-input"
                />
              </div>
              <div className="form-group">
                <label htmlFor="edit-kb-description">Description</label>
                <textarea
                  id="edit-kb-description"
                  value={editKBDescription}
                  onChange={(e) => setEditKBDescription(e.target.value)}
                  placeholder="Enter knowledgebase description"
                  rows="4"
                  autoFocus
                />
              </div>
            </div>
            <div className="dialog-footer">
              <button 
                onClick={() => {
                  setShowEditKBDescriptionModal(false);
                  setKBToEditDescription(null);
                  setEditKBDescription('');
                }}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                onClick={editKnowledgebaseDescription}
                className="dialog-primary"
                disabled={isLoading}
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Rename Knowledgebase Modal */}
      {/* Commented out to hide rename functionality temporarily */}
      {/* {showRenameKBModal && kbToRename && (
        <div className="kb-dialog-overlay">
          <div className="kb-dialog">
            <div className="dialog-header">
              <h3>Rename Knowledgebase</h3>
              <button 
                className="dialog-close"
                onClick={() => {
                  setShowRenameKBModal(false);
                  setKBToRename(null);
                  setRenameKBName('');
                }}
              >
                ×
              </button>
            </div>
            <div className="dialog-body">
              <div className="form-group">
                <label htmlFor="rename-kb-name">Name *</label>
                <input
                  type="text"
                  id="rename-kb-name"
                  value={renameKBName}
                  onChange={(e) => setRenameKBName(e.target.value)}
                  placeholder="Enter new knowledgebase name"
                  autoFocus
                />
              </div>
            </div>
            <div className="dialog-footer">
              <button 
                onClick={() => {
                  setShowRenameKBModal(false);
                  setKBToRename(null);
                  setRenameKBName('');
                }}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                onClick={renameKnowledgebase}
                className="dialog-primary"
                disabled={isLoading || !renameKBName.trim()}
              >
                Rename
              </button>
            </div>
          </div>
        </div>
      )} */}
    </div>
  );
};

export default KnowledgebaseBrowser;