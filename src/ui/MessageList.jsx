import React, { useEffect, useRef } from 'react';
import MarkdownRenderer from './MarkdownRenderer';
import useChatStore from './store';

const MessageList = ({ messages, isLoading = false, isInitializing = false }) => {
  // Use messages from props which are passed from ChatContainer
  const messagesArray = messages || [];
  const endOfMessagesRef = useRef(null);
  const messageRefs = useRef({});

  // Scroll to the bottom whenever messages change
  useEffect(() => {
    if (endOfMessagesRef.current) {
      endOfMessagesRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  }, [messagesArray]);

  // Ensure the latest assistant message is always visible during streaming
  useEffect(() => {
    const lastMessage = messagesArray[messagesArray.length - 1];
    if (lastMessage && lastMessage.role === 'assistant' && !lastMessage.complete) {
      if (messageRefs.current[messagesArray.length - 1]) {
        messageRefs.current[messagesArray.length - 1].scrollIntoView({ 
          behavior: 'smooth', 
          block: 'nearest' 
        });
      }
    }
  }, [messagesArray]);

  return (
    <div className="message-list" style={{ 
      flex: 1, 
      overflowY: 'auto', 
      padding: '20px', 
      display: 'flex', 
      flexDirection: 'column', 
      gap: '20px', 
      maxHeight: 'calc(100vh - 200px)',
      // Hide scrollbar
      scrollbarWidth: 'none', // Firefox
      msOverflowStyle: 'none', // IE and Edge
    }}>
      {messagesArray.map((message, index) => (
        <div 
          key={index} 
          ref={el => messageRefs.current[index] = el}
          className={`message ${message.role}`}
          style={{ 
            // Card-like container for the message
            backgroundColor: message.role === 'assistant' ? '#FFF8F0' : '#F0FAFC',
            backdropFilter: message.role === 'user' ? 'blur(8px)' : 'none',
            border: message.role === 'user' ? '1px solid rgba(255, 255, 255, 0.8)' : 'none',
            boxShadow: message.role === 'user' ? '0 2px 8px rgba(0, 0, 0, 0.05)' : 'none',
            borderRadius: message.role === 'user' ? '10px' : '18px',
            padding: message.role === 'user' ? '12px' : '12px', 
            marginBottom: '12px',
            maxWidth: '100%',
            alignSelf: message.role === 'user' ? 'flex-start' : 'flex-start', 
            position: message.role === 'assistant' ? 'relative' : 'static',
            marginTop: message.role === 'assistant' ? '16px' : '0',
            display: 'block',
            width: 'fit-content',
            minWidth: '50px',
            boxSizing: 'border-box',
          }}
        >
          <div 
            className={`message-content ${!message.complete ? 'streaming' : ''}`}
            style={{ 
                color: message.role === 'user' ? '#202124' : '#202124',
                wordWrap: 'break-word',
                overflowWrap: 'break-word',
                lineHeight: '1.5',
                fontFamily: '"Roboto", sans-serif',
                // For streaming messages, ensure smooth updates
                transition: message.role === 'assistant' && !message.complete 
                  ? 'padding-bottom 0.3s ease' 
                  : 'none',
                display: 'block',
                width: '100%',
                overflowX: 'auto',
                overflowY: 'hidden',
                boxSizing: 'border-box',
              }}
          >
            {message.role === 'assistant' ? (
              <MarkdownRenderer content={message.content || ''} />
            ) : (
              message.content
            )}
            {message.role === 'assistant' && !message.complete && (
              <div className="typing-indicator" style={{ 
                display: 'flex',
                gap: '4px',
                marginTop: '8px',
                justifyContent: 'flex-start', 
              }}>
                {[1, 2, 3].map(dot => (
                  <div 
                    key={dot} 
                    style={{ 
                      width: '8px',
                      height: '8px',
                      borderRadius: '50%',
                      backgroundColor: '#5F6368',
                      animation: `typing 1.4s infinite both ${dot * 0.2}s`,
                    }}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      ))}
      
      {/* Show a plain assistant message at end if loading and not initializing and not empty */}
      {isLoading && !isInitializing && messagesArray.length > 0 && (
        <div
          className="message assistant"
          style={{ 
            backgroundColor: '#FFF8F0',
            borderRadius: '18px',
            padding: '12px', 
            marginBottom: '12px',
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            maxWidth: '70%',
            alignSelf: 'flex-start',
            width: 'fit-content',
          }}
        >
          <div
            className="spinner"
            style={{ 
              minWidth: 20,
              minHeight: 20,
              width: 20,
              height: 20,
              border: '2px solid #E8EAED',
              borderTop: '2px solid #7bb8ff',
              borderRadius: '50%',
              animation: 'spin 1s linear infinite',
            }}
          />
          <span style={{ fontFamily: '"Roboto", sans-serif' }}>Thinking...</span>
        </div>
      )}
      <div ref={endOfMessagesRef} />
    </div>
  );
};

export default MessageList;