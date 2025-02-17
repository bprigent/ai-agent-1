import { Box, TextField, Button } from '@mui/material';
import Header from '../components/Header';
import { useState } from 'react';

function Chat() {
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!message.trim()) return;
        
        // Handle message submission here
        console.log('Message submitted:', message);
        setMessage('');
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
            <Header title="Chat" />
            
            {/* Main content area */}
            <Box
                sx={{
                    flex: 1,
                    flexGrow: 1,
                    overflowY: 'auto',
                    p: 2
                }}
            >
                {/* Chat messages will go here */}
            </Box>

            {/* Footer with input */}
            <Box
                component="form"
                onSubmit={handleSubmit}
                sx={{
                    borderTop: '1px solid #e0e0e0',
                    p: 2,
                    backgroundColor: 'white',
                    display: 'flex',
                    gap: 1
                }}
            >
                <TextField
                    fullWidth
                    size="small"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type your message..."
                    variant="outlined"
                />
                <Button 
                    type="submit"
                    variant="contained"
                    disabled={!message.trim()}
                >
                    Send
                </Button>
            </Box>
        </Box>
    );
}

export default Chat;