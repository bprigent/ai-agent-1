import { 
    Drawer, 
    List, 
    ListItem, 
    ListItemText, 
    ListItemButton
} from '@mui/material';
import { Link, useLocation } from 'react-router-dom';

function Navigation() {
    const location = useLocation();
    const drawerWidth = 320;

    const menuItems = [
        { text: 'Money Agent', path: '/' },
        { text: 'Chat', path: '/chat' },
        { text: 'Budget', path: '/budget' },
        { text: 'Expenses', path: '/expenses' }
    ];

    return (
        <Drawer
            variant="permanent"
            sx={{
                width: drawerWidth,
                flexShrink: 0,
                '& .MuiDrawer-paper': {
                    width: drawerWidth,
                    boxSizing: 'border-box',
                    backgroundColor: '#f5f5f5',
                    borderRight: '1px solid #e0e0e0'
                },
            }}
        >
            <List>
                {menuItems.map((item) => (
                    <ListItem key={item.text} disablePadding>
                        <ListItemButton
                            component={Link}
                            to={item.path}
                            selected={location.pathname === item.path}
                            sx={{
                                '&.Mui-selected': {
                                    backgroundColor: 'rgba(0, 0, 0, 0.08)',
                                    '&:hover': {
                                        backgroundColor: 'rgba(0, 0, 0, 0.12)',
                                    },
                                },
                            }}
                        >
                            <ListItemText primary={item.text} />
                        </ListItemButton>
                    </ListItem>
                ))}
            </List>
        </Drawer>
    );
}

export default Navigation;  