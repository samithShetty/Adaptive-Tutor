import React , {useState, useEffect} from "react"

function App() {
  const [time, setTime] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/time')
      .then(response => response.json())
      .then(data => setTime(data.time));
  }, []);
  
  return (
    <div>
      <h1>Current Time: {time}</h1>
    </div>
  )
}

export default App