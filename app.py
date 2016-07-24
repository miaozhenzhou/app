from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/mika")
def mika():
    return "mika"

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>'%name

if __name__ == '__main__':
    app.run(debug=True)
