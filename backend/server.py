from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import time
from randomQuestionVar import generate_equation, solve_equation
from randomQuestionPictures import generateEquation, ImageAnswer

app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:3000'])

## Example api method
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/problem/le')
def random_question_le():
    return jsonify(generate_equation())

@app.route('/problem/crv')
def random_question_crv():
    return send_file(generateEquation("Continuous_Random_Variable"))

@app.route('/problem/dp')
def random_question_dp():
    return send_file(generateEquation("Discrete_Probability"))

@app.route('/problem/sd')
def random_question_sd():
    return send_file(generateEquation("Sampling_Distribution"))

@app.route('/answer/le', methods = ['POST'])
def get_answer_le():
    equation = request.json.get('problem/le')
    print(equation)
    answer = solve_equation(equation)
    print(answer)
    return jsonify(answer)

if __name__ == "__main__":
    app.run()