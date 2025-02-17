import { configureStore } from '@reduxjs/toolkit';
import messagesReducer from './messagesSlice';
// ... other imports

export const store = configureStore({
  reducer: {
    messages: messagesReducer,
    // ... other reducers
  },
}); 