from flask import Flask, jsonify, render_template
import random
import time

app = Flask(__name__)

data = {
    "moisture": 50,
    "temperature": 30,
    "humidity": 60
}

def generate_data():
    data["moisture"] = random.randint(20, 80)
    data["temperature"] = random.randint(25, 35)
    data["humidity"] = random.randint(40, 80)

@app.route('/')
def home():
    return "Smart Farm System Running"

@app.route('/data')
def get_data():
    generate_data()
    status = "Soil OK"

    if data["moisture"] < 30:
        status = "Irrigation needed"

    return jsonify({
        "data": data,
        "status": status
    })

@app.route('/dashboard')
def dashboard():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)