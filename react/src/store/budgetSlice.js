import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchBudget = createAsyncThunk('budget/fetch-budget', async () => {
    const response = await fetch('http://localhost:8000/api/fetch-budget');
    return response.json();
});

const budgetSlice = createSlice({
    name: 'budget',
    initialState: {
        items: [],
        loading: false,
        error: null
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(fetchBudget.pending, (state) => {
                state.loading = true;
            })
            .addCase(fetchBudget.fulfilled, (state, action) => {
                state.loading = false;
                state.items = action.payload.budget;
            })
            .addCase(fetchBudget.rejected, (state, action) => {
                state.loading = false;
                state.error = action.error.message;
            })
    }
});

export default budgetSlice.reducer;