import React, {useState} from "react"

export const NavBar = () => {

    return (
    <nav className="nav">
        <a href="/" className="site-title">
            Quantum Quokkas
        </a>
        <ul>
            <li>
                <a href="/">Home</a>
            </li>
            <li>
                <a href="/login">Sign In</a>
            </li>
            <li>
                <a href="/topics">Topics</a>
            </li>
        </ul>
    </nav>
  );
}
