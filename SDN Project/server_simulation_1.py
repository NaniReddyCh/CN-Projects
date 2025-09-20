# File: server_simulation.py
import time
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def respond():
    # Simulate response time
#    delay = random.choice([10, 20, 30])
    delay = 10
    time.sleep(delay / 1000)  # Convert to seconds
    return jsonify({"message": "Response from server", "delay": delay})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

