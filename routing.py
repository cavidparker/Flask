from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>This is the home page<h2>'
@app.route('/cavid')
def cavid():
    return '<h2><center> Cavid is good </h2></center>'

@app.route('/profile/<username>')
def username(username):
    return "Hi how are you %s" % username

@app.route('/post/<int:post_id>')
def postid(post_id):
    return "here is your ID NO %s" % post_id

if __name__ == "__main__":
    app.run()