import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const messageAgent = createAsyncThunk(
    'messages/messageAgent',
    async (message, { dispatch, signal }) => {
        try {
            // First, add the user's message
            const userMessage = {
                id: Date.now(),
                author: 'user',
                content: message,
                status: 'sent'
            };
            dispatch(addMessage(userMessage));

            const controller = new AbortController();
            signal.addEventListener('abort', () => controller.abort());

            const response = await fetch('http://localhost:8000/api/message-agent', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message }),
                signal: controller.signal
            }); 
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            
            // Return only the assistant's response
            return {
                id: Date.now(),
                author: 'assistant',
                content: data.response,
                status: data.status
            };
        } catch (error) {
            if (error.name === 'AbortError') {
                return;
            }
            throw error;
        }
    }
);


const messagesSlice = createSlice({
    name: 'messages',
    initialState: {
        messages: [
            {
                id: 1,
                author: 'system',
                content: 'Hello, how can I help you today?',
                status: 'sent'
            }
        ],
        status: 'idle',
        error: null
    },
    reducers: {
        addMessage: (state, action) => {
            console.log('Adding message:', action.payload);
            state.messages.push(action.payload);
        }
    },
    extraReducers: (builder) => {
        builder
            .addCase(messageAgent.pending, (state) => {
                state.status = 'loading';
            })
            .addCase(messageAgent.fulfilled, (state, action) => {
                state.status = 'succeeded';
                if (action.payload?.status === 'success') {
                    state.messages.push(action.payload);
                }
            })
            .addCase(messageAgent.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
                state.messages.push({
                    id: Date.now(),
                    author: 'system',
                    content: `Error: ${action.error.message || 'Failed to get response from agent'}`,
                    status: 'error'
                });
            });
    }
});

export const { addMessage } = messagesSlice.actions;

export const selectMessages = (state) => state.messages.messages;

export default messagesSlice.reducer;



