from flask import Flask, url_for
app = Flask(__name__)

@app.route("/home")
def index():
    return '홈페이지에 오신 것을 환영합니다!'

@app.route('/user/<username>')
def profile(username:str):
    return f'{username}님의 프로필 페이지 입니다. 홈으로 가기 : {url_for("index")}'

if __name__ == '__main__':
    app.run(debug=True)