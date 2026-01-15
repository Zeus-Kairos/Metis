import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane } from '@fortawesome/free-solid-svg-icons';
import useChatStore from './store';

const MessageInput = () => {
  const [input, setInput] = useState('');
  const { sendMessage, isLoading, activeThreadId } = useChatStore();

  const handleSend = (e) => {
    e.preventDefault();
    if (input.trim() && !isLoading && activeThreadId) {
      sendMessage(input.trim());
      setInput('');
    }
  };

  const handleKeyDown = (e) => {
    // Send on Enter, shift+Enter for newlines
    if (e.key === 'Enter' && !e.shiftKey) {
      handleSend(e);
    }
  };

  return (
    <>
      <form 
        onSubmit={handleSend}
        style={{
          padding: '20px',
          borderTop: '1px solid #E8EAED',
          backgroundColor: 'white',
        }}
      >
        <div style={{
          position: 'relative',
          maxWidth: '720px',
          margin: '0 auto',
        }}>
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={activeThreadId ? "Type a message..." : "Create a conversation to start messaging"}
            disabled={isLoading || !activeThreadId}
            style={{
              width: '100%',
              minHeight: '48px',
              maxHeight: '120px',
              padding: '12px 48px 12px 12px',
              border: '1px solid #DADCE0',
              borderRadius: '24px',
              fontSize: '16px',
              fontFamily: 'inherit',
              resize: 'none',
              outline: 'none',
              transition: 'border-color 0.2s',
              backgroundColor: activeThreadId ? '#FFFFFF' : '#F8F9FA',
              boxSizing: 'border-box',
              cursor: activeThreadId ? 'text' : 'not-allowed',
            }}
            onFocus={(e) => {
              e.target.borderColor = '#4285F4';
            }}
            onBlur={(e) => {
              e.target.borderColor = '#DADCE0';
            }}
          />
          {/* Send button */}
          <button
            type="submit"
            disabled={!input.trim() || isLoading || !activeThreadId}
            style={{
              position: 'absolute',
              right: '8px',
              top: '50%',
              transform: 'translateY(-50%)',
              background: 'none',
              border: 'none',
              color: input.trim() && !isLoading && activeThreadId ? '#4285F4' : '#C5C5C5',
              cursor: input.trim() && !isLoading && activeThreadId ? 'pointer' : 'not-allowed',
              padding: '8px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              borderRadius: '50%',
              transition: 'background-color 0.2s',
            }}
            onMouseEnter={(e) => {
              if (input.trim() && !isLoading && activeThreadId) {
                e.target.style.backgroundColor = 'rgba(66, 133, 244, 0.1)';
              }
            }}
            onMouseLeave={(e) => {
              e.target.style.backgroundColor = 'transparent';
            }}
          >
            <FontAwesomeIcon 
              icon={faPaperPlane} 
              size="lg" 
              style={{
                transform: 'rotate(45deg)',
                opacity: input.trim() && !isLoading && activeThreadId ? 1 : 0.6,
              }}
            />
          </button>
        </div>
      </form>
    </>
  );
};

export default MessageInput;