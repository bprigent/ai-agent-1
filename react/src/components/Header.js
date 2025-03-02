import { Box, Typography } from '@mui/material';

function Header({ title }) {
    return (
        <Box
            sx={{
                height: '40px',
                display: 'flex',
                alignItems: 'center',
                px: 2,
                borderBottom: '1px solid #e0e0e0',
                backgroundColor: 'white'
            }}
        >
            <Typography variant="subtitle1" fontWeight={500}>
                {title}
            </Typography>
        </Box>
    );
}

export default Header; 