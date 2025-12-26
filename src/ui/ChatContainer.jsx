import React, { useState, useEffect } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import useChatStore from './store';
import Sidebar from './Sidebar';
import RightSidebar from './RightSidebar';
import SystemPrompt from './SystemPrompt';
import KnowledgebaseBrowser from './KnowledgebaseBrowser';
import ApiConfiguration from './ApiConfiguration';
import './ChatContainer.css';


const ChatContainer = () => {
  const { 
    isLoading, 
    error, 
    user_id,
    initializeApp,
    createConversation, 
    conversations,
    activeThreadId,
    setError,
    renameConversation
  } = useChatStore();
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [rightSidebarOpen, setRightSidebarOpen] = useState(true);
  const [isEditingTitle, setIsEditingTitle] = useState(false);
  const [editingTitle, setEditingTitle] = useState('');
  const [initialized, setInitialized] = useState(false);
  const [view, setView] = useState('chat'); // 'chat' or 'knowledgebase'
  const [showApiConfig, setShowApiConfig] = useState(false);
  // Fix: Access messages through active conversation, not as a function
  const currentMessages = conversations[activeThreadId]?.messages || [];
  const currentConversation = conversations[activeThreadId];
  const isInitializing = isLoading && !user_id;

  // Initialize the app only once
  useEffect(() => {
    if (initialized) return;
    
    const init = async () => {
      await initializeApp()
      
      setInitialized(true);
    }
    
    // Call the init function
    init();
  }, [initializeApp, initialized]);

  const handleNewChat = async () => {
    // If user_id is null, show error and don't attempt to create conversation
    if (!user_id) {
      setError('User not authenticated. Please refresh the page and try again.');
      return;
    }
    
    await createConversation();
  };

  const handleTitleUpdate = () => {
    if (activeThreadId && editingTitle.trim() !== '') {
      renameConversation(activeThreadId, editingTitle.trim());
    }
    setIsEditingTitle(false);
    setEditingTitle('');
  };

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="chat-container">
      {/* Left Sidebar */}
      <Sidebar 
        isOpen={sidebarOpen} 
        onToggle={toggleSidebar}
        activeThreadId={activeThreadId}
        conversations={conversations}
        onMenuItemClick={(item) => {
          if (item === 'api-configuration') {
            setShowApiConfig(true);
          }
        }}
      />
      
      {/* Main Chat Area */}
      <div className={`main-chat-area ${sidebarOpen ? 'sidebar-open' : 'sidebar-closed'} ${rightSidebarOpen ? 'right-sidebar-open' : 'right-sidebar-closed'}`}>
        {/* Header */}
        <header className="chat-header">
          <div className="title-container">
            <div className="chat-title-container">
              {isEditingTitle ? (
                <input
                  type="text"
                  value={editingTitle}
                  onChange={(e) => setEditingTitle(e.target.value)}
                  onBlur={handleTitleUpdate}
                  onKeyPress={(e) => {
                    if (e.key === 'Enter') {
                      handleTitleUpdate();
                    } else if (e.key === 'Escape') {
                      setIsEditingTitle(false);
                      setEditingTitle(currentConversation?.title || '');
                    }
                  }}
                  autoFocus
                  className="chat-title-input"
                />
              ) : (
                <>
                  <h1 className="chat-title">{view === 'chat' ? (currentConversation?.title || 'Metis') : 'Knowledge Base'}</h1>
                  {view === 'chat' && activeThreadId && (
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setIsEditingTitle(true);
                        setEditingTitle(currentConversation?.title || '');
                      }}
                      className="edit-title-btn"
                      title="Edit conversation title"
                    >
                      ✏️
                    </button>
                  )}
                </>
              )}
            </div>
            <div className="view-toggle">
              <button 
                className={`toggle-btn ${view === 'chat' ? 'active' : ''}`}
                onClick={() => setView('chat')}
                title="Chat View"
              >
                💬
              </button>
              <button 
                className={`toggle-btn ${view === 'knowledgebase' ? 'active' : ''}`}
                onClick={() => setView('knowledgebase')}
                title="Knowledge Base"
              >
                📖
              </button>
            </div>
          </div>
        </header>

        {/* Main Content */}
        <main className="chat-main">
          {isInitializing ? (
            <div className="loading-state">
              <div className="spinner-container">
                <div className="spinner"></div>
                <span>Initializing application...</span>
              </div>
            </div>
          ) : error ? (
            <div className="error-state">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="#EA4335" strokeWidth="2"/>
                <line x1="15" y1="9" x2="9" y2="15" stroke="#EA4335" strokeWidth="2" strokeLinecap="round"/>
                <line x1="9" y1="9" x2="15" y2="15" stroke="#EA4335" strokeWidth="2" strokeLinecap="round"/>
              </svg>
              <h3>Error loading application</h3>
              <p>{error}</p>
              <button onClick={initializeApp} className="retry-button">
                Retry
              </button>
            </div>
          ) : view === 'knowledgebase' ? (
            <KnowledgebaseBrowser />
          ) : !activeThreadId ? (
            <div className="no-threads-state">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2" stroke="#BDC1C6" strokeWidth="2"/>
                <path d="M9 18H15" stroke="#BDC1C6" strokeWidth="2" strokeLinecap="round"/>
                <path d="M12 15V18" stroke="#BDC1C6" strokeWidth="2" strokeLinecap="round"/>
                <path d="M9 9H15" stroke="#BDC1C6" strokeWidth="2" strokeLinecap="round"/>
                <path d="M9 6H15" stroke="#BDC1C6" strokeWidth="2" strokeLinecap="round"/>
              </svg>
              <h3>No conversations yet</h3>
              <p>You don't have any conversations. Create a new one to get started.</p>
              <button onClick={handleNewChat} className="create-chat-button">
                Create New Chat
              </button>
            </div>
          ) : currentMessages.length === 0 ? (
            <div className="empty-state">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="#BDC1C6" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
              <h3>Start a conversation</h3>
              <p>Begin asking questions about your knowledge base</p>
            </div>
          ) : (
            <MessageList 
              messages={currentMessages} 
              isLoading={isLoading} 
              isInitializing={isInitializing}
            />
          )}
        </main>
        {/* Input Area */}
        {view === 'chat' && <MessageInput />}
      </div>
      
      {/* Right Sidebar */}
      <RightSidebar 
        isOpen={rightSidebarOpen} 
        onToggle={() => setRightSidebarOpen(!rightSidebarOpen)} 
        isKnowledgebaseView={view === 'knowledgebase'}
        onExpand={() => setView(view === 'knowledgebase' ? 'chat' : 'knowledgebase')}
      />
      
      {/* API Configuration Modal */}
      <ApiConfiguration
        isOpen={showApiConfig}
        onClose={() => setShowApiConfig(false)}
      />
    </div>
  );
};

export default ChatContainer;