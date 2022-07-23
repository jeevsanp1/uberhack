from flask import Flask,request,render_template,redirect,url_for,session
app = Flask(__name__)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
@app.route("/app", methods=['GET', 'POST'])
def home():
    return render_template("app.html")


if __name__ == '__main__':
    app.run(app, debug=True)