import { useNavigate } from 'react-router-dom';


function NotFound() {

    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/');
    }

    return (
        <div>
            <h1>404 - Page Not Found</h1>
            <p>The page you are looking for does not exist.</p>
            <button onClick={handleClick}>Go to Home</button>
        </div>
    );
}

export default NotFound; 