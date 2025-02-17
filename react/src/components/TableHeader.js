import { TableHead, TableRow, TableCell } from '@mui/material';
import { styled } from '@mui/material/styles';

// Custom styled TableCell for the header
const StyledTableCell = styled(TableCell)(({ theme }) => ({
    backgroundColor: '#f5f5f5',
    padding: '8px 16px',
    fontSize: '0.75rem',
    fontWeight: 500,
    color: theme.palette.text.secondary,
    borderBottom: '1px solid #e0e0e0'
}));

function CustomTableHeader({ columns }) {
    return (
        <TableHead>
            <TableRow>
                {columns.map((column) => (
                    <StyledTableCell key={column.id}>
                        {column.label}
                    </StyledTableCell>
                ))}
            </TableRow>
        </TableHead>
    );
}

export default CustomTableHeader; 