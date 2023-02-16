from flask import Flask
from flask_cors import CORS
import time

app = Flask(__name__)
cors = CORS(app)

## Example api method
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == "__main__":
    app.run()