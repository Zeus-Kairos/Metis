import ChatContainer from './ChatContainer';
import './index.css';
import { useEffect, useState } from 'react';
import SystemPrompt from './SystemPrompt';
import useChatStore from './store';
import Login from './Login';

function App() {
  const { initializeApp, isLoading, error, isInitializing, user_id, authChecked } = useChatStore();

  // Initialize the app when it loads
  useEffect(() => {
    const init = async () => {
      await initializeApp();
    };
    
    init();
  }, [initializeApp]);

  // Show loading while auth is being checked
  if (!authChecked) {
    return <div className="loading">Loading...</div>;
  }

  // Show login if not authenticated
  if (!user_id) {
    return <Login />;
  }

  // Show main app if authenticated
  return (
    <div>
      <SystemPrompt />
      <ChatContainer />
    </div>
  );
}

export default App