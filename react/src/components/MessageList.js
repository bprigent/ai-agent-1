import { useSelector } from 'react-redux';
import { selectMessages } from '../store/messagesSlice';

function MessageList() {
    const messages = useSelector(selectMessages);

    return (
        <div>
            {messages.map((message) => (
                <div key={message.id}>
                    <strong>{message.author}:</strong> {message.content}
                </div>
            ))}
        </div>
    );
}

export default MessageList;
