import React from 'react';
import { Link } from 'react-router-dom';
import { SiAnki } from "react-icons/si";


const Header = () => {
  return (
        <header className='LandingHeader'>
        <div class="logo" >
        {/* <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Anki-logo.svg" alt="Anki Logo"/> */}
        <Link to="/" className='logoAnki'>
        <div className="logoAnki">         
            <h4 >AnkiWeb</h4>            
        <SiAnki size={30}/>
        </div>
        </Link>

        <nav>
        <ul class="nav-links">
        <li><Link to="/">Decks</Link></li>
        <li><Link to="/addCard">Add</Link></li>
        <li><Link to="/search">Search</Link></li>
        </ul>
        </nav>
        </div>
        <div class="account-options">
        <Link to="/Profile">Account</Link>
        <Link to="/login">Logout</Link>
        </div>
        <div class="menu-toggle">
       
      
        <span></span>
        <span></span>
        <span></span>
        </div>
        </header>

  );
};

export default Header;
