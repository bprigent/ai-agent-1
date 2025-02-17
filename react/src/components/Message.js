import { Box, Typography } from '@mui/material';

function Message({ content, author }) {
    const isUser = author === 'user';
    const isSystem = author === 'system';

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
                    backgroundColor: isUser 
                        ? 'primary.main' 
                        : isSystem 
                        ? 'grey.200' 
                        : '#f5f5f5',
                    color: isUser ? 'white' : 'text.primary',
                    borderRadius: 2,
                    p: 2,
                    whiteSpace: 'pre-wrap', // This will preserve line breaks
                }}
            >
                {isSystem && (
                    <Typography variant="caption" color="text.secondary">
                        System Message
                    </Typography>
                )}
                {!isSystem && (
                    <Typography variant="caption" color={isUser ? 'white' : 'text.secondary'}>
                        {author}
                    </Typography>
                )}
                <Typography variant="body1">
                    {content}
                </Typography>
            </Box>
        </Box>
    );
}

export default Message;