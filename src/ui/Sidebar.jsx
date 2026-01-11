import React, { useState, useEffect, useRef } from 'react';
import useChatStore from './store';
import './Sidebar.css';

const Sidebar = ({ isOpen, onToggle, onMenuItemClick }) => {
  const { conversations, createConversation, switchConversation, activeThreadId, renameConversation, removeConversation, username, logout } = useChatStore();
  const [editingId, setEditingId] = useState(null);
  const [editingTitle, setEditingTitle] = useState('');
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [showConfirmDialog, setShowConfirmDialog] = useState(false);
  const [confirmDialogConfig, setConfirmDialogConfig] = useState({
    title: '',
    message: '',
    onConfirm: () => {},
    confirmText: 'Confirm',
    cancelText: 'Cancel'
  });
  const userMenuRef = useRef(null);
  
  // Close menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (userMenuRef.current && !userMenuRef.current.contains(event.target)) {
        setShowUserMenu(false);
      }
    };
    
    if (showUserMenu) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [showUserMenu]);
  
  // Handle menu item clicks
  const handleMenuItemClick = (item) => {
    setShowUserMenu(false);
    
    switch (item) {
      case 'logout':
        logout();
        break;
      default:
        console.log(`Clicked on: ${item}`);
        // Call the onMenuItemClick prop if provided
        if (onMenuItemClick) {
          onMenuItemClick(item);
        }
    }
  };

  const handleTitleUpdate = (threadId, e) => {
    // 确保停止事件传播，即使e可能是undefined
    if (e && e.stopPropagation) {
      e.stopPropagation();
    }
    
    if (editingTitle.trim() !== '') {
      // 调用重命名函数，但确保不触发任何线程切换
      renameConversation(threadId, editingTitle.trim());
    }
    
    // 重置编辑状态
    setEditingId(null);
    setEditingTitle('');
  };

  const handleNewConversation = async () => {
    // Get user_id from store to check authentication before creating conversation
    const { user_id, setError } = useChatStore.getState();
    
    if (!user_id) {
      setError('User not authenticated. Please refresh the page and try again.');
      return;
    }
    
    await createConversation();
  };
  
  const handleDeleteConversation = (threadId, e) => {
    e.stopPropagation(); // Prevent switching conversation when clicking delete
    
    // Show confirm dialog for conversation deletion
    setConfirmDialogConfig({
      title: 'Delete Conversation',
      message: 'Are you sure you want to delete this conversation?',
      onConfirm: () => removeConversation(threadId),
      confirmText: 'Delete',
      cancelText: 'Cancel'
    });
    setShowConfirmDialog(true);
  };

  const formatDate = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleString(undefined, { 
      month: 'short', 
      day: 'numeric', 
      hour: '2-digit', 
      minute: '2-digit',
      hour12: true
    });
  };

  const getPreview = (messages) => {
    // Find the last message from the user
    const lastUserMessage = [...messages].reverse().find(msg => msg.role === 'user');
    
    if (lastUserMessage) {
      // Truncate to one line and limit length
      const oneLineContent = lastUserMessage.content.replace(/\n/g, ' ').trim();
      return oneLineContent.length > 40 
        ? oneLineContent.substring(0, 40) + '...' 
        : oneLineContent;
    }
    return 'New conversation';
  };

  return (
    <>
      <div className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      {/* User Info Section */}
      {username && (
        <div className="sidebar-user-info" ref={userMenuRef}>
          {/* User icon and name - Hide when sidebar is closed, positioned left */}
          <div className="user-menu-container" onClick={() => setShowUserMenu(!showUserMenu)}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="user-icon">
              <path d="M12 4.354a4 4 0 1 1 0 5.292M15 21H3v-1a6 6 0 0 1 12 0v1zm0 0h6v-1a6 6 0 0 0-9-5.197M13 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            <div className="user-name">{username}</div>
          </div>
          
          {/* Sidebar Toggle Button - Always visible, positioned right */}
          <button 
            onClick={onToggle} 
            className="sidebar-toggle-button"
            title={isOpen ? 'Close Sidebar' : 'Open Sidebar'}
          >
            {isOpen ? (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 18L9 12L15 6" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            ) : (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="1" fill="#5F6368"/>
                <circle cx="16" cy="12" r="1" fill="#5F6368"/>
                <circle cx="8" cy="12" r="1" fill="#5F6368"/>
              </svg>
            )}
          </button>
          
          {showUserMenu && (
            <div className="user-menu-popup">
              <div className="user-menu-item" onClick={() => handleMenuItemClick('user-profile')}>User Profile</div>
              <div className="user-menu-item" onClick={() => handleMenuItemClick('api-configuration')}>API Configuration</div>
              <div className="user-menu-divider"></div>
              <div className="user-menu-item logout-item" onClick={() => handleMenuItemClick('logout')}>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="logout-icon">
                  <path d="M9 21H5C3.89543 21 3 20.1046 3 19V5C3 3.89543 3.89543 3 5 3H9" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M16 17L21 12L16 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <path d="M21 12H9" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                <span>Logout</span>
              </div>
            </div>
          )}
        </div>
      )}
      
      {/* Header - Moved below user info */}
      <div className="sidebar-header">
        <h2>Conversations</h2>
        
        {/* Add Plan section moved next to header */}
        <div className="add-plan-section">
          <button
            onClick={handleNewConversation}
            className="add-plan-icon-btn"
            aria-label="Add new plan"
            title="Add new plan"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 5V19M5 12H19" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
          <span className="add-plan-text">Add</span>
        </div>
      </div>

      {/* Conversations List */}
      <div className="conversations-list">
        {conversations && Object.values(conversations).length > 0 && Object.values(conversations).filter(c => c.threadId !== activeThreadId).length > 0 && (
          Object.values(conversations)
            .filter(conversation => conversation.threadId !== activeThreadId) // Filter out active conversation
            .sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt))
            .map((conversation) => {
              // No need for isActive check as we've filtered out active conversation
              return (
                <div
                  key={conversation.threadId}
                  onClick={() => {
                    // 只有当不是编辑状态时才允许切换对话
                    if (editingId !== conversation.threadId) {
                      switchConversation(conversation.threadId);
                    }
                  }}
                  className="conversation-item"
                >
                  <div className="conversation-details">
                    <div className="conversation-header">
                      {editingId === conversation.threadId ? (
                        <input
                          type="text"
                          value={editingTitle}
                          onChange={(e) => {
                            e.stopPropagation();
                            setEditingTitle(e.target.value);
                          }}
                          onBlur={(e) => {
                            e.stopPropagation();
                            handleTitleUpdate(conversation.threadId, e);
                          }}
                          onKeyPress={(e) => {
                            e.stopPropagation();
                            if (e.key === 'Enter') {
                              handleTitleUpdate(conversation.threadId, e);
                            } else if (e.key === 'Escape') {
                              setEditingId(null);
                              setEditingTitle('');
                            }
                          }}
                          autoFocus
                          className="conversation-title-input"
                        />
                      ) : (
                        <div className="conversation-title-container">
                          <div className="conversation-title">
                            {conversation.title || 'Untitled Conversation'}
                          </div>
                          <button
                            className="edit-conversation-btn"
                            onClick={(e) => {
                              e.stopPropagation();
                              setEditingId(conversation.threadId);
                              setEditingTitle(conversation.title || '');
                            }}
                            aria-label="Edit conversation title"
                            title="Edit conversation title"
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                            </svg>
                          </button>
                        </div>
                      )}
                      {/* Delete Button */}
                      {/* Removed check that hid delete button when only one conversation remained */}
                      <button
                        className="delete-conversation-btn"
                        onClick={(e) => handleDeleteConversation(conversation.threadId, e)}
                        aria-label="Delete conversation"
                        title="Delete conversation"
                      >
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                          <path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                        </svg>
                      </button>
                    </div>
                    {/* Move date below the title */}
                    <div className="conversation-date">
                      {formatDate(conversation.updatedAt)}
                    </div>
                    <div className="conversation-preview">
                      {getPreview(conversation.messages)}
                    </div>
                  </div>
                  <div className="conversation-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="#5F6368" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </div>
                </div>
              );
            })
        )}
      </div>
    </div>
    
    {/* Confirm Dialog */}
    {showConfirmDialog && (
      <div className="kb-dialog-overlay">
        <div className="kb-dialog">
          <div className="dialog-header">
            <h3>{confirmDialogConfig.title}</h3>
            <button 
              className="dialog-close"
              onClick={() => setShowConfirmDialog(false)}
            >
              ×
            </button>
          </div>
          <div className="dialog-body">
            <p>{confirmDialogConfig.message}</p>
          </div>
          <div className="dialog-footer">
            <button 
              onClick={() => setShowConfirmDialog(false)}
            >
              {confirmDialogConfig.cancelText}
            </button>
            <button 
              onClick={() => {
                confirmDialogConfig.onConfirm();
                setShowConfirmDialog(false);
              }}
              className="dialog-primary"
            >
              {confirmDialogConfig.confirmText}
            </button>
          </div>
        </div>
      </div>
    )}
    </>
  );
};

export default Sidebar;