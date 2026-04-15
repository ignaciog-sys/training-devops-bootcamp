from flask import Flask, request, jsonify
import json

data = None
app = Flask(__name__)

@app.route("/granada")
def granada():
    return jsonify(data), 200

if __name__ == "__main__":
    data = json.load(open("./bd.json"))
    app.run(port=5000)

