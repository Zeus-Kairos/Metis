import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPaperPlane, faMicrophone, faMicrophoneSlash } from '@fortawesome/free-solid-svg-icons';
import useChatStore from './store';
import { useVoiceInput } from './VoiceInput';
import STTSettings from './STTSettings';

const MessageInput = () => {
  const [input, setInput] = useState('');
  const [showSTTSettings, setShowSTTSettings] = useState(false);
  const { sendMessage, isLoading, activeThreadId } = useChatStore();
  const user_id = useChatStore(state => state.user_id);
  
  // Voice input integration
  const {
    isListening,
    transcript,
    error: voiceError,
    toggleListening,
    isSupported: voiceSupported
  } = useVoiceInput({
    onTranscription: (text) => {
      setInput(text);
    },
    onFinalTranscription: (text) => {
      setInput(text);
    },
    disabled: isLoading || !activeThreadId || !user_id,
    language: 'en'
  });
  
  // Update input when transcript changes
  React.useEffect(() => {
    if (transcript) {
      setInput(transcript);
    }
  }, [transcript]);

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
            placeholder={activeThreadId ? (isListening ? "Listening..." : "Type a message...") : "Create a conversation to start messaging"}
            disabled={isLoading || !activeThreadId || isListening}
            style={{
              width: '100%',
              minHeight: '48px',
              maxHeight: '120px',
              padding: '12px 48px 12px 44px',
              border: isListening ? '2px solid #4285F4' : '1px solid #DADCE0',
              borderRadius: '24px',
              fontSize: '16px',
              fontFamily: 'inherit',
              resize: 'none',
              outline: 'none',
              transition: 'border-color 0.2s',
              backgroundColor: activeThreadId ? (isListening ? '#E8F0FE' : '#FFFFFF') : '#F8F9FA',
              boxSizing: 'border-box',
              cursor: activeThreadId && !isListening ? 'text' : 'not-allowed',
            }}
            onFocus={(e) => {
              if (!isListening) {
                e.target.borderColor = '#4285F4';
              }
            }}
            onBlur={(e) => {
              if (!isListening) {
                e.target.borderColor = '#DADCE0';
              }
            }}
          />
          {/* Buttons container for vertical layout */}
          <div style={{
            position: 'absolute',
            left: '6px',
            top: '50%',
            transform: 'translateY(-50%)',
            display: 'flex',
            flexDirection: 'column',
            gap: '2px',
            zIndex: 1,
          }}>
            {/* Voice input button */}
            {voiceSupported && (
              <button
                type="button"
                onClick={toggleListening}
                disabled={isLoading || !activeThreadId || !user_id}
                style={{
                  background: isListening ? '#EA4335' : 'none',
                  border: 'none',
                  color: isListening ? 'white' : (activeThreadId && user_id ? '#4285F4' : '#C5C5C5'),
                  cursor: activeThreadId && user_id ? 'pointer' : 'not-allowed',
                  padding: '4px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  borderRadius: '50%',
                  transition: 'background-color 0.2s',
                  minWidth: '24px',
                  minHeight: '24px',
                }}
                onMouseEnter={(e) => {
                  if (activeThreadId && user_id) {
                    e.target.style.backgroundColor = isListening ? '#D32F2F' : 'rgba(66, 133, 244, 0.1)';
                  }
                }}
                onMouseLeave={(e) => {
                  e.target.style.backgroundColor = isListening ? '#EA4335' : 'transparent';
                }}
                title={isListening ? 'Stop voice input' : 'Start voice input (uses server microphone)'}
              >
                <FontAwesomeIcon 
                  icon={isListening ? faMicrophoneSlash : faMicrophone}
                  size="sm"
                />
              </button>
            )}
            
            {/* STT Settings button */}
            <button
              type="button"
              onClick={() => setShowSTTSettings(!showSTTSettings)}
              disabled={isLoading}
              style={{
                background: 'none',
                border: 'none',
                color: activeThreadId && user_id ? '#4285F4' : '#C5C5C5',
                cursor: activeThreadId && user_id ? 'pointer' : 'not-allowed',
                padding: '4px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                borderRadius: '50%',
                transition: 'background-color 0.2s',
                minWidth: '24px',
                minHeight: '24px',
              }}
              title="STT Settings"
              onMouseEnter={(e) => {
                if (activeThreadId && user_id) {
                  e.target.style.backgroundColor = 'rgba(66, 133, 244, 0.1)';
                }
              }}
              onMouseLeave={(e) => {
                e.target.style.backgroundColor = 'transparent';
              }}
            >
              ⚙️
            </button>
          </div>
          {/* Send button */}
          <button
            type="submit"
            disabled={!input.trim() || isLoading || !activeThreadId || isListening}
            style={{
              position: 'absolute',
              right: '8px',
              top: '50%',
              transform: 'translateY(-50%)',
              background: 'none',
              border: 'none',
              color: input.trim() && !isLoading && activeThreadId && !isListening ? '#4285F4' : '#C5C5C5',
              cursor: input.trim() && !isLoading && activeThreadId && !isListening ? 'pointer' : 'not-allowed',
              padding: '8px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              borderRadius: '50%',
              transition: 'background-color 0.2s',
            }}
            onMouseEnter={(e) => {
              if (input.trim() && !isLoading && activeThreadId && !isListening) {
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
                opacity: input.trim() && !isLoading && activeThreadId && !isListening ? 1 : 0.6,
              }}
            />
          </button>
        </div>
        {/* Voice error message */}
        {voiceError && (
          <div style={{
            maxWidth: '720px',
            margin: '8px auto 0',
            padding: '8px 12px',
            backgroundColor: '#FCE8E6',
            color: '#D93025',
            borderRadius: '8px',
            fontSize: '14px',
          }}>
            {voiceError}
          </div>
        )}
      </form>
      
      {/* STTSettings Modal */}
      <STTSettings 
        isVisible={showSTTSettings} 
        onClose={() => setShowSTTSettings(false)} 
      />
    </>
  );
};

export default MessageInput;