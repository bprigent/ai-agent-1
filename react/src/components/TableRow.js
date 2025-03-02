import { TableRow, TableCell } from '@mui/material';
import { styled } from '@mui/material/styles';

const StyledTableCell = styled(TableCell)({
    padding: '12px 16px',
    fontSize: '0.875rem',
    borderBottom: '1px solid #e0e0e0'
});

function CustomTableRow({ columns, data }) {
    return (
        <TableRow>
            {columns.map((column) => (
                <StyledTableCell key={column.id}>
                    {column.render(data)}
                </StyledTableCell>
            ))}
        </TableRow>
    );
}

export default CustomTableRow; 