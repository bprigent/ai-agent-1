import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchExpenses = createAsyncThunk(
    'expenses/fetchAll',
    async () => {
        let url = 'http://localhost:8000/api/fetch-all-expenses';
        const response = await fetch(url);
        return response.json();
    }
);

const expensesSlice = createSlice({
    name: 'expenses',
    initialState: {
        items: [],
        loading: false,
        error: null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchExpenses.pending, (state) => {
                state.loading = true;
            })
            .addCase(fetchExpenses.fulfilled, (state, action) => {
                state.loading = false;
                state.items = action.payload.expenses;
            })
            .addCase(fetchExpenses.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message;
            })
    },
});

export default expensesSlice.reducer; 