from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    a = 10
    b = 20
    c = a + b 
    return f"The result is  : {a + b}"


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=9000, debug=True)