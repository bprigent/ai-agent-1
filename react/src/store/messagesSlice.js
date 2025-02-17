import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const messageAgent = createAsyncThunk(
    'messages/messageAgent',
    async (message) => {
        console.log('Sending message to agent:', message);
        const response = await fetch('http://localhost:8000/api/message-agent', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message })
        }); 
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        console.log('Received response from agent:', data);
        return {
            id: Date.now(),
            author: 'assistant',
            content: data.response,
            status: data.status
        };
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
                console.log('Agent request pending');
                state.status = 'loading';
            })
            .addCase(messageAgent.fulfilled, (state, action) => {
                console.log('Agent request fulfilled:', action.payload);
                state.status = 'succeeded';
                if (action.payload.status === 'success') {
                    state.messages.push(action.payload);
                } else {
                    state.error = action.payload.response;
                    state.messages.push({
                        id: Date.now(),
                        author: 'system',
                        content: `Error: ${action.payload.response}`,
                        status: 'error'
                    });
                }
            })
            .addCase(messageAgent.rejected, (state, action) => {
                console.log('Agent request rejected:', action.error);
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



