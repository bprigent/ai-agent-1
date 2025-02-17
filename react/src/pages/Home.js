import { 
    Typography, 
    Box,
    Button
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Header from '../components/Header';

// Example Home component
function Home() {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/chat');
    };

    return (
        <Box
            sx={{
                height: '100vh',
                display: 'flex',
                flexDirection: 'column',
                overflow: 'hidden'  // Prevent scrolling
            }}
        >
            <Header title="Home" />
            
            <Box
                sx={{
                    flex: 1,
                    flexGrow: 1,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: 2
                }}
            >
                <Typography variant="h2" component="h1" gutterBottom>
                    Welcome to Origin Agent
                </Typography>
                <Button variant="contained" color="primary" onClick={handleClick}>
                    Chat now
                </Button>
            </Box>
        </Box>
    );
}

export default Home;
