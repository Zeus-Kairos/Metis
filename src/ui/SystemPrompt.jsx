import React from 'react';
import useChatStore from './store';

const SystemPrompt = () => {
  const { systemPrompt, systemPromptVisible } = useChatStore();

  if (!systemPromptVisible || !systemPrompt) {
    return null;
  }

  return (
    <div 
      className="system-prompt"
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        backgroundColor: '#4CAF50',
        color: 'white',
        padding: '12px 24px',
        boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
        zIndex: 1000,
        fontSize: '16px',
        fontWeight: '500',
        textAlign: 'center',
        animation: 'slideDown 0.3s ease-out'
      }}
    >
      {systemPrompt}
    </div>
  );
};

export default SystemPrompt;