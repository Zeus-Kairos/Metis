import React, { useState, useEffect, useCallback } from 'react';
import useChatStore, { fetchWithAuth } from './store';
import './RightSidebar.css';

const RightSidebar = ({ isOpen, onToggle, onExpand }) => {
  const { knowledgebases } = useChatStore();
  const [activeKB, setActiveKB] = useState(knowledgebases.find(kb => kb.is_active));
  const [currentPath, setCurrentPath] = useState(['']);
  const [folders, setFolders] = useState([]);
  const [files, setFiles] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  
  // Update activeKB when knowledgebases change
  useEffect(() => {
    const newActiveKB = knowledgebases.find(kb => kb.is_active);
    setActiveKB(newActiveKB);
    if (newActiveKB) {
      // Reset path and refetch when knowledgebase changes
      setCurrentPath(['']);
    }
  }, [knowledgebases]);
  
  // Fetch directory contents
  const fetchDirectoryContents = useCallback(async (path) => {
    if (!activeKB) return;
    
    setIsLoading(true);
    setError('');
    try {
      const fullPath = path.join('/').replace(/^\//, '');
      const response = await fetchWithAuth(`/api/knowledgebase/list?path=${encodeURIComponent(fullPath)}&knowledge_base=${encodeURIComponent(activeKB.name)}`);
      
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
  }, [activeKB]);
  
  // Fetch initial directory contents when path changes
  useEffect(() => {
    fetchDirectoryContents(currentPath);
  }, [currentPath, fetchDirectoryContents]);
  
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
  
  // Get the display name for the current path
  const getPathDisplayName = () => {
    if (currentPath.length === 1) {
      return 'Root';
    }
    return currentPath[currentPath.length - 1];
  };
  
  return (
    <div className={`right-sidebar ${isOpen ? 'open' : 'closed'}`}>
      {isOpen ? (
        <div className="right-sidebar-content">
          <div className="right-sidebar-header">
            <h3>Knowledge Base</h3>
            <div className="right-sidebar-actions">
              <button 
                className="expand-button"
                onClick={onExpand}
                title="Open Knowledge Base Browser"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 3v18h18M19 9l-7 7-7-7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
              <button 
                className="toggle-button"
                onClick={onToggle}
                title="Close Sidebar"
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
          
          {activeKB ? (
            <div className="right-sidebar-body">
              <div className="active-knowledgebase">
                <div className="kb-name">{activeKB.name}</div>
                <div className="kb-description">{activeKB.description || 'No description'}</div>
              </div>
              
              {/* File Browser */}
              <div className="file-browser-section">
                <div className="file-browser-header">
                  <h4>Files</h4>
                  <div className="path-navigator">
                    <span 
                      className={`path-item ${currentPath.length === 1 ? 'active' : ''}`}
                      onClick={navigateUp}
                    >
                      📁
                    </span>
                    {currentPath.slice(1).map((pathSegment, index) => (
                      <React.Fragment key={index}>
                        <span className="path-separator">/</span>
                        <span 
                          className="path-item"
                          onClick={() => setCurrentPath(currentPath.slice(0, index + 2))}
                        >
                          {pathSegment}
                        </span>
                      </React.Fragment>
                    ))}
                  </div>
                </div>
                
                {isLoading ? (
                  <div className="loading-indicator">Loading...</div>
                ) : error ? (
                  <div className="file-browser-error">{error}</div>
                ) : (
                  <div className="file-browser-content">
                    {/* Folders */}
                    {folders.length > 0 && (
                      <div className="file-browser-items">
                        {folders.map((folder, index) => (
                          <div 
                            key={index} 
                            className="file-browser-item folder-item"
                            onClick={() => navigateToFolder(folder)}
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="item-icon">
                              <path d="M20 20H4V6L10 3L16 6V20Z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                            </svg>
                            <span className="item-name">{folder}</span>
                          </div>
                        ))}
                      </div>
                    )}
                    
                    {/* Files */}
                    {files.length > 0 && (
                      <div className="file-browser-items">
                        {files.map((file, index) => (
                          <div key={index} className="file-browser-item file-item">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="item-icon">
                              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              <polyline points="14 2 14 8 20 8" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              <line x1="16" y1="13" x2="8" y2="13" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              <line x1="16" y1="17" x2="8" y2="17" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              <polyline points="10 9 9 9 8 9" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                            </svg>
                            <span className="item-name">{file.name}</span>
                            <span className="item-size">{file.size}</span>
                          </div>
                        ))}
                      </div>
                    )}
                    
                    {folders.length === 0 && files.length === 0 && (
                      <div className="empty-folder">
                        <p>Empty folder</p>
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          ) : (
            <div className="no-active-kb">
              <p>No active knowledge base</p>
            </div>
          )}
        </div>
      ) : (
        <div className="right-sidebar-collapsed">
          <button 
            className="expand-button-collapsed"
            onClick={onToggle}
            title="Open Knowledge Base Sidebar"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M3 19V5a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
      )}
    </div>
  );
};

export default RightSidebar;