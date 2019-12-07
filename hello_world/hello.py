from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return("Hello World!")

@app.route('/welcome')
def welcome():
    return('Welcome to Flask')

@app.route('/hello/<name>')
def show_user_profile(name):
    return('Hello,%s' % name)

if __name__ == "__main__":
    app.run(debug = True)
