from flask import Flask, jsonify
from flask_cors import CORS

from genetic import generate_diet

app = Flask(__name__)
CORS(app)


@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("porong!")


@app.route("/get-diet", methods=["GET"])
def get_diet():
    return generate_diet()


if __name__ == "__main__":
    app.run()
