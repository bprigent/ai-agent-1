import { Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline, Box } from '@mui/material';
import Home from './pages/Home';
import NotFound from './pages/NotFound';
import Chat from './pages/Chat';
import Navigation from './components/Navigation';
import store from './store/store';
import { Provider } from 'react-redux';
import Expenses from './pages/Expenses';
import Budget from './pages/Budget';

const theme = createTheme({
  palette: {
    primary: {
      main: '#000000',
    },
    secondary: {
      main: '#292929',
    },
  },
  typography: {
    fontFamily: '"DM Sans", sans-serif',
    h1: {
      fontWeight: 700,
      fontSize: '4rem',
      lineHeight: 1.2,
    },
    h2: {
      fontWeight: 700,
      fontSize: '3rem',
      lineHeight: 1.3,
    },
    h3: {
      fontWeight: 500,
      fontSize: '2.5rem',
      lineHeight: 1.3,
    },
    h4: {
      fontWeight: 500,
      fontSize: '2rem',
      lineHeight: 1.4,
    },
    button: {
      fontWeight: 500,
      textTransform: 'none',  // This prevents automatic uppercase transformation
    },
    body1: {
      fontSize: '1rem',
      lineHeight: 1.5,
    },
    body2: {
      fontSize: '0.875rem',
      lineHeight: 1.5,
    },
  },
});

function App() {
  return (
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Box sx={{ display: 'flex' }}>
        <Navigation />
        <Box
          component="main"
          sx={{
            flexGrow: 1,
          }}
        >
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/chat" element={<Chat />} />
            <Route path="*" element={<NotFound />} />
            <Route path="/expenses" element={<Expenses />} />
            <Route path="/budget" element={<Budget />} />
          </Routes>
          </Box>
        </Box>
      </ThemeProvider>
    </Provider>
  );
}

export default App;
