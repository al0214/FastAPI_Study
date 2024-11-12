from flask import Flask, url_for
app = Flask(__name__)

@app.route("/user/<username>")
def show_user_profile(username:str):
    return f'User {username}'

@app.route('/post/<year>/<month>/<day>')
def show_post(year:str, month:str, day:str):
    return f'Post for {year}/{month}/{day}'

@app.route('/')
def index():
    user_url = url_for('show_user_profile', username='johndoe')
    post_url = url_for('show_post', year = '2023', month = '04', day = '01')
    
    return f'User URL : {user_url}<br>Post URL : {post_url}'
    
if __name__ == '__main__':
    app.run(debug=True)