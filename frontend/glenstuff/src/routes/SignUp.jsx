// import React, { useState } from 'react';
// import { TextField, Button, Container, Typography, Box } from '@mui/material';

// const SignupPage = () => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [confirmPassword, setConfirmPassword] = useState('');

//   const handleSignup = () => {
//     // Handle signup logic here
//   };

//   return (
//     <Container maxWidth="sm">
//       <Box mt={5}>
//         <Typography variant="h4" gutterBottom>Signup</Typography>
//         <TextField
//           label="Email"
//           variant="outlined"
//           fullWidth
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           margin="normal"
//         />
//         <TextField
//           label="Password"
//           type="password"
//           variant="outlined"
//           fullWidth
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//           margin="normal"
//         />
//         <TextField
//           label="Confirm Password"
//           type="password"
//           variant="outlined"
//           fullWidth
//           value={confirmPassword}
//           onChange={(e) => setConfirmPassword(e.target.value)}
//           margin="normal"
//         />
//         <Button
//           variant="contained"
//           color="primary"
//           onClick={handleSignup}
//           fullWidth
//         >
//           Signup
//         </Button>
//       </Box>
//     </Container>
//   );
// };

// export default SignupPage;



import { SiAnki } from "react-icons/si";

import pic from "/Images/imprintLogo.jpg"
import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';


const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log("Logged in");
  };

  return (
        <>
    <header className="loginHeader">

         <div className="ankiLogo">
           <div className='NamePart'>
             <div className="ankiNameLogin">Anki Web</div>
             <SiAnki size={24}/>
           </div>
           <div>
        
           </div>
       </div>
       <div className="signUp">
       <button type="button" class="btn btn-success">Login</button>
       <button type="button" class="btn btn-primary">Sign Up</button>
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
            Sign Up
          </Typography>
          <div className="loginInfo">
            Create a free account in under a minute...
          </div>
          <div className="loginInfo2">
            We will send you an email to confirm your address, so please ensure your email address is correct
          </div>
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
            Sign up
          </Button>

          <div className="SignupMessage">
            Your email is used as your Anki Web ans for communication relating to service , such as when you reset your password.
          </div>
          
        </Box>
      </div>
    </div>
    </>
  );
};

export default LoginPage;
