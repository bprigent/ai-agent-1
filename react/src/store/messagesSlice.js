import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const messageAgent = createAsyncThunk(
    'messages/messageAgent',
    async (message) => {
        const response = await fetch('/api/message-agent', {
            method: 'POST',
            body: JSON.stringify({ message })
        }); 
        return response.json();
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
                state.messages.push(action.payload);
            })
            .addCase(messageAgent.rejected, (state, action) => {
                state.status = 'failed';    
            })
    }
});

export const { addMessage } = messagesSlice.actions;

export const selectMessages = (state) => state.messages.messages;

export default messagesSlice.reducer;



