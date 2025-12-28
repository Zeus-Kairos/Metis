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
  const [fileItems, setFileItems] = useState([]); // Contains files and folders with their descriptions
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
  const [showInlineEdit, setShowInlineEdit] = useState(false);
  const [kbToEditDescription, setKBToEditDescription] = useState(null);
  const [editKBDescription, setEditKBDescription] = useState('');
  
  // State variables for bulk editing file/folder descriptions
  const [showEditDescriptionsModal, setShowEditDescriptionsModal] = useState(false);
  const [editingFiles, setEditingFiles] = useState([]);
  
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
      // Get the active knowledgebase to get its ID
      const activeKB = knowledgebases.find(kb => kb.is_active);
      if (!activeKB) {
        throw new Error('No active knowledgebase found');
      }
      
      // Call API with kb_id instead of knowledge_base name
      const response = await fetchWithAuth(`/api/knowledgebase/list?path=${encodeURIComponent(path)}&kb_id=${activeKB.id}&knowledge_base=${encodeURIComponent(activeKB.name)}`);
      if (!response.ok) {
        throw new Error('Failed to fetch directory contents');
      }
      const data = await response.json();
      
      // Extract just the names for backward compatibility with existing UI
      const folderNames = data.folders?.map(folder => folder.name) || [];
      const fileNames = data.files?.map(file => file.name) || [];
      
      setFolders(folderNames);
      setFiles(fileNames);
      
      // Store the full file items with their metadata for display
      const allItems = [];
      
      // Add folders with metadata
      if (Array.isArray(data.folders)) {
        data.folders.forEach(folder => {
          allItems.push({
            id: folder.id,
            name: folder.name,
            type: 'folder',
            uploaded_time: folder.uploaded_time,
            description: folder.description
          });
        });
      }
      
      // Add files with metadata
      if (Array.isArray(data.files)) {
        data.files.forEach(file => {
          allItems.push({
            id: file.id,
            name: file.name,
            type: 'file',
            uploaded_time: file.uploaded_time,
            file_size: file.file_size,
            description: file.description
          });
        });
      }
      
      setFileItems(allItems);
    } catch (err) {
      setError(err.message);
      // Clear fileItems on error
      setFileItems([]);
    } finally {
      setIsLoading(false);
    }
  }, [currentKnowledgebase, knowledgebases]);

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

  // Use current directory's items when edit descriptions modal is opened
  useEffect(() => {
    if (showEditDescriptionsModal) {
      // Use the existing fileItems from the current directory
      setEditingFiles(fileItems);
    }
  }, [showEditDescriptionsModal, fileItems]);

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
          <button 
            onClick={() => setShowEditDescriptionsModal(true)} 
            className="kb-btn kb-btn-secondary"
            disabled={isLoading}
          >
            Edit Descriptions
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

      {/* Active Knowledgebase Description with inline edit */}
      {(() => {
        const activeKB = knowledgebases.find(kb => kb.is_active);
        if (activeKB) {
          return (
            <div className="kb-active-description">
              <div className="kb-active-description-title">
                <span>Description:</span>
                <button 
                  className="kb-knowledgebase-edit-btn"
                  onClick={() => {
                    setKBToEditDescription(activeKB);
                    setEditKBDescription(activeKB.description || '');
                    setShowInlineEdit(true);
                  }}
                  title="Edit knowledgebase description"
                >
                  ✎
                </button>
              </div>
              {showInlineEdit && kbToEditDescription && kbToEditDescription.id === activeKB.id ? (
                <div className="kb-active-description-edit">
                  <textarea
                    value={editKBDescription}
                    onChange={(e) => setEditKBDescription(e.target.value)}
                    placeholder="Enter knowledgebase description"
                    rows="3"
                    style={{ width: '100%', marginBottom: '8px' }}
                    autoFocus
                  />
                  <div style={{ display: 'flex', gap: '8px', justifyContent: 'flex-end' }}>
                    <button 
                      onClick={() => {
                        setShowInlineEdit(false);
                        setKBToEditDescription(null);
                        setEditKBDescription('');
                      }}
                      style={{ padding: '4px 8px', fontSize: '14px' }}
                    >
                      Cancel
                    </button>
                    <button 
                      onClick={async () => {
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
                          
                          setShowInlineEdit(false);
                          setKBToEditDescription(null);
                          setEditKBDescription('');
                        } catch (err) {
                          setError(err.message);
                        } finally {
                          setIsLoading(false);
                        }
                      }}
                      className="dialog-primary"
                      style={{ padding: '4px 8px', fontSize: '14px' }}
                      disabled={isLoading}
                    >
                      Save
                    </button>
                  </div>
                </div>
              ) : (
                <div className="kb-active-description-content">
                  {activeKB.description || 'No description available'}
                </div>
              )}
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
            {fileItems.length === 0 ? (
              <div className="kb-empty">No items found</div>
            ) : (
              <div className="kb-items">
                {/* Sort items: folders first, then files, both by name */}
                {fileItems
                  .sort((a, b) => {
                    // Sort folders before files
                    if (a.type === 'folder' && b.type !== 'folder') return -1;
                    if (a.type !== 'folder' && b.type === 'folder') return 1;
                    // Sort by name
                    return a.name.localeCompare(b.name);
                  })
                  .map((item) => (
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
                        <div className="item-details">
                          <div className="item-header">
                            <div className="item-title-container">
                              <span className="item-name">{item.name}</span>
                              {item.type === 'file' && item.file_size && (
                                <span className="item-size">({(item.file_size / 1024).toFixed(2)} KB)</span>
                              )}
                            </div>
                            {item.uploaded_time && (
                              <span className="item-uploaded-time">
                                {new Date(item.uploaded_time).toLocaleString()}
                              </span>
                            )}
                          </div>
                          {item.description && (
                            <div className="item-description">{item.description}</div>
                          )}
                        </div>
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

      {/* Edit File/Folder Descriptions Modal */}
      {showEditDescriptionsModal && (
        <div className="kb-dialog-overlay">
          <div className="kb-dialog" style={{ maxWidth: '780px', maxHeight: '90vh' }}>
            <div className="dialog-header">
              <h3>Edit File & Folder Descriptions</h3>
              <button 
                className="dialog-close"
                onClick={() => {
                  setShowEditDescriptionsModal(false);
                  setEditingFiles([]);
                }}
              >
                ×
              </button>
            </div>
            <div className="dialog-body" style={{ overflowY: 'auto', maxHeight: '65vh' }}>
              {isLoading ? (
                <div className="kb-loading">Loading files...</div>
              ) : editingFiles.length === 0 ? (
                <div className="kb-empty">No files found to edit</div>
              ) : (
                <div className="edit-descriptions-list">
                  {editingFiles.map((file) => (
                    <div key={`${file.type}-${file.id}-${file.name}`} className="edit-description-item">
                      <div className="edit-description-item-header">
                        <span className={`item-icon ${file.type}-icon`}>
                          {file.type === 'folder' ? '📁' : '📄'}
                        </span>
                        <span className="item-name">{file.name}</span>
                        {file.type === 'file' && file.file_size && (
                          <span className="item-size">({(file.file_size / 1024).toFixed(2)} KB)</span>
                        )}
                      </div>
                      <div className="form-group">
                        <label htmlFor={`description-${file.id}`}>Description</label>
                        <textarea
                          id={`description-${file.id}`}
                          value={file.description || ''}
                          onChange={(e) => {
                            setEditingFiles(prev => prev.map(f => 
                              f.id === file.id ? { ...f, description: e.target.value } : f
                            ));
                          }}
                          placeholder="Enter description for this file/folder"
                          rows="2"
                          style={{ fontSize: '13px', padding: '6px 8px' }}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
            <div className="dialog-footer">
              <button 
                onClick={() => {
                  setShowEditDescriptionsModal(false);
                  setEditingFiles([]);
                }}
                disabled={isLoading}
              >
                Cancel
              </button>
              <button 
                onClick={async () => {
                  // Save all updated descriptions
                  setIsLoading(true);
                  setError('');
                  try {
                    const activeKB = knowledgebases.find(kb => kb.is_active);
                    if (!activeKB) {
                      throw new Error('No active knowledgebase found');
                    }

                    // Prepare the updates array
                    const updates = editingFiles.map(file => ({
                      file_id: file.id,
                      description: file.description || ''
                    }));

                    // Call the API to update multiple descriptions
                    const response = await fetchWithAuth(`/api/knowledgebase/${activeKB.id}/descriptions`, {
                      method: 'PUT',
                      headers: {
                        'Content-Type': 'application/json',
                      },
                      body: JSON.stringify(updates),
                    });

                    if (!response.ok) {
                      const errorData = await response.json().catch(() => ({}));
                      throw new Error(errorData.detail || 'Failed to update descriptions');
                    }

                    // Refresh the directory contents to show updated descriptions
                    fetchDirectoryContents(currentPath.join('/').replace(/^\//, ''));
                    refreshFileBrowser(); // Trigger sidebar refresh
                    
                    // Close the modal
                    setShowEditDescriptionsModal(false);
                    setEditingFiles([]);
                  } catch (err) {
                    setError(err.message);
                  } finally {
                    setIsLoading(false);
                  }
                }}
                className="dialog-primary"
                disabled={isLoading}
              >
                Save All Descriptions
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default KnowledgebaseBrowser;