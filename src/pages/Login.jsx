import React, {useState} from "react";

export const Login = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(username, password);
    }
    
    return (
      <div className="auth-form-container">
        <h1>Login</h1>
        <form className="login-form" onSubmit={handleSubmit}>
            <label htmlFor="username">username</label>
            <input value = {username} onChange={(e)=> setUsername(e.target.value)} type="username" placeholder="username" id = "username" name = "username"/>
            <label htmlFor="password">password</label>
            <input value = {password} onChange={(e)=> setPassword(e.target.value)}type="password" placeholder="********" id = "password" name = "password"/>
            <button type="submit">Log In</button>
        </form>
        <a href="/register">
          <button className="link-btn">Don't have an account? Register Here!</button>
        </a>
      </div>
    )
}