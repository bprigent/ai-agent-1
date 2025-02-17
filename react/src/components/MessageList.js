import { useSelector } from 'react-redux';
import { selectMessages } from '../store/messagesSlice';
import { Box } from '@mui/material';
import Message from './Message';
import { useEffect } from 'react';

function MessageList() {
    const messages = useSelector(selectMessages);
    
    useEffect(() => {
        console.log(messages);
    }, [messages]);

    return (
        <Box>
            {messages.map((message) => (
                <Message key={message.id} content={message.content} author={message.author} />
            ))}
        </Box>
    );
}

export default MessageList;
