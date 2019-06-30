from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("sign_in_form.html")

@app.route("/", methods=["POST"])

def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    # User name validation #
    if username == "":
        username_error = "Please enter a username."

    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must contain between 3 and 20 characters."
        username = ""
    
    elif " " in username:
        username_error = "Username cannot contain any spaces."

    # Validate password #
    if password == "":
        password_error = "Please enter a valid password."
    
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must contain between 3 and 20 characters."
        password = ""
    
    elif " " in password:
        password_error = "Password must not contain spaces."
        password = ""
    
    # Password verification #
    if verify == "":
        verify_error = "Please validate your password."
    
    elif verify != password:
        verify_error = "Passwords do not mach. Please re-enter password."
        verify = ""
    
    # Validate Email #
    arroba = email.count("@")
    punto = email.count(".")

    if arroba != 1 or punto != 1:
        email_error = "Please add a valid email address."

    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return render_template("welcome.html", username = username)
    else: return render_template("sign_in_form.html",
        username = username,
        username_error = username_error,
        password_error = password_error,
        verify = verify,
        verify_error = verify_error,
        email = email,
        email_error = email_error
        )

app.run()