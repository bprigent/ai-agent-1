import { useSelector } from 'react-redux';
import { selectMessages } from '../store/messagesSlice';
import Message from './Message';
import { Box } from '@mui/material';

function MessageList() {
    const messages = useSelector(selectMessages);
    const status = useSelector(state => state.messages.status);
    const error = useSelector(state => state.messages.error);

    console.log('Current messages:', messages);
    console.log('Current status:', status);
    console.log('Current error:', error);

    return (
        <Box sx={{ flexGrow: 1, overflow: 'auto', p: 2 }}>
            {messages.map((message) => (
                <Message 
                    key={message.id} 
                    content={message.content}
                    author={message.author}
                />
            ))}
        </Box>
    );
}

export default MessageList;
