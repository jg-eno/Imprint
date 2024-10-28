import { SiAnki } from "react-icons/si";
import pic from "/Images/imprintLogo.jpg";
import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(''); // To display login errors, if any

  const handleLogin = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        alert(data.message); // Successful login
      } else {
        setError(data.message); // Handle invalid credentials
      }
    } catch (error) {
      console.error("Login Error:", error);
      setError("An error occurred. Please try again.");
    }
  };

  return (
    <>
      <div className="random">
        <header className="loginHeader">
          <div className="ankiLogo">
            <div className="NamePart">
              <div className="ankiNameLogin">Anki Web</div>
              <SiAnki size={24} />
            </div>
          </div>
          <div className="signUp">
            <button type="button" className="btn btn-primary">
              Sign Up
            </button>
          </div>
        </header>

        <div className="login-container">
          <div className="login-left">
            <img 
              src={pic}
              alt="Login Illustration"
              className="login-image"
            />
          </div>

          <div className="login-right">
            <Box>
              <Typography variant="h4" gutterBottom className="login-title">
                Login
              </Typography>
              <div className="loginInfo">
                Log into your existing Account
              </div>

              {error && <Typography color="error">{error}</Typography>} {/* Error Display */}

              <TextField
                label="Email"
                variant="outlined"
                fullWidth
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                margin="normal"
                className="login-field"
              />
              <TextField
                label="Password"
                type="password"
                variant="outlined"
                fullWidth
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                margin="normal"
                className="login-field"
              />
              <Button
                variant="contained"
                color="primary"
                onClick={handleLogin}
                fullWidth
                className="login-button"
              >
                Login
              </Button>

              <div className="ResetPass">
                <a href="#">Reset Password</a>
              </div>
            </Box>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginPage;
