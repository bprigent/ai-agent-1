import { Box, TextField, Button } from '@mui/material';
import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addMessage } from '../store/messagesSlice';
import { messageAgent } from '../store/messagesSlice';

function MessageInput() {
    const [message, setMessage] = useState('');
    const dispatch = useDispatch();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!message.trim()) return;
        
        dispatch(addMessage({
            id: Date.now(),
            author: 'user',
            content: message,
            status: 'sent'
        }));

        dispatch(messageAgent(message));

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
            />
            <Button 
                type="submit"
                variant="contained"
                disabled={!message.trim()}
            >
                Send
            </Button>
        </Box>
    );
}

export default MessageInput; 