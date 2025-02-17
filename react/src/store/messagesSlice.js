import { createSlice } from '@reduxjs/toolkit';

const messagesSlice = createSlice({
    name: 'messages',
    initialState: {
        messages: []
    },
    reducers: {
        addMessage: (state, action) => {
            state.messages.push(action.payload);
        }
    }
});

export const { addMessage } = messagesSlice.actions;

export const selectMessages = (state) => state.messages.messages;

export default messagesSlice.reducer;



