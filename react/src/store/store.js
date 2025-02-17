import { configureStore } from '@reduxjs/toolkit';
import messagesReducer from './messagesSlice';
import expensesReducer from './expensesSlice';
import budgetReducer from './budgetSlice';  

export default configureStore({
    reducer: {
        messages: messagesReducer,
        expenses: expensesReducer,
        budget: budgetReducer,
    },
});
