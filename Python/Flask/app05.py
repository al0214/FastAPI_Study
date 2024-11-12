from flask import Flask, url_for
app = Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)