import { configureStore } from '@reduxjs/toolkit';
import messagesReducer from './messagesSlice';
import expensesReducer from './expensesSlice';

export default configureStore({
    reducer: {
        messages: messagesReducer,
        expenses: expensesReducer,
    },
});
