import './navbar.css';
import {Link} from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar">
            <div className="headContianer">
            <Link className='navbar-brand' to='/'>
              Money Tracker
            </Link>
            <div className="desktopMenu">
            <Link className="nav-link desktopMenuListItem" to="/">Home</Link>
            <Link className="nav-link desktopMenuListItem" to="/create/">Add New Transaction</Link>
            </div>
            </div> 
              
            
        </nav>
        )};

        export default Navbar;