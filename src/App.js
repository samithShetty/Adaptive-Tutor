import React , {useState, useEffect} from "react";
import { BrowserRouter, Route, Link } from "react-router-dom";
import "./App.css";
import {Login} from "./pages/Login";
import { Register } from "./pages/Register";
import { Problem } from "./pages/Problem";

function App() {
  const [currentForm, setCurrentForm] = useState('login');

  const toggleForm = (formName) => {
    setCurrentForm(formName);
  }

  return (
/*
      <div className="App">
        {
          currentForm === "login" ? <Login onFormSwitch={toggleForm}/> : <Register onFormSwitch={toggleForm}/> 
        }
      </div>
*/
        <Problem/>
  );
}

export default App;