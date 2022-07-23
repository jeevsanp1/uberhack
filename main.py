from flask import Flask,request,render_template,redirect
 

app = Flask(__name__)
 

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")
@app.route("/app", methods=['GET', 'POST'])
def main():
    return render_template("app.html")
 
# main driver function
if __name__ == '__main__':
        app.run()
