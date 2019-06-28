from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("sign_in_form.html")

@app.route("/", methods=["POST"])
def welcome():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]


    
    return render_template("welcome.html", username=username)

app.run()