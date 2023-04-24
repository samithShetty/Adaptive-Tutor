from flask import Flask, jsonify, request
from flask_cors import CORS
import time
from randomQuestionVar import generate_equation, solve_equation

app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:3000'])

## Example api method
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/problem')
def random_question():
    return jsonify(generate_equation())

@app.route('/answer', methods = ['POST'])
def get_answer():
    equation = request.json.get('problem')
    print(equation)
    answer = solve_equation(equation)
    print(answer)
    return jsonify(answer)

if __name__ == "__main__":
    app.run()