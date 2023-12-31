import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import userIcon from "../../images/user-icon.png"
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [first_name, setFirstName] = useState("");
	const [last_name, setLastName] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [profile_image_id, setProfileImageId] = useState(null);
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	useEffect(() => {
		const errors = {};
		if (username.length === 0) errors.username = "";
		if (email.length === 0) errors.email = "";
		if (first_name.length === 0) errors.firstName = "";
		if (last_name.length === 0) errors.lastName = "";
		if (password.length === 0 || password.length < 6) errors.password = "";
		if (confirmPassword.length === 0 || confirmPassword.length < 6)
		  errors.confirmPassword = "";
		if (username.length < 4 && username.length > 0)
		  errors.username = "Username needs to be at least 4 characters.";
		if (password.length < 6 && password.length > 0)
		  errors.password = "Password needs to be at least 6 characters.";

		setErrors(Object.values(errors));
	  }, [email, first_name, last_name, username, password, confirmPassword]);


	  const isValidEmail = (email) => {
		const emailRegex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
		return emailRegex.test(email);
	  };


	const handleSubmit = async (e) => {
		e.preventDefault();
		console.log("Username:", username);
		console.log("Email:", email);
		console.log("Password:", password);
		console.log("First Name:", first_name);
		console.log("Last Name:", last_name);
		console.log("Profile Image ID:", profile_image_id);


		if (password === confirmPassword) {

            if (!isValidEmail(email)) {
				setErrors(["Invalid email format"]);
				return;
			}

			const formData = new FormData();

			formData.append("username", username);
			formData.append("email", email);
			formData.append("password", password);
			formData.append("first_name", first_name);
			formData.append("last_name", last_name);
			console.log("Profile Image ID (Before FormData):", profile_image_id);
			formData.append("profile_image_id", profile_image_id);
			console.log("AFTER Profile Image ID:", profile_image_id);

			const data = await dispatch(signUp(username, email, password, first_name, last_name, profile_image_id));
			console.log("THIS IS DATA:", data);
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Passwords must match",
			]);
		}
	}

	return (
		<>
			<div className="icon-container">
				<img src={userIcon}
					className="icon"
					alt=""
				/>
			</div>
			<div className="signup_container">
				<div className="signup_title">Sign Up for Yelping</div>
				<form onSubmit={handleSubmit}>
					<div className="business-error__container">
						{errors.map((error, idx) => (
							<div className="signup-error" key={idx}>{(error)}</div>
						))}
					</div>
					<div className='signup__input'>
						{/* <label>Username</label> */}
						<input
							type="text"
							placeholder="Username"
							value={username}
							onChange={(e) => setUsername(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input'>
						{/* Email */}
						<input
							type="text"
							placeholder="Email"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input'>
						{/* First Name */}
						<input
							type="text"
							placeholder="First Name"
							value={first_name}
							onChange={(e) => setFirstName(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input'>
						{/* Last Name */}
						<input
							type="text"
							placeholder="Last Name"
							value={last_name}
							onChange={(e) => setLastName(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input'>
						{/* Profile Image */}
						<input
                            type="file"
                            placeholder="Please provide a profile picture"
                            accept="image/*"
                            onChange={(e) => setProfileImageId(e.target.files[0])}
                            required
						/>
					</div>
					<div className='signup__input'>
						{/* Password */}
						<input
							type="password"
							placeholder="Password"
							value={password}
							onChange={(e) => setPassword(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input'>
						{/* Confirm Password */}
						<input
							type="password"
							placeholder="Confirm Password"
							value={confirmPassword}
							onChange={(e) => setConfirmPassword(e.target.value)}
							required
						/>
					</div>
					<div className='signup__input_button_container'>
						<button className="signup__button" type="submit">Sign Up</button>
					</div>
				</form>
			</div >
		</>
	);
}

export default SignupFormModal;
