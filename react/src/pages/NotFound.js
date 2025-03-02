import { useNavigate } from 'react-router-dom';
import { 
    Box, 
    Typography, 
    Button
} from '@mui/material';

function NotFound() {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/');
    }

    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                    minHeight: '100vh',
                    textAlign: 'center',
                    gap: 2
                }}
            >
            <Typography variant="h1" component="h1" color="primary">
                404
            </Typography>
            <Typography variant="h4" component="h2" gutterBottom>
                Page Not Found
            </Typography>
            <Typography variant="body1" color="text.secondary" paragraph>
                The page you are looking for does not exist.
            </Typography>
            <Button 
                variant="contained" 
                onClick={handleClick}
                size="large"
            >
                Back to Home
            </Button>
        </Box>
    );
}

export default NotFound; 