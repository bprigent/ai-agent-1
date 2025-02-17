import { configureStore } from '@reduxjs/toolkit';
import messagesReducer from './messagesSlice';
import expensesReducer from './expensesSlice';
import budgetReducer from './budgetSlice';  

const store = configureStore({
    reducer: {
        messages: messagesReducer,
        expenses: expensesReducer,
        budget: budgetReducer,
    },
});

export default store;