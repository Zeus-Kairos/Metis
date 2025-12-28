import React, { useState, useEffect, useCallback } from 'react';
import useChatStore, { fetchWithAuth } from './store';
import './RightSidebar.css';

const RightSidebar = ({ isOpen, onToggle, onExpand, isKnowledgebaseView }) => {
  const { knowledgebases, fileBrowserRefreshTrigger, fileBrowserLastModifiedPath } = useChatStore();
  const [activeKB, setActiveKB] = useState(knowledgebases.find(kb => kb.is_active));
  
  // Define file tree structure state
  const [fileTree, setFileTree] = useState({
    type: 'folder',
    name: 'Root',
    path: [''],
    isExpanded: true,
    isLoading: false,
    children: [],
    error: ''
  });
  
  // Cache for directory contents - key is path, value is the fetched data
  const [directoryCache, setDirectoryCache] = useState({});
  
  // Ref to access the latest directoryCache without triggering re-renders
  const directoryCacheRef = React.useRef(directoryCache);
  
  // Update the ref whenever directoryCache changes
  useEffect(() => {
    directoryCacheRef.current = directoryCache;
  }, [directoryCache]);

  
  // Fetch directory contents for a specific folder path
  const fetchDirectoryContents = useCallback(async (folderPath, forceRefresh = false) => {
    if (!activeKB || !activeKB.id || !activeKB.name) {
      console.error('Active knowledgebase not properly defined:', activeKB);
      return [];
    }
    
    const fullPath = folderPath.join('/').replace(/^\//, '');
    
    // Create cache key based on knowledgebase and path
    const cacheKey = `${activeKB.id}:${fullPath}`;
    
    // Check if we have cached data for this path using the ref, unless forceRefresh is true
    if (!forceRefresh && directoryCacheRef.current[cacheKey]) {
      // Return cached data immediately
      return directoryCacheRef.current[cacheKey];
    }
    
    try {
      // Use kb_id instead of knowledge_base name for better performance
      const response = await fetchWithAuth(`/api/knowledgebase/list?path=${encodeURIComponent(fullPath)}&kb_id=${activeKB.id}&knowledge_base=${encodeURIComponent(activeKB.name)}`);
      
      if (!response.ok) {
        throw new Error(`Failed to fetch directory contents: ${response.status}`);
      }
      
      const data = await response.json();
      
      // Create children array with folders first, then files
      const children = [
        // Convert folders to tree items (now objects with metadata)
        ...(data.folders || []).map(folder => ({
          type: 'folder',
          name: folder.name,
          path: [...folderPath, folder.name],
          isExpanded: true,
          isLoading: false,
          children: [],
          error: ''
        })),
        // Convert files to tree items (now objects with metadata)
        ...(data.files || []).map(file => ({
          type: 'file',
          name: file.name,
          path: [...folderPath, file.name]
        }))
      ];
      
      // Cache the result
      setDirectoryCache(prev => ({
        ...prev,
        [cacheKey]: children
      }));
      
      // Also update the ref immediately
      directoryCacheRef.current = {
        ...directoryCacheRef.current,
        [cacheKey]: children
      };
      
      return children;
    } catch (error) {
      console.error('Error fetching directory contents:', error);
      // Return empty array on error to prevent further issues
      return [];
    }
  }, [activeKB]);
  
  // Recursive function to update the file tree
  const updateFileTree = useCallback((tree, path, updates) => {
    if (JSON.stringify(tree.path) === JSON.stringify(path)) {
      return { ...tree, ...updates };
    }
    
    if (tree.type === 'folder') {
      return {
        ...tree,
        children: tree.children.map(child => updateFileTree(child, path, updates))
      };
    }
    
    return tree;
  }, []);
  
  // Function to fetch folder contents without toggling expansion
  const fetchFolderContents = useCallback(async (folderPath) => {
    // Get the current folder state using a state updater
    setFileTree(prevTree => {
      // Find current folder in the previous tree
      let currentFolder;
      const findCurrentFolder = (tree) => {
        if (JSON.stringify(tree.path) === JSON.stringify(folderPath)) {
          currentFolder = tree;
          return;
        }
        if (tree.children) {
          for (const child of tree.children) {
            findCurrentFolder(child);
          }
        }
      };
      findCurrentFolder(prevTree);
      
      if (!currentFolder) return prevTree;
      
      // Only fetch if children are empty and not already loading
      if (currentFolder.children.length === 0 && !currentFolder.isLoading) {
        // Set loading state immediately
        const loadingTree = updateFileTree(prevTree, folderPath, {
          isLoading: true,
          error: ''
        });
        
        // Fetch children asynchronously
        (async () => {
          try {
            const children = await fetchDirectoryContents(folderPath);
            // Update with fetched children
            setFileTree(prevTree => {
              const updatedTree = updateFileTree(prevTree, folderPath, {
                isLoading: false,
                children: children,
                error: ''
              });
              
              // If the folder is expanded, automatically fetch contents for its subfolders
              if (currentFolder.isExpanded) {
                // For each subfolder that's expanded, fetch its contents
                children.forEach(child => {
                  if (child.type === 'folder' && child.isExpanded) {
                    fetchFolderContents(child.path);
                  }
                });
              }
              
              return updatedTree;
            });
          } catch (err) {
            // Update with error - set children to empty array explicitly
            setFileTree(prevTree => updateFileTree(prevTree, folderPath, {
              isLoading: false,
              children: [],
              error: err.message
            }));
          }
        })();
        
        return loadingTree;
      }
      
      return prevTree;
    });
  }, [updateFileTree, fetchDirectoryContents]);
  
  // Handle folder expand/collapse
  const toggleFolder = useCallback(async (folderPath) => {
    // Get the current folder state using a state updater to avoid direct dependency on fileTree
    setFileTree(prevTree => {
      // Find current folder in the previous tree
      let currentFolder;
      const findCurrentFolder = (tree) => {
        if (JSON.stringify(tree.path) === JSON.stringify(folderPath)) {
          currentFolder = tree;
          return;
        }
        if (tree.children) {
          for (const child of tree.children) {
            findCurrentFolder(child);
          }
        }
      };
      findCurrentFolder(prevTree);
      
      if (!currentFolder) return prevTree;
      
      const newExpandedState = !currentFolder.isExpanded;
      
      // Toggle the expanded state
      const updatedTree = updateFileTree(prevTree, folderPath, {
        isExpanded: newExpandedState
      });
      
      // If expanding, children not yet fetched, and not already loading, fetch them
      if (newExpandedState && currentFolder.children.length === 0 && !currentFolder.isLoading) {
        // Set loading state immediately
        const loadingTree = updateFileTree(updatedTree, folderPath, {
          isLoading: true,
          error: ''
        });
        
          // Fetch children asynchronously
        (async () => {
          try {
            const children = await fetchDirectoryContents(folderPath);
            // Update with fetched children
            setFileTree(prevTree => {
              const updatedTree = updateFileTree(prevTree, folderPath, {
                isLoading: false,
                children: children,
                error: ''
              });
              
              // If the folder is expanded, automatically fetch contents for its subfolders
              // This ensures that when a folder is expanded, all its subfolders are fetched recursively
              if (newExpandedState) {
                // For each subfolder that's expanded, fetch its contents
                children.forEach(child => {
                  if (child.type === 'folder' && child.isExpanded) {
                    fetchFolderContents(child.path);
                  }
                });
              }
              
              return updatedTree;
            });
          } catch (err) {
            // Update with error - set children to empty array explicitly
            setFileTree(prevTree => updateFileTree(prevTree, folderPath, {
              isLoading: false,
              children: [],
              error: err.message
            }));
          }
        })();
        
        return loadingTree;
      }
      
      return updatedTree;
    });
  }, [updateFileTree, fetchDirectoryContents]);
  
  // Recursive component to render the file tree
  const FileTreeItem = ({ item, depth = 0 }) => {
    // Simplified layout - no more flexbox conflicts
    return (
      <div style={{ marginLeft: `${depth * 16}px` }}>
        <div style={{ display: 'block', padding: '4px 8px', borderRadius: '4px', cursor: 'pointer' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {/* Toggle button for folders */}
            {item.type === 'folder' ? (
              <span 
                onClick={() => toggleFolder(item.path)}
                style={{ cursor: 'pointer', display: 'inline-flex', width: '12px', height: '12px', justifyContent: 'center', alignItems: 'center' }}
              >
                {item.isLoading ? (
                  '⏳'
                ) : item.isExpanded ? (
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: 'inline', verticalAlign: 'middle' }}>
                    <polyline points="6 9 12 15 18 9" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                ) : (
                  <svg width="12" height="12" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: 'inline', verticalAlign: 'middle' }}>
                    <polyline points="9 6 15 12 9 18" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  </svg>
                )}
              </span>
            ) : (
              <span style={{ width: '12px', height: '12px' }}></span>
            )}
            
            {/* Icon */}
            <span style={{ display: 'inline-flex', width: '16px', height: '16px' }}>
              {item.type === 'folder' ? (
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: 'inline', verticalAlign: 'middle' }}>
                  <path d="M20 20H4V6L10 3L16 6V20Z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              ) : (
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{ display: 'inline', verticalAlign: 'middle' }}>
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <polyline points="14 2 14 8 20 8" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <line x1="16" y1="13" x2="8" y2="13" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <line x1="16" y1="17" x2="8" y2="17" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <polyline points="10 9 9 9 8 9" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              )}
            </span>
            
            {/* Name (always visible!) */}
            <span style={{
              color: item.type === 'folder' ? '#202124' : '#5F6368',
              fontSize: '13px',
              lineHeight: '16px',
              overflow: 'hidden',
              textOverflow: 'ellipsis',
              whiteSpace: 'nowrap',
              flex: '1',
              minWidth: '50px',
              backgroundColor: 'transparent',
              visibility: 'visible',
              opacity: '1',
              zIndex: '100'
            }}>
              {item.name}
            </span>
            
            {/* Size for files */}
            {item.type === 'file' && (
              <span style={{ color: '#9AA0A6', fontSize: '11px' }}>
                {item.size}
              </span>
            )}
            
            {/* Error message */}
            {item.type === 'folder' && item.error && (
              <span style={{ color: 'red', fontSize: '10px', marginLeft: '8px' }}>
                Error: {item.error}
              </span>
            )}
          </div>
          
          {/* Children for expanded folders */}
          {item.type === 'folder' && item.isExpanded && (
            <div style={{ marginTop: '2px' }}>
              {item.children.map(child => (
                <FileTreeItem key={child.name} item={child} depth={depth + 1} />
              ))}
            </div>
          )}
        </div>
      </div>
    );
  };
  
  // Update activeKB when knowledgebases change and fetch root contents
  useEffect(() => {
    const newActiveKB = knowledgebases.find(kb => kb.is_active);
    setActiveKB(newActiveKB);
    if (newActiveKB) {
      // Reset file tree and fetch root contents immediately
      const resetTree = {
        type: 'folder',
        name: 'Root',
        path: [''],
        isExpanded: true,
        isLoading: true,
        children: [],
        error: ''
      };
      setFileTree(resetTree);
      
      // Fetch root contents
      (async () => {
        try {
            const children = await fetchDirectoryContents(['']);
            setFileTree(prev => ({
              ...prev,
              isLoading: false,
              children: children,
              error: ''
            }));
            
            // Auto-fetch contents for expanded subfolders
            children.forEach(child => {
              if (child.type === 'folder' && child.isExpanded) {
                fetchFolderContents(child.path);
              }
            });
          } catch (err) {
            setFileTree(prev => ({
              ...prev,
              isLoading: false,
              error: err.message
            }));
          }
      })();
    }
  }, [knowledgebases, fetchDirectoryContents, fetchFolderContents]);
  
  // Refresh file browser when triggered from elsewhere (e.g., file upload/delete)
  useEffect(() => {
    if (activeKB) {
      // Function to update a specific path in the file tree
      const updateSpecificPath = async (tree, targetPathParts) => {
        // If we've reached the end of the path parts, this is the folder we need to update
        if (targetPathParts.length === 0) {
          // This is the target folder, fetch its contents
          const currentPath = tree.path.join('/').replace(/^\//, '');
          try {
            const currentCacheKey = `${activeKB.id}:${currentPath}`;
            // Get old children from cache BEFORE fetching fresh data
            const oldChildren = directoryCacheRef.current[currentCacheKey] || [];
            
            // Fetch fresh data for this path
            const children = await fetchDirectoryContents(tree.path, true);
            
            // Clear cache for any deleted folders and their subfolders recursively
            if (activeKB) {
              // Get current child folder names from the new data
              const newFolderNames = new Set(
                children.filter(child => child.type === 'folder').map(child => child.name)
              );
              
              // Compare old cached children with new data to detect deletions
              oldChildren.forEach(child => {
                if (child.type === 'folder' && !newFolderNames.has(child.name)) {
                  // This folder was deleted, clear its cache and all subfolders recursively
                  const childPathParts = [...tree.path, child.name];
                  const childFullPath = childPathParts.join('/').replace(/^\//, '');
                  const deletedCachePrefix = `${activeKB.id}:${childFullPath}`;
                  
                  // Function to recursively clear cache for this folder and all subfolders
                  const clearCacheRecursively = (cache) => {
                    const updatedCache = { ...cache };
                    Object.keys(updatedCache).forEach(key => {
                      // Delete if the key matches the exact folder or starts with the folder path followed by /
                      if (key === deletedCachePrefix || key.startsWith(`${deletedCachePrefix}/`)) {
                        delete updatedCache[key];
                      }
                    });
                    return updatedCache;
                  };
                  
                  // Clear from state
                  setDirectoryCache(prev => clearCacheRecursively(prev));
                  
                  // Clear from ref immediately
                  directoryCacheRef.current = clearCacheRecursively(directoryCacheRef.current);
                }
              });
            }
            
            return {
              ...tree,
              children: children,
              isLoading: false,
              error: ''
            };
          } catch (err) {
            console.error('Error updating target folder:', currentPath, err);
            return {
              ...tree,
              children: [],
              isLoading: false,
              error: err.message
            };
          }
        }
        
        // Find the next folder in the path
        const nextFolderName = targetPathParts[0];
        const folderIndex = tree.children.findIndex(child => 
          child.type === 'folder' && child.name === nextFolderName
        );
        
        if (folderIndex === -1) {
          // Folder not found, this shouldn't happen in a valid path
          return tree;
        }
        
        // Recursively update the child folder with the remaining path parts
        const updatedChild = await updateSpecificPath(
          { ...tree.children[folderIndex], isLoading: true },
          targetPathParts.slice(1)
        );
        
        // Update the tree with the updated child
        const updatedChildren = [...tree.children];
        updatedChildren[folderIndex] = updatedChild;
        
        return {
          ...tree,
          children: updatedChildren,
          isLoading: false
        };
      };
      
      // Function to recursively update the file tree starting from the root
      const updateFileTreeRecursively = async (tree, pathParts, isRoot = false) => {
        // Create the full path for the current folder
        const currentPath = pathParts.join('/').replace(/^\//, '');
        
        // Only refresh if it's the modified folder, not the root folder
        const shouldRefresh = currentPath === fileBrowserLastModifiedPath;
        
        if (shouldRefresh) {
          try {
            const currentPathCacheKey = `${activeKB.id}:${currentPath}`;
            // Get old children from cache BEFORE fetching fresh data
            const oldChildren = directoryCacheRef.current[currentPathCacheKey] || [];
            
            // Fetch fresh data for this path
            const children = await fetchDirectoryContents(pathParts, true);
            
            // Get current child folder names from the new data
            const newFolderNames = new Set(
              children.filter(child => child.type === 'folder').map(child => child.name)
            );
            
            // Clear cache for any folders that were in the old cache but not in the new data (deleted folders)
            oldChildren.forEach(child => {
              if (child.type === 'folder' && !newFolderNames.has(child.name)) {
                // This folder was deleted, clear its cache and all subfolders recursively
                const childPathParts = [...pathParts, child.name];
                const childFullPath = childPathParts.join('/').replace(/^\//, '');
                const deletedCachePrefix = `${activeKB.id}:${childFullPath}`;
                
                // Function to recursively clear cache for this folder and all subfolders
                const clearCacheRecursively = (cache) => {
                  const updatedCache = { ...cache };
                  Object.keys(updatedCache).forEach(key => {
                    // Delete if the key matches the exact folder or starts with the folder path followed by /
                    if (key === deletedCachePrefix || key.startsWith(`${deletedCachePrefix}/`)) {
                      delete updatedCache[key];
                    }
                  });
                  return updatedCache;
                };
                
                // Clear from state
                setDirectoryCache(prev => clearCacheRecursively(prev));
                
                // Clear from ref immediately
                directoryCacheRef.current = clearCacheRecursively(directoryCacheRef.current);
              }
            });
            
            // Merge cached children for subfolders to preserve their contents
            const childrenWithCachedData = children.map(child => {
              if (child.type === 'folder') {
                // Check if we have cached data for this child folder
                const childPathParts = [...pathParts, child.name];
                const childFullPath = childPathParts.join('/').replace(/^\//, '');
                const childCacheKey = `${activeKB.id}:${childFullPath}`;
                
                // If we have cached children for this folder, use them instead of the empty array from API
                if (directoryCacheRef.current[childCacheKey]) {
                  return {
                    ...child,
                    children: directoryCacheRef.current[childCacheKey],
                    isLoading: false
                  };
                }
              }
              return child;
            });
            
            // Update this folder's children with merged data
            tree.children = childrenWithCachedData;
            
            // If this is the modified folder, no need to go deeper
            if (currentPath === fileBrowserLastModifiedPath) {
              return tree;
            }
          } catch (err) {
            console.error('Error updating folder:', currentPath, err);
            tree.error = err.message;
            tree.children = [];
            return tree;
          }
        }
        
        // If this is the modified folder, we've already updated it above
        if (currentPath === fileBrowserLastModifiedPath) {
          return tree;
        }
        
        // Recursively update children
        for (let i = 0; i < tree.children.length; i++) {
          const child = tree.children[i];
          if (child.type === 'folder') {
            // For subfolders, check if their path matches the modified path
            const childPathParts = [...pathParts, child.name];
            const childFullPath = childPathParts.join('/').replace(/^\//, '');
            
            // Only update if this folder is part of the modified path's hierarchy
            if (fileBrowserLastModifiedPath.startsWith(childFullPath)) {
              tree.children[i] = await updateFileTreeRecursively(
                { ...child, isLoading: true }, 
                childPathParts
              );
            }
          }
        }
        
        return tree;
      };
      
      // Start updating based on the modified path
      (async () => {
        try {
          if (fileBrowserLastModifiedPath === '') {
            // Modified path is root, update from root
            const updatedTree = await updateFileTreeRecursively(
              { ...fileTree, isLoading: true }, 
              [''],
              true
            );
            setFileTree(prev => ({
              ...updatedTree,
              isLoading: false
            }));
          } else {
            // Modified path is a subfolder, only update that specific path
            const pathParts = fileBrowserLastModifiedPath.split('/');
            const parentPathParts = pathParts.slice(0, -1); // All parts except last
            const targetPathParts = pathParts.slice(-1); // Only the last part (the modified folder)
            
            if (parentPathParts.length === 0) {
              // Modified folder is directly under root
              const updatedTree = await updateSpecificPath(
                { ...fileTree, isLoading: true },
                pathParts
              );
              setFileTree(prev => ({
                ...updatedTree,
                isLoading: false
              }));
            } else {
              // Modified folder is nested, update its parent first
              const updatedTree = await updateSpecificPath(
                fileTree, // Don't set isLoading on root, only on the specific path
                pathParts
              );
              setFileTree(prev => updatedTree);
            }
          }
        } catch (err) {
          console.error('Error refreshing file tree:', err);
          setFileTree(prev => ({
            ...prev,
            isLoading: false,
            error: err.message
          }));
        }
      })();
    }
  }, [fileBrowserRefreshTrigger, activeKB, fetchDirectoryContents, fileBrowserLastModifiedPath]);
  
  // Use a ref to track the current fileTree state without causing re-renders
  const fileTreeRef = React.useRef(fileTree);
  
  // Update the ref whenever fileTree changes
  useEffect(() => {
    fileTreeRef.current = fileTree;
  }, [fileTree]);
  
  // Auto-fetch contents for expanded folders that have no children
  useEffect(() => {
    if (!activeKB) return;
    
    // Function to recursively check and fetch expanded folders
    const fetchExpandedFolders = async () => {
      const currentTree = fileTreeRef.current;
      if (!currentTree || !currentTree.children) return;
      
      // Inner recursive function that doesn't depend on external state
      const fetchRecursive = async (tree) => {
        if (tree.type === 'folder' && tree.isExpanded) {
          // If this folder has no children and is not loading, fetch its contents
          if (tree.children.length === 0 && !tree.isLoading) {
            await fetchFolderContents(tree.path);
          } 
          // Otherwise, recursively check its children
          else if (tree.children.length > 0) {
            for (const child of tree.children) {
              if (child.type === 'folder') {
                await fetchRecursive(child);
              }
            }
          }
        }
      };
      
      await fetchRecursive(currentTree);
    };
    
    // Start checking from the root
    fetchExpandedFolders();
  }, [activeKB, fetchFolderContents]);
  
  return (
    <div className={`right-sidebar ${isOpen ? 'open' : 'closed'}`}>
      {isOpen ? (
        <div className="right-sidebar-content">
          <div className="right-sidebar-header">
            <h3>Knowledge Base</h3>
            <div className="right-sidebar-actions">
              <button 
                className={`expand-button ${isKnowledgebaseView ? 'active checked' : ''}`}
                onClick={onExpand}
                title={isKnowledgebaseView ? "Close Knowledge Base Browser" : "Open Knowledge Base Browser"}
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 3v18h18M19 9l-7 7-7-7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                <span className="toggle-indicator">
                  {isKnowledgebaseView ? '✓' : ''}
                </span>
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
                </div>
                
                <div className="file-browser-content">
                  {fileTree.isLoading ? (
                    <div className="loading-indicator">Loading...</div>
                  ) : fileTree.error ? (
                    <div className="file-browser-error">{fileTree.error}</div>
                  ) : (
                    <div className="file-browser-items">
                      {/* Render the file tree recursively */}
                      {fileTree.children.map(item => (
                        <FileTreeItem key={item.name} item={item} depth={0} />
                      ))}
                      
                      {fileTree.children.length === 0 && (
                        <div className="empty-folder">
                          <p>Empty folder</p>
                        </div>
                      )}
                    </div>
                  )}
                </div>
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