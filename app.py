from flask import Flask, render_template
from flask import request

import json

app = Flask(__name__)




@app.route('/',  methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    return msg

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)