import { create } from 'zustand';

// Helper function to get token from localStorage
const getToken = () => {
  return localStorage.getItem('token');
};

// Helper function to add auth header to fetch requests
export const fetchWithAuth = async (url, options = {}) => {
  const token = getToken();
  let headers = {
    ...options.headers
  };

  // Don't set Content-Type if body is FormData - browser handles it automatically
  if (!options.body || !(options.body instanceof FormData)) {
    headers['Content-Type'] = headers['Content-Type'] || 'application/json';
  }

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  // Use direct backend URL instead of proxy
  const fullUrl = url.startsWith('http') ? url : `http://localhost:8000${url}`;
  
  console.debug('Making API request to:', fullUrl);

  try {
    const response = await fetch(fullUrl, {
      ...options,
      headers
    });

    // Check if response is 401 Unauthorized
    if (response.status === 401) {
      // Token is invalid or expired, remove it and log out
      localStorage.removeItem('token');
      
      // Get the store instance and call logout to reset state
      const store = useChatStore.getState();
      if (store.logout) {
        store.logout();
      }
    }

    return response;
  } catch (fetchError) {
    console.error('Fetch failed for URL:', fullUrl, 'Error:', fetchError);
    throw fetchError;
  }
};

const useChatStore = create((set, get) => {
  // Helper function to update active thread
  const updateActiveThread = (updates) => {
    const { activeThreadId, conversations } = get();
    set((state) => ({
      conversations: {
        ...state.conversations,
        [activeThreadId]: {
          ...conversations[activeThreadId],
          ...updates,
          updatedAt: new Date().toISOString()
        }
      }
    }));
  };

  return {
    // Initial state
    user_id: null,
    username: null,
    activeThreadId: null,
    conversations: {},
    knowledgebases: [],
    isLoading: false,
    isInitializing: false,
    authChecked: false,
    error: null,
    showErrorModal: false,
    fileBrowserRefreshTrigger: 0,

    // Initialize app by getting active user and threads
    initializeApp: async () => {
      try {
        // Check if we're already initializing or initialized
        const currentState = get();
        if (currentState.isInitializing || (currentState.user_id && currentState.authChecked)) {
          // Already initializing or initialized, no need to proceed
          return;
        }
        
        set({ isLoading: true, error: null, isInitializing: true });
        
        // Check if we have a token
      const token = getToken();
      
      if (!token) {
        // No token found, set user_id to null and return
        set({ 
          isLoading: false, 
          isInitializing: false,
          authChecked: true,
          user_id: null,
          activeThreadId: null,
          conversations: {}
        });
        return;
      }
      
      // Step 1: Get active user from /api/users/me endpoint
      const userResponse = await fetchWithAuth('/api/users/me');
      
      if (!userResponse.ok) {
        if (userResponse.status === 401) {
          // Token is invalid or expired, remove it
          localStorage.removeItem('token');
          set({ 
            isLoading: false, 
            isInitializing: false,
            authChecked: true,
            user_id: null,
            activeThreadId: null,
            conversations: {}
          });
        } else {
          throw new Error(`Failed to get active user: ${userResponse.status}`);
        }
        return;
      }
        
        // Try to parse response as JSON, handle case where HTML is returned
        const contentType = userResponse.headers.get('content-type');
        
        if (!contentType || !contentType.includes('application/json')) {
          const textContent = await userResponse.text();
          console.warn('Received non-JSON response from /api/users/me:', textContent.substring(0, 100) + '...');
          throw new Error('Received invalid response format from server');
        }
        
        const userData = await userResponse.json();
        const userId = userData.id; // Using 'id' instead of 'user_id' from response
        const username = userData.username;
        
        if (!userId) {
          throw new Error('Invalid user data received from server');
        }
        
        // Update user_id and username in state
        set({ user_id: userId, username: username });
        
        // Step 2: Get all knowledgebases for the user
        const knowledgebasesResponse = await fetchWithAuth('/api/knowledgebase');
        
        if (!knowledgebasesResponse.ok) {
          throw new Error(`Failed to get knowledgebases: ${knowledgebasesResponse.status}`);
        }
        
        const knowledgebasesData = await knowledgebasesResponse.json();
        let knowledgebases = knowledgebasesData.knowledgebases || [];
        
        // Create default knowledgebase if none exist
        if (knowledgebases.length === 0) {
          const createDefaultKBResponse = await fetchWithAuth('/api/knowledgebase', {
            method: 'POST',
            body: JSON.stringify({
              name: 'default',
              description: 'Default knowledgebase',
              navigation: {}
            })
          });
          
          if (createDefaultKBResponse.ok) {
            // Fetch knowledgebases again to get the newly created one
            const updatedKBsResponse = await fetchWithAuth('/api/knowledgebase');
            if (updatedKBsResponse.ok) {
              const updatedKBsData = await updatedKBsResponse.json();
              knowledgebases = updatedKBsData.knowledgebases || [];
            }
          }
        }
        
        // Step 3: Get all threads for the user
        const threadsResponse = await fetchWithAuth(`/api/threads/${userId}`);
        
        if (!threadsResponse.ok) {
          throw new Error(`Failed to get threads: ${threadsResponse.status}`);
        }
        
        // Check content type for threads response too
        const threadsContentType = threadsResponse.headers.get('content-type');
        
        if (!threadsContentType || !threadsContentType.includes('application/json')) {
          const textContent = await threadsResponse.text();
          console.warn('Received non-JSON response from /api/threads:', textContent.substring(0, 100) + '...');
          throw new Error('Received invalid response format from server for threads');
        }
        
        const threadsData = await threadsResponse.json();
        const threads = threadsData.threads || [];
        
        // Create conversations object from threads
        const conversations = {};
        let activeThreadId = null;
        
        // Process threads if any exist
        if (threads.length > 0) {
          threads.forEach((thread) => {
            conversations[thread.thread_id || thread.id] = {
              threadId: thread.thread_id || thread.id,
              title: thread.title,
              messages: [],
              createdAt: thread.created_at || new Date().toISOString(),
              updatedAt: thread.updated_at || new Date().toISOString()
            };
          });
          
          // Step 3: Set active thread with priority to thread where is_active is true
          // If no thread has is_active=true, use the first thread
          const activeThread = threads.find(thread => thread.is_active === true);
          activeThreadId = activeThread 
            ? (activeThread.thread_id || activeThread.id)
            : (threads[0].thread_id || threads[0].id);
          
          // Update state with conversations, active thread, and knowledgebases
          set({ 
            conversations,
            activeThreadId,
            knowledgebases,
            isLoading: false,
            isInitializing: false,
            authChecked: true
          });
        } else {
          // No threads exist - create a new thread automatically
          await get().createConversation();
          
          // Update state with knowledgebases and loading states
          set({ 
            knowledgebases,
            isLoading: false,
            isInitializing: false,
            authChecked: true
          });
        }
        
        // If we have an active thread, call the /api/thread/set-active API to update the backend
        if (activeThreadId && userId) {
          try {
            await fetchWithAuth(`/api/thread/set-active?user_id=${userId}&thread_id=${activeThreadId}`, {
              method: 'POST'
            });
            
            // Fetch thread history after setting active thread
            await get().fetchThreadHistory(activeThreadId);
          } catch (error) {
            console.error('Error setting active thread at initialization:', error);
            // Continue with initialization even if API call fails
          }
        }
        
      } catch (err) {
      console.error('Failed to initialize app:', err);
      set({ 
        isLoading: false, 
        isInitializing: false,
        authChecked: true,
        error: err.message
      });
      
      // Check if error is due to authentication
      if (err.message.includes('401')) {
        localStorage.removeItem('token');
        set({ user_id: null });
      }
    }
    },

    // Update the active knowledgebase
    setActiveKnowledgebase: async (kbId) => {
      try {
        // Call API to update active knowledgebase using the new endpoint
        const response = await fetchWithAuth(`/api/knowledgebase/${kbId}/active`, {
          method: 'PATCH'
        });
        
        if (response.ok) {
          // Fetch updated knowledgebases
          const kbsResponse = await fetchWithAuth('/api/knowledgebase');
          if (kbsResponse.ok) {
            const kbsData = await kbsResponse.json();
            set({ knowledgebases: kbsData.knowledgebases || [] });
          }
        }
      } catch (error) {
        console.error('Error updating active knowledgebase:', error);
        throw error;
      }
    },

    // Fetch thread history by calling /api/thread/history endpoint
    fetchThreadHistory: async (threadId) => {
      if (!threadId) return;
      
      try {
        const { user_id } = get();
        if (!user_id) {
          console.error('Cannot fetch thread history: user_id is null');
          return;
        }
        
        // Call the /api/thread/history endpoint to get message history
        const response = await fetchWithAuth(`/api/thread/history?user_id=${user_id}&thread_id=${threadId}`);
        
        // Check content type
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
          const textContent = await response.text();
          console.error('Received non-JSON response from /api/thread/history:', textContent);
          throw new Error('Received invalid response format from server');
        }
        
        const historyData = await response.json();
        // Fix: Backend returns 'history' not 'messages'
        const messages = historyData.history || [];
        
        // Ensure all messages have the 'complete' flag
        const messagesWithComplete = messages.map(msg => ({
          ...msg,
          // All existing messages from history should be complete
          complete: true
        }));
        
        // Update the conversation with the fetched messages
        set((state) => ({
          conversations: {
            ...state.conversations,
            [threadId]: {
              ...state.conversations[threadId],
              messages: messagesWithComplete
            }
          }
        }));
      } catch (error) {
        console.error('Error fetching thread history:', error);
        // Continue with initialization even if API call fails
      }
    },

    // Add a message to the active conversation
    addMessage: (message) => {
      updateActiveThread({ messages: [...get().conversations[get().activeThreadId].messages, message] });
    },

    // Create a new conversation thread
    createConversation: async () => {
      try {
        const { user_id } = get();
        if (!user_id) {
          set({ error: 'Failed to create conversation: User not authenticated' });
          return null;
        }
        
        set({ isLoading: true, error: null });
        
        // Generate a default title
        const defaultTitle = `Conversation ${new Date().toLocaleString()}`;
        
        // Call the backend API to create a new thread
        const response = await fetchWithAuth(`/api/thread/create?user_id=${user_id}&title=${encodeURIComponent(defaultTitle)}`, {
          method: 'POST'
        });
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const contentType = response.headers.get('content-type');
        if (!contentType || !contentType.includes('application/json')) {
          const textContent = await response.text();
          console.error('Received non-JSON response from /api/thread/create:', textContent);
          throw new Error('Received invalid response format from server');
        }
        
        const data = await response.json();
        const threadId = data.thread_id;
        
        const newConversation = {
          threadId: threadId,
          title: data.title || defaultTitle,
          messages: [],
          createdAt: new Date().toISOString(),
          updatedAt: new Date().toISOString()
        };
        
        set((state) => ({
          conversations: {
            ...state.conversations,
            [threadId]: newConversation
          },
          activeThreadId: threadId,
          isLoading: false
        }));
        
        return threadId;
      } catch (error) {
        console.error('Error creating conversation:', error);
        set({ error: 'Failed to create conversation: ' + error.message, isLoading: false });
        return null;
      }
    },

    // Switch between conversation threads
    switchConversation: async (threadId) => {
      const { user_id } = get();
      
      // Only make API call if user_id exists
      if (user_id) {
        try {
          // Call the /api/thread/set-active API to update the active thread on the backend
          await fetchWithAuth(`/api/thread/set-active?user_id=${user_id}&thread_id=${threadId}`, {
            method: 'POST'
          });
        } catch (error) {
          console.error('Error setting active thread:', error);
          // Continue with local state update even if API call fails
        }
      }
      
      set(() => ({
        activeThreadId: threadId
      }));
      
      // Fetch thread history after switching
      await get().fetchThreadHistory(threadId);
    },

    // Clear messages in the active conversation
    clearMessages: function() {
      updateActiveThread({
        messages: [],
        title: 'New Chat'
      });
    },

    // Rename a conversation
    renameConversation: async (threadId, newTitle) => {
      // Update local state immediately for responsive UI
      set((state) => ({
        conversations: {
          ...state.conversations,
          [threadId]: {
            ...state.conversations[threadId],
            title: newTitle,
            updatedAt: new Date().toISOString()
          }
        }
      }));

      // Update on backend
      const { user_id } = get();
      if (user_id) {
        try {
          const response = await fetchWithAuth(`/api/thread/rename?user_id=${user_id}&thread_id=${threadId}&title=${encodeURIComponent(newTitle)}`, {
            method: 'PUT'
          });

          if (!response.ok) {
            console.error('Error renaming conversation:', response.status);
            // Revert to original title if backend update fails
            const originalTitle = get().conversations[threadId].title;
            set((state) => ({
              conversations: {
                ...state.conversations,
                [threadId]: {
                  ...state.conversations[threadId],
                  title: originalTitle
                }
              }
            }));
          }
        } catch (error) {
          console.error('Error renaming conversation:', error);
        }
      }
    },

    // Send a message to the backend
    sendMessage: async (content, metadata = {}) => {
      const { user_id, activeThreadId } = get();
      if (!user_id || !activeThreadId) {
        set({ error: 'User not authenticated or no active conversation' });
        return;
      }

      try {
        set({ isLoading: true, error: null });

        // Create a new user message
        const newMessage = {
          id: `msg_${Date.now()}`,
          role: 'user',
          content: content,
          metadata: metadata,
          timestamp: new Date().toISOString(),
          isLoading: true
        };

        // Add the user message to the conversation
        updateActiveThread({ messages: [...get().conversations[activeThreadId].messages, newMessage] });

        // Send the message to the backend
        const response = await fetchWithAuth(`/api/chat`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            message: content,
            user_id,
            thread_id: activeThreadId
          }),
        });

        if (!response.ok) {
          throw new Error(`Failed to send message: ${response.status}`);
        }
        
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
          // If response is JSON, it's a direct response
          let result;
          try {
            result = await response.json();
          } catch (jsonError) {
            console.error('JSON parsing error:', jsonError);
            throw new Error('Invalid JSON response from server');
          }
          
          // Update the message with the response
          set((state) => {
            const updatedMessages = [...state.conversations[activeThreadId].messages];
            const userMessageIndex = updatedMessages.findIndex(msg => msg.id === newMessage.id);
            
            if (userMessageIndex !== -1) {
              // Replace the user message with the updated version (remove loading state)
              updatedMessages[userMessageIndex] = { ...updatedMessages[userMessageIndex], isLoading: false };
            }
            
            // Add the assistant's response
            updatedMessages.push({
              id: `msg_${Date.now()}_response`,
              role: 'assistant',
              content: result.response || 'Sorry, I couldn\'t process your request.',
              metadata: {},
              timestamp: new Date().toISOString(),
              complete: true // Add complete flag set to true for non-streaming responses
            });
            
            return {
              conversations: {
                ...state.conversations,
                [activeThreadId]: {
                  ...state.conversations[activeThreadId],
                  messages: updatedMessages,
                  updatedAt: new Date().toISOString()
                }
              },
              isLoading: false
            };
          });
        } else {
          // If response is not JSON, it might be a streaming response
          const reader = response.body.getReader();
          const decoder = new TextDecoder();
          
          let partialContent = '';
          let assistantMessageId = `msg_${Date.now()}_stream`;
          
          // Add an empty assistant message to the conversation
          updateActiveThread({
            messages: [...get().conversations[activeThreadId].messages, {
              id: assistantMessageId,
              role: 'assistant',
              content: '',
              metadata: {},
              timestamp: new Date().toISOString(),
              complete: false // Add complete flag set to false initially
            }]
          });

          // Process the stream
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            const chunk = decoder.decode(value, { stream: true });
            const lines = chunk.split('\n');
            
            // Process each SSE line
            for (const line of lines) {
              if (line.startsWith('data: ')) {
                try {
                  const jsonData = JSON.parse(line.substring(6));
                  if (jsonData.response) {
                    // Only append the response content, not the entire JSON
                    partialContent += jsonData.response;
                  } else if (jsonData.error) {
                    // Handle error from SSE
                    const errorMsg = jsonData.error;
                    let displayError = errorMsg;
                    
                    // Check for specific error pattern
                    if (errorMsg.includes('Error invoking chat model')) {
                      displayError = 'Error invoking chat model. Please check your API configuration.';
                    }
                    
                    // Show error in modal and remove the assistant message with loading effect
                    set((state) => {
                      const updatedMessages = [...state.conversations[activeThreadId].messages];
                      // Find and remove the assistant message we added for streaming
                      const assistantMessageIndex = updatedMessages.findIndex(msg => msg.id === assistantMessageId);
                      if (assistantMessageIndex !== -1) {
                        updatedMessages.splice(assistantMessageIndex, 1);
                      }
                      
                      return {
                        conversations: {
                          ...state.conversations,
                          [activeThreadId]: {
                            ...state.conversations[activeThreadId],
                            messages: updatedMessages,
                            updatedAt: new Date().toISOString()
                          }
                        },
                        isLoading: false,
                        error: displayError,
                        showErrorModal: true
                      };
                    });
                    
                    // Break out of loops since we encountered an error
                    return;
                  }
                } catch (e) {
                  console.error('Error parsing SSE data:', e);
                }
              }
            }

            // Update the assistant message with the partial content
            set((state) => {
              const updatedMessages = [...state.conversations[activeThreadId].messages];
              const assistantMessageIndex = updatedMessages.findIndex(msg => msg.id === assistantMessageId);
              
              if (assistantMessageIndex !== -1) {
                updatedMessages[assistantMessageIndex] = { 
                  ...updatedMessages[assistantMessageIndex], 
                  content: partialContent
                };
              }
              
              return {
                conversations: {
                  ...state.conversations,
                  [activeThreadId]: {
                    ...state.conversations[activeThreadId],
                    messages: updatedMessages,
                    updatedAt: new Date().toISOString()
                  }
                },
                isLoading: !done
              };
            });
          }
          
          // Mark the assistant message as complete
          set((state) => {
            const updatedMessages = [...state.conversations[activeThreadId].messages];
            const assistantMessageIndex = updatedMessages.findIndex(msg => msg.id === assistantMessageId);
            
            if (assistantMessageIndex !== -1) {
              updatedMessages[assistantMessageIndex] = { 
                ...updatedMessages[assistantMessageIndex], 
                complete: true // Set complete flag to true when streaming is done
              };
            }
            
            return {
              conversations: {
                ...state.conversations,
                [activeThreadId]: {
                  ...state.conversations[activeThreadId],
                  messages: updatedMessages,
                  updatedAt: new Date().toISOString()
                }
              },
              isLoading: false
            };
          });
        }
      } catch (error) {
        console.error('Error sending message:', error);
        
        // Update the message to show error state
        set((state) => {
          const updatedMessages = [...state.conversations[activeThreadId].messages];
          const userMessageIndex = updatedMessages.findIndex(msg => msg.id === `msg_${Date.now()}`);
          
          if (userMessageIndex !== -1) {
            updatedMessages[userMessageIndex] = { ...updatedMessages[userMessageIndex], isLoading: false };
          }
          
          let errorMsg = error.message;
          let displayError = errorMsg;
          
          // Check for specific error pattern
          if (errorMsg.includes('Error invoking chat model')) {
            displayError = 'Error invoking chat model. Please check your API configuration.';
          }
          
          // Show error in modal instead of adding to conversation
          return {
            conversations: {
              ...state.conversations,
              [activeThreadId]: {
                ...state.conversations[activeThreadId],
                messages: updatedMessages,
                updatedAt: new Date().toISOString()
              }
            },
            isLoading: false,
            error: displayError,
            showErrorModal: true
          };
        });
      }
    },

    // Remove a conversation
    removeConversation: async (threadId) => {
      const { user_id, conversations } = get();
      
      if (!user_id) {
        set({ error: 'User not authenticated. Cannot delete conversation.' });
        return;
      }
      
      try {
        set({ isLoading: true, error: null });
        
        // Call backend API to delete the thread
        const response = await fetchWithAuth(`/api/thread/${user_id}/${threadId}`, {
          method: 'DELETE'
        });
        
        if (!response.ok) {
          throw new Error(`Failed to delete conversation: ${response.status}`);
        }
        
        // Create a new conversations object without the deleted thread
        const { [threadId]: deletedConversation, ...remainingConversations } = conversations;
        
        // If the deleted conversation was the active one, set a new active thread
        let newActiveThreadId = get().activeThreadId;
        if (newActiveThreadId === threadId) {
          // Get the keys of remaining conversations
          const remainingThreadIds = Object.keys(remainingConversations);
          // Set to null if no conversations remain, otherwise use the first one
          newActiveThreadId = remainingThreadIds.length > 0 ? remainingThreadIds[0] : null;
        }
        
        // Update state
        set({
          conversations: remainingConversations,
          activeThreadId: newActiveThreadId,
          isLoading: false
        });
        
      } catch (error) {
        console.error('Error deleting conversation:', error);
        set({ error: 'Failed to delete conversation: ' + error.message, isLoading: false });
      }
    },
    
    // Set error message
    setError: (error) => {
      set({ error });
    },

    // Show error modal
    showError: (error) => {
      set({ error, showErrorModal: true });
    },

    // Hide error modal
    hideErrorModal: () => {
      set({ showErrorModal: false });
    },

    // Reset the store
    resetStore: () => {
      set({
        user_id: null,
        activeThreadId: null,
        conversations: {},
        isLoading: false,
        error: null
      });
    },
    
    // Trigger file browser refresh
    refreshFileBrowser: () => {
      set((state) => ({
        fileBrowserRefreshTrigger: state.fileBrowserRefreshTrigger + 1
      }));
    },
    
    // Logout function
    logout: () => {
      // Remove token from localStorage
      localStorage.removeItem('token');
      // Reset store state
      set({
        user_id: null,
        username: null,
        activeThreadId: null,
        conversations: {},
        knowledgebases: [],
        isLoading: false,
        isInitializing: false,
        authChecked: true,
        error: null
      });
    }
  };
});

export default useChatStore;