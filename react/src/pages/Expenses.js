import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { 
    Box, 
    Table, 
    TableBody, 
    TableCell, 
    TableContainer, 
    TableHead, 
    TableRow,
    Paper,
    CircularProgress
} from '@mui/material';
import Header from '../components/Header';
import { fetchExpenses } from '../store/expensesSlice';

function Expenses() {

    const dispatch = useDispatch();
    const { items, loading } = useSelector((state) => state.expenses);

    useEffect(() => {
        dispatch(fetchExpenses());
    }, [dispatch]);

    return (
        <Box sx={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
            
            <Header title="Expenses" />

            <TableContainer component={Paper} sx={{ flex: 1, mx: 2 }}>
                {loading ? (
                    <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
                        <CircularProgress />
                    </Box>
                ) : (
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell>Date</TableCell>
                                <TableCell>Description</TableCell>
                                <TableCell>Category</TableCell>
                                <TableCell>Account</TableCell>
                                <TableCell>Amount</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {items.map((expense, index) => (
                                <TableRow key={index}>
                                    <TableCell>{new Date(expense.Date).toLocaleDateString()}</TableCell>
                                    <TableCell>{expense['Expense Name']}</TableCell>
                                    <TableCell>{expense['Budget Category']}</TableCell>
                                    <TableCell>{expense['Account Number']}</TableCell>
                                    <TableCell>${Math.abs(expense.Amount).toFixed(2)}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                )}
            </TableContainer>
        </Box>
    );
}

export default Expenses;