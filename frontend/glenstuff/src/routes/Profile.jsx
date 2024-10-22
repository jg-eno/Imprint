import "../components/profile.css";
import React, { useState } from 'react';
import styled, { ThemeProvider } from 'styled-components';
import Header from "../components/Header";

const Profile =()=>{ 
  
    const [isDarkMode, setIsDarkMode] = useState(true);


    const toggleTheme = () => {
        setIsDarkMode(!isDarkMode);
    };

    const handleChangeEmail=()=>{
        console.log("Change Email");
    }

    const handleChangePassword=()=>{
        console.log("Change Password");
    }

    const handleUpdate=()=>{
        console.log("Update");
    }
  return (
    <>
    <div className="profileSection">
    <Header/>

    <div className="accountContent">
    
    <div className={`settings-container ${isDarkMode ? 'dark' : 'light'}`}>
      <header className="header">
        <h2>Account Settings</h2>
        <button className="theme-toggle" onClick={toggleTheme}>
          {isDarkMode ? 'Light Mode' : 'Dark Mode'}
        </button>
      </header>

      <div className="form-section">
        <div className="form-group">
          <button className=" change-btn btn btn-outline-warning " onClick={handleChangeEmail}>Change Email</button>
          <input type="email" placeholder="New email" className="input-field" />
        </div>

        <div className="form-group">
          <button className="change-btn  btn btn-outline-warning " onClick={handleChangePassword}>Change Password</button>
          <input type="password" placeholder="Current password" className="input-field" />
        </div>

        <button className="btn btn-outline-success" onClick={handleUpdate}>Update</button>
        <a href="#" className="remove-account">Remove Account</a>
      </div>
      </div>
      <div className="tagline">
        <span className="gradient-text">Master <br /> Knowledge, <br />One Card at a Time.</span>
        </div>

    </div>
    </div>
    </>
  );
}

export default Profile;