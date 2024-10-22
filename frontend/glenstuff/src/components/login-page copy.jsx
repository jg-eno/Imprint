import { useState } from "react";
import { Link } from "react-router-dom";
import "./Login.css"; 

function Login() {
  const initialValues = { email: "", password: "" };
  const [formValues, setFormValues] = useState(initialValues);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);

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
    <div className="login-container_s">
      {Object.keys(formErrors).length === 0 && isSubmit ? (
        <div className="ui_s message_s success_s">Logged in successfully</div>
      ) : (
        console.log("Entered Details", formValues)
      )}

      <form onSubmit={handleSubmit}>
        <h1>Login</h1>
        <div className="ui_s divider_s"></div>
        <div className="ui_s form_s">
          <div className="field_s">
            <label>Email</label>
            <input
              type="text"
              name="email"
              placeholder="Enter your email"
              value={formValues.email}
              onChange={handleChange}
            />
          </div>
          <p>{formErrors.email}</p>
          <div className="field_s">
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder="Enter your password"
              value={formValues.password}
              onChange={handleChange}
            />
          </div>
          <p>{formErrors.password}</p>
          <button className="fluid_s ui_s button_s blue_s">Login</button>
        </div>
      </form>
      <div className="text_s">
        Don’t have an account? <Link to="/">Sign Up</Link>
      </div>
    </div>
  );
}

export default Login;

