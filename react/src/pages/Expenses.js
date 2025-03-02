import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { 
    Box, 
    Table, 
    TableBody, 
    TableContainer, 
    Paper,
    CircularProgress
} from '@mui/material';
import Header from '../components/Header';
import { fetchExpenses } from '../store/expensesSlice';
import CustomTableHeader from '../components/TableHeader';
import CustomTableRow from '../components/TableRow';

function Expenses() {

    const dispatch = useDispatch();
    const { items, loading } = useSelector((state) => state.expenses);

    const expenseColumns = [
        { 
            id: 'date', 
            label: 'Date',
            render: (expense) => new Date(expense.Date).toLocaleDateString()
        },
        { 
            id: 'expenseName', 
            label: 'Expense Name',
            render: (expense) => expense['Expense Name']
        },
        { 
            id: 'budgetCategory', 
            label: 'Budget Category',
            render: (expense) => expense['Budget Category']
        },
        { 
            id: 'accountNumber', 
            label: 'Account Number',
            render: (expense) => expense['Account Number']
        },
        { 
            id: 'amount', 
            label: 'Amount',
            render: (expense) => `$${Math.abs(expense.Amount).toFixed(2)}`
        }
    ];

    useEffect(() => {
        dispatch(fetchExpenses());
    }, [dispatch]);

    return (
        <Box sx={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
            <Header title="Expenses" />
            <TableContainer component={Paper} sx={{ flex: 1 }}>
                {loading ? (
                    <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
                        <CircularProgress />
                    </Box>
                ) : (
                    <Table>
                        <CustomTableHeader columns={expenseColumns} />
                        <TableBody>
                            {items.map((expense, index) => (
                                <CustomTableRow 
                                    key={index}
                                    columns={expenseColumns}
                                    data={expense}
                                />
                            ))}
                        </TableBody>
                    </Table>
                )}
            </TableContainer>
        </Box>
    );
}

export default Expenses;