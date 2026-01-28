import React, { useEffect, useRef, useMemo } from 'react';
import MarkdownRenderer from './MarkdownRenderer';

const MessageList = ({ messages, isLoading = false, isInitializing = false }) => {
  // Use messages from props which are passed from ChatContainer
  const messagesArray = useMemo(() => messages || [], [messages]);
  const endOfMessagesRef = useRef(null);
  const messageRefs = useRef({});
  // Refs for display content divs to enable auto-scrolling
  const displayRefs = useRef({});
  // State to track which display messages are expanded
  const [expandedDisplays, setExpandedDisplays] = React.useState({});
  
  // Toggle display expansion for a specific message
  const toggleDisplay = (messageIndex) => {
    setExpandedDisplays(prev => ({
      ...prev,
      [messageIndex]: !prev[messageIndex]
    }));
  };
  
  // Auto-scroll display content to bottom when updated, especially during streaming
  React.useEffect(() => {
    if (messagesArray.length > 0) {
      const lastMessage = messagesArray[messagesArray.length - 1];
      const lastIndex = messagesArray.length - 1;
      
      // Only auto-scroll if it's an assistant message with display content
      if (lastMessage.role === 'assistant' && lastMessage.display && typeof lastMessage.display === 'string') {
        const displayVisible = expandedDisplays[lastIndex] || !lastMessage.content.trim();
        
        if (displayVisible) {
          const displayEl = displayRefs.current[lastIndex];
          if (displayEl) {
            // Scroll to the bottom of the display content
            displayEl.scrollTop = displayEl.scrollHeight;
          }
        }
      }
    }
  }, [messagesArray, expandedDisplays]);

  // Simplified scrolling logic: always scroll to bottom when messages change
  useEffect(() => {
    if (endOfMessagesRef.current) {
      endOfMessagesRef.current.scrollIntoView({ 
        behavior: 'auto', // Use immediate scrolling instead of smooth to prevent conflicts
        block: 'end' 
      });
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
            backgroundColor: message.role === 'assistant' ? 'transparent' : '#64B5F6',
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
            // Prevent long lines from overflowing
            wordBreak: 'break-all',         
          }}
        >
          <div 
            className={`message-content ${!message.complete ? 'streaming' : ''}`}
            style={{ 
                color: message.role === 'user' ? 'white' : '#000000',
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
            {/* Display 'display' data with expand/collapse functionality */}
            {message.role === 'assistant' && message.display && typeof message.display === 'string' && message.display.trim() && (
              <>
                {/* Expand/Collapse button - only show when there's both display data and response content */}
                {message.content.trim() && (
                  <button
                    onClick={() => toggleDisplay(index)}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: '#606266',
                      fontSize: '0.75em',
                      cursor: 'pointer',
                      padding: '4px 8px',
                      marginBottom: '4px',
                      borderRadius: '4px',
                      hover: {
                        backgroundColor: '#f0f0f0'
                      }
                    }}
                  >
                    {expandedDisplays[index] ? '▼ Hide details' : '▶ Show details'}
                  </button>
                )}
                
                {/* Show display data if there's no response or it's expanded */}
                {(expandedDisplays[index] || !message.content.trim()) && (
                  <div 
                    className="display-content"
                    ref={el => displayRefs.current[index] = el}
                    style={{ 
                      fontSize: '0.8em',
                      color: '#606266',
                      marginBottom: '8px',
                      padding: '8px',
                      border: '1px solid #e0e0e0',
                      lineHeight: '1.4',
                      fontFamily: '"Roboto", sans-serif',
                      whiteSpace: 'pre-wrap',
                      maxHeight: '300px', // Increased vertical space
                      overflowY: 'auto',
                      borderRadius: '4px',
                      backgroundColor: '#F8F8F8', // Distinct background color for sliding window
                    }}
                  >
                    {message.display}
                  </div>
                )}
              </>
            )}
            
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
            backgroundColor: 'transparent',
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
          <span style={{ fontFamily: '"Roboto", sans-serif', color: '#000000' }}>Thinking...</span>
        </div>
      )}
      <div ref={endOfMessagesRef} />
    </div>
  );
};

export default MessageList;