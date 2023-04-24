import React, {useState, useEffect} from "react";

export const LinearEquation = () => {
    const [problem, setProblem] = useState('');
    const [answer, setAnswer] = useState('');
    const [userAnswer, setUserAnswer] = useState('');

    useEffect(() => {
        fetch('http://localhost:5000/problem')
          .then(response => response.json())
          .then(data => {
            setProblem(data.problem);
            setAnswer(data.answer);
        });
    }, []);



    const checkAnswer = (e) => {
        e.preventDefault()
        console.log(userAnswer,answer);
        if (userAnswer == answer) {
            alert("Correct!");
        } else {
            alert("Incorrect!");
        }
    }

    return (
        <div className="problem-container">
            <h1 className="problemTitle">Problem</h1>
            <h2 className="problemText">{problem}</h2>
            <form className="math-problem" onSubmit={checkAnswer}>
                <input value = {userAnswer} onChange={(e)=> setUserAnswer(e.target.value)} type="number" placeholder="answer" id = "answer" name = "answer"/>
                <button type="submit" className="prob-check-button">Submit</button>
            </form>

        </div>
    )

}