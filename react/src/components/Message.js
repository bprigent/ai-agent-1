import { Box, Typography } from '@mui/material';

function Message({ content, author }) {
    const isUser = author === 'user';

    return (
        <Box
            sx={{
                width: '100%',
                display: 'flex',
                justifyContent: isUser ? 'flex-end' : 'flex-start',
                mb: 1
            }}
        >
            <Box
                sx={{
                    maxWidth: '70%',
                    backgroundColor: isUser ? 'primary.main' : '#f5f5f5',
                    color: isUser ? 'white' : 'text.primary',
                    borderRadius: isUser ? 2 : 0,
                    p: isUser ? 1 : 0,
                }}
            >
                <Typography variant="body1">
                    {content}
                </Typography>
            </Box>
        </Box>
    );
}

export default Message;