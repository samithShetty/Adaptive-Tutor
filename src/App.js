import React , {useState, useEffect} from "react";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Problem } from "./pages/Problem";
import { NavBar } from "./NavBar";

function App() {
  let component
  switch (window.location.pathname) {
    case "/":
      component = <Home />
      break
    case "/topics":
      //component = <Topics />
      break
    case "/login":
      component = <Login />
      break
    case "/register":
      component = <Register />
      break
      
  }

  return (
        <>
          <NavBar/>
          {component}
        </>
  );
}

export default App;