import { Box } from '@mui/material';


function Message({ content, author }) {
    return (
        <Box>
            {content}
            {author}
        </Box>
    );
}   

export default Message;