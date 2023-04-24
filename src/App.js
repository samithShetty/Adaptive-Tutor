import { Home } from "./pages/Home";
import { NavBar } from "./components/NavBar";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Topics } from "./pages/Topics";
import { LinearEquation } from "./MathProblems/LinearEquation";
import { ContinuousRandomVar } from "./MathProblems/ContinuousRandomVar";
import { DiscreteProbability } from "./MathProblems/DiscreteProbability";
import { SamplingDistribution } from "./MathProblems/SamplingDistribution";
import "./App.css"


function App() {
  let component;
  switch (window.location.pathname) {
    case "/":
      component = <Home />
      break
    case "/topics":
      component = <Topics />
      break
    case "/login":
      component = <Login />
      break
    case "/register":
      component = <Register />
      break
    case "/problem/crv":
      component = <ContinuousRandomVar />
      break
    case "/problem/dp":
        component = <DiscreteProbability />
        break
    case "/problem/le":
      component = <LinearEquation />
      break
    case "/problem/sd":
      component = <SamplingDistribution />
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