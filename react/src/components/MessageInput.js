import { Box, TextField, Button, CircularProgress } from '@mui/material';
import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { messageAgent } from '../store/messagesSlice';

function MessageInput() {
    const [message, setMessage] = useState('');
    const dispatch = useDispatch();
    const status = useSelector(state => state.messages.status);
    const isLoading = status === 'loading';

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!message.trim() || isLoading) return;
        
        try {
            await dispatch(messageAgent(message)).unwrap();
        } catch (error) {
            console.error('Failed to send message:', error);
        }
        
        setMessage('');
    };

    return (
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
                disabled={isLoading}
            />
            <Button 
                type="submit"
                variant="contained"
                disabled={!message.trim() || isLoading}
            >
                {isLoading ? <CircularProgress size={24} /> : 'Send'}
            </Button>
        </Box>
    );
}

export default MessageInput; 