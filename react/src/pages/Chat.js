import { Box } from '@mui/material';
import Header from '../components/Header';
import MessageList from '../components/MessageList';
import MessageInput from '../components/MessageInput';

function Chat() {
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
            <Box
                sx={{
                    flex: 1,
                    flexGrow: 1,
                    overflowY: 'auto',
                    p: 2
                }}
            >
                <MessageList />
            </Box>
            <MessageInput />
        </Box>
    );
}

export default Chat;