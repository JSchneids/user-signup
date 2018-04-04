from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True  #Display runtime errors

#User signup home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup():
    username = request.form["user-name"]
    password = request.form["user-password"]
    verify = request.form["verify-password"]
    email = request.form["user-email"]

    #Empty string for error messages
    username_error =''
    password_error=''
    verify_error=''
    email_error=''

    #Username 
    if username == "": 
        username_error = "Please fill out username box."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Your username can not have less 3 characters or more than 20 characters."
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
    #Password
    if password == "": 
        password_error = "Enter a password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long."
    elif " " in password:
        password_error = "Your password cannot contain any spaces."
    #Verify/Compare Password
    if verify == "" or verify != password: 
        verify_error = "Passwords do not match. Please try again."
    #Verify Email
    if email == "": 
        email_error = "Please enter a email."
    elif len(email) < 3 or len(email) > 20:
        email_error = "Password must be between 3 and 20 characters long."
    elif " " in email:
        email_error = "Your email cannot contain any spaces."
    elif "@" not in email:
        email_error = "Please input a valid email containing a @"
    elif "." not in email:
        email_error = "Please input a valid email containing a . period"
    #If no errors then redirect
    if not username_error and not password_error and not verify_error and not email_error:
        return  redirect('/welcome_page?username={0}'.format(username))   
    #If it has errors then it displays them on same page
    else:
        return render_template('index.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,
            email = email,
            email_error = email_error    
        )
#Redirect to welcome page
@app.route("/welcome_page")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username) 

app.run()