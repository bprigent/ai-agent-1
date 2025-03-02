import Header from '../components/Header';
import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Box, TableContainer, Paper, CircularProgress, Table, TableBody } from '@mui/material';
import { fetchBudget } from '../store/budgetSlice';
import CustomTableHeader from '../components/TableHeader';
import CustomTableRow from '../components/TableRow';

function Budget() {
    const dispatch = useDispatch();
    const { items, loading } = useSelector((state) => state.budget);

    const budgetColumns = [
        {
            id: 'budgetCategory',
            label: 'Budget Category',
            render: (budget) => budget['Budget Category']
        }, 
        {
            id: 'budgetAmount',
            label: 'Budget Amount',
            render: (budget) => `$${Math.abs(budget['Budget Amount']).toFixed(2)}`
        }
    ];

    useEffect(() => {
        let mounted = true;
        
        const fetchData = async () => {
            if (mounted) {
                dispatch(fetchBudget());
            }
        };

        fetchData();

        return () => {
            mounted = false;
        };
    }, [dispatch]);

    return (
        <Box sx={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
            <Header title="Budget" />
            <TableContainer component={Paper} sx={{ flex: 1 }}>
                {loading ? (
                    <Box sx={{ display: 'flex', justifyContent: 'center', p: 3 }}>
                        <CircularProgress />
                    </Box>
                ) : (
                    <Table>
                        <CustomTableHeader columns={budgetColumns} />
                        <TableBody>
                            {items.map((budget, index) => (
                                <CustomTableRow key={index} columns={budgetColumns} data={budget} />
                            ))}
                        </TableBody>
                    </Table>
                )}
            </TableContainer>
        </Box>
    );
}   

export default Budget;  