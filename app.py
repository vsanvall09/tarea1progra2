from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hola a todos"


if __name__ == "_main_":
    app.run(debug=True)
