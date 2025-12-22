import React, { useState, useEffect, useRef } from 'react';
import useChatStore from './store';

/**
 * VoiceInput hook that connects to backend STT service via WebSocket
 * Uses RealtimeSTT library on the backend for transcription
 */
export const useVoiceInput = ({ onTranscription, onFinalTranscription, disabled = false, language = 'en' }) => {
  const [isListening, setIsListening] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [error, setError] = useState(null);
  const wsRef = useRef(null);
  const { user_id } = useChatStore();

  const connectWebSocket = () => {
    if (!user_id || disabled) return null;

    try {
      // Determine WebSocket URL
      const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
      const wsUrl = `${protocol}//${window.location.host}/stt/stream`;
      
      const ws = new WebSocket(wsUrl);
      console.log(`WebSocket connection to ${wsUrl} created successfully`);
      
      ws.onopen = () => {
        // Send initialization message
        ws.send(JSON.stringify({
          user_id: user_id,
          config: {
            input_device_index: 1,
            language: language,
          }
        }));
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          
          switch (data.type) {
            case 'status':
              if (data.status === 'listening') {
                setIsListening(true);
                setError(null);
              } else if (data.status === 'stopped') {
                setIsListening(false);
              }
              break;
              
            case 'transcription_update':
              if (data.text) {
                setTranscript(data.text);
                if (onTranscription) {
                  onTranscription(data.text);
                }
              }
              break;
              
            case 'transcription_stabilized':
              if (data.text) {
                setTranscript(data.text);
                if (onFinalTranscription) {
                  onFinalTranscription(data.text);
                }
              }
              break;
              
            case 'vad_start':
              // Voice activity detected - start showing visual feedback
              break;
              
            case 'vad_stop':
              // Voice activity stopped
              break;
              
            case 'wakeword_detected':
              // Wake word detected
              break;
              
            case 'error':
              setError(data.message || 'STT error occurred');
              setIsListening(false);
              break;
          }
        } catch (err) {
          console.error('Error parsing WebSocket message:', err);
        }
      };

      ws.onerror = (err) => {
        console.error('WebSocket error:', err);
        setError('Connection error. Please check if STT service is available.');
        setIsListening(false);
      };

      ws.onclose = () => {
        setIsListening(false);
        wsRef.current = null;
      };

      return ws;
    } catch (err) {
      console.error('Error creating WebSocket:', err);
      setError('Failed to connect to STT service.');
      return null;
    }
  };

  const startListening = () => {
    if (disabled || !user_id || isListening) return;
    
    try { 
      setError(null);
      const ws = connectWebSocket();
      if (ws) {
        wsRef.current = ws;
      } else {
        setError('Failed to start voice input. Please try again.');
      }
    } catch (err) {
      console.error('Error starting recognition:', err);
      setError('Failed to start voice input. Please try again.');
    }
  };

  const stopListening = () => {
    if (wsRef.current && isListening) {
      try {
        wsRef.current.send(JSON.stringify({ command: 'stop' }));
      } catch (err) {
        console.error('Error stopping recognition:', err);
      }
      setIsListening(false);
    }
  };

  const toggleListening = () => {
    if (isListening) {
      stopListening();
    } else {
      startListening();
    }
  };

  const getFinalText = () => {
    if (wsRef.current && isListening) {
      try {
        wsRef.current.send(JSON.stringify({ command: 'get_text' }));
      } catch (err) {
        console.error('Error getting final text:', err);
      }
    }
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (wsRef.current) {
        wsRef.current.close();
        wsRef.current = null;
      }
    };
  }, []);

  return {
    isListening,
    transcript,
    error,
    startListening,
    stopListening,
    toggleListening,
    getFinalText,
    isSupported: true // WebSocket is supported in all modern browsers
  };
};

