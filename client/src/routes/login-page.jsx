import { useState } from "react";
import { Link } from "react-router-dom";
import "../components/Login.css"; 

function Login() {
  const initialValues = { email: "", password: "" };
  const [formValues, setFormValues] = useState(initialValues);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault(); // Prevent page reload
    
    const { email, password } = formValues;
    try {
      const response = await fetch("http://127.0.0.1:5001/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({email, password }),
        
      });

      const data = await response.json();
      if (response.ok) {
        alert(data.message); // Login Successful
        window.location.href = "/"; // Redirect to home page
      } else {
        alert(data.message); // Invalid credentials
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  };

  
const handleChange = (e) => {
    const { name, value } = e.target;
    setFormValues({ ...formValues, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setFormErrors(validate(formValues));
    setIsSubmit(true);
  };

  const validate = (values) => {
    const errors = {};
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;
    if (!values.email) {
      errors.email = "Email is required!";
    } else if (!regex.test(values.email)) {
      errors.email = "This is not a valid email format!";
    }
    if (!values.password) {
      errors.password = "Password is required!";
    } else if (values.password.length < 4) {
      errors.password = "Password must be more than 4 characters";
    }
    return errors;
  };

  return (
    <div className="login-container">
      {Object.keys(formErrors).length === 0 && isSubmit ? (
        <div className="ui message success">Logged in successfully</div>
      ) : (
        console.log("Entered Details", formValues)
      )}

      <form onSubmit={handleSubmit}>
        <h1>Login</h1>
        <div className="ui divider"></div>
        <div className="ui form">
          <div className="field">
            <label>Email</label>
            <input
              type="text"
              name="email"
              className="loginInput"
              placeholder="Enter your email"
              value={formValues.email}
              onChange={handleChange}
            />
          </div>
          <p>{formErrors.email}</p>
          <div className="field">
            <label>Password</label>
            <input
              type="password"
              name="password"
              className="loginInput"
              placeholder="Enter your password"
              value={formValues.password}
              onChange={handleChange}
            />
          </div>
          <p>{formErrors.password}</p>
          <button className="loginPagebuttons fluid ui button blue"
          onClick={handleLogin}>Login</button>
        </div>
      </form>
      <div className="text">
        Don’t have an account? <Link to="/Signup">Sign Up</Link>
      </div>
    </div>
  );
}

export default Login;
