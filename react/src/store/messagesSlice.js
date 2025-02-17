import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const messageAgent = createAsyncThunk(
    'messages/messageAgent',
    async (message) => {
        const response = await fetch('/api/message-agent', {
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
        messages: [],
        status: 'idle',
        error: null
    },
    reducers: {
        addMessage: (state, action) => {
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
                if (action.payload.status === 'success') {
                    state.messages.push(action.payload);
                } else {
                    state.error = action.payload.response;
                }
            })
            .addCase(messageAgent.rejected, (state, action) => {
                state.status = 'failed';
                state.error = action.error.message;
                state.messages.push({
                    id: Date.now(),
                    author: 'system',
                    content: 'Error: Failed to get response from agent',
                    status: 'error'
                });
            });
    }
});

export const { addMessage } = messagesSlice.actions;

export const selectMessages = (state) => state.messages.messages;

export default messagesSlice.reducer;



