from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True  #Display runtime errors


userform = """
    <!doctype html>
    <html>
        <style>
            .error {{ color: red; }}
        </style>
        <h1>User-Signup</h1>
        <body>
                <form method='POST'>
                    <label>Username: 
                        <input name="user-name" type="text" value="" />
                    </label>
                    <span class="error">{username_error}</span>
                    <br>
                    <label>Password:     
                        <input name="user-password" type="password" />
                    </label>
                    <span class="error">{password_error}</span>
                    <br>
                    <label>Verify Password:      
                        <input name="verify-password" type="password" />
                    </label>
                    <span class="error">{verify_error}</span>
                    <br>
                    
                    <label>Email (optional):
                        <input name="user-email" type="text" value=""/>
                    </label>
                    <span class="error">{email_error}</span>
                    <br>
                    <input type="submit" />   
                </form>
        </body>
    </html>
    """

@app.route('/')
def display_time_form():
    return userform.format(username_error ='', password_error='',
        verify_error='', email_error='')

@app.route('/', methods=['POST'])
def validate_time():
    
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
        username_error = "Please fill out username box above."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Your username can not have less 3 characters or more than 20 characters."
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
        username = ""

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
        verify = ""
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
        return userform.format(
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

'''
email needs to be optional
3. For the username and email fields, you should preserve what the user typed, so they don't have
to retype it. With the password fields, you should clear them, for security reasons.
4. Use templates (one for the index/home page and one for the welcome page) to render the HTML for your web app.
'''