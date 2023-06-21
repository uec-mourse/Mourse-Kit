from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>これが見えたらサーバは無事に起動しています</p>"

@app.route("/echo", methods=["POST"])
def echo():
    text = request.json["data"]
    return text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)