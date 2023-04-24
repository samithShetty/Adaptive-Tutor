import React, {useState} from "react";

export const Home = (props) => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(username, password);
    }
    
    return (
      <h1>Welcome to the Adaptive Tutor</h1>
    )
}