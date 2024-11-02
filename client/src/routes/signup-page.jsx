import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../components/Signup.css";

function Signup() {
    const initialValues = {
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
    };
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});
    const [isSubmit, setIsSubmit] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormValues({ ...formValues, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent page reload
        
        const errors = validate(formValues); // Validate the form
        setFormErrors(errors); // Set validation errors

        if (Object.keys(errors).length === 0) {
            try {
                const response = await fetch("http://127.0.0.1:5000/signup", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formValues),
                });

                const data = await response.json();
                if (response.ok) {
                    alert(data.message); // Login Successful
                } else {
                    alert(data.message); // Invalid credentials
                }
                setIsSubmit(true); // Mark as successfully submitted
            } catch (error) {
                console.error("Error:", error);
                alert("An error occurred. Please try again.");
            }
        }
    };

    useEffect(() => {
        if (Object.keys(formErrors).length === 0 && isSubmit) {
            console.log("Submitted Successfully:", formValues);
        }
    }, [formErrors, formValues, isSubmit]);

    const validate = (values) => {
        const errors = {};
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/i;

        if (!values.username) {
            errors.username = "Username is required!";
        }
        if (!values.email) {
            errors.email = "Email is required!";
        } else if (!regex.test(values.email)) {
            errors.email = "This is not a valid email format!";
        }
        if (!values.password) {
            errors.password = "Password is required";
        } else if (values.password.length < 4) {
            errors.password = "Password must be more than 4 characters";
        } else if (values.password.length > 10) {
            errors.password = "Password cannot exceed more than 10 characters";
        }
        if (values.password !== values.confirmPassword) {
            errors.confirmPassword = "Those passwords didn’t match. Try again.";
        }
        return errors;
    };

    return (
        <div className="bgImg">
            <div className="container">
                {isSubmit && Object.keys(formErrors).length === 0 && (
                    <div className="ui message success">Signed up successfully</div>
                )}

                <form onSubmit={handleSubmit}>
                    <h1 className="signupheading">Sign Up</h1>
                    <div className="ui divider"></div>
                    <div className="ui form">
                        <div className="field">
                            <label>Username</label>
                            <input
                                type="text"
                                name="username"
                                className="signupPageInputs"
                                placeholder="Choose a username"
                                value={formValues.username}
                                onChange={handleChange}
                            />
                            {formErrors.username && <p>{formErrors.username}</p>}
                        </div>
                        
                        <div className="field">
                            <label>Email</label>
                            <input
                                type="text"
                                name="email"
                                className="signupPageInputs"
                                placeholder="Email"
                                value={formValues.email}
                                onChange={handleChange}
                            />
                            {formErrors.email && <p>{formErrors.email}</p>}
                        </div>
                        
                        <div className="field">
                            <label>Password</label>
                            <input
                                type="password"
                                name="password"
                                className="signupPageInputs"
                                placeholder="Password"
                                value={formValues.password}
                                onChange={handleChange}
                            />
                            {formErrors.password && <p>{formErrors.password}</p>}
                        </div>
                        
                        <div className="field">
                            <label>Confirm Password</label>
                            <input
                                type="password"
                                name="confirmPassword"
                                className="signupPageInputs"
                                placeholder="Confirm password"
                                value={formValues.confirmPassword}
                                onChange={handleChange}
                            />
                            {formErrors.confirmPassword && <p>{formErrors.confirmPassword}</p>}
                        </div>

                        <button className="SignupPageButtons fluid ui button blue">
                            Submit
                        </button>
                    </div>
                    
                    <div className="text">
                        Already have an account? <Link to="/Login">Login</Link>
                    </div>
                </form>
            </div>
        </div>
    );
}

export default Signup;
