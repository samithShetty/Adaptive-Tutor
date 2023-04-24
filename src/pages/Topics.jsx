export const Topics = (props) => {
    return (
        <div className="topics-container">
            <h1 className='topicsTitle'>Topics</h1>
            <ul className="topics-list">
                <a href="/problem/le"><li>Linear Equations</li></a>
                <a href="/problem/crv"><li>Continuous Random Variable</li></a>
                <a href="/problem/dp"><li>Discrete Probability</li></a>
                <a href="/problem/sd"><li>Sampling Distribution</li></a>
            </ul>
        </div>
    )
}