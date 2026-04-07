from flask import Flask, request, jsonify
from agent import run_agent

app = Flask(__name__)

@app.route('/ai', methods=['POST'])
def ai():
    data = request.json
    prompt = data.get("prompt", "")

    result = run_agent(prompt)

    return jsonify({"result": result})

app.run(host="0.0.0.0", port=5000)