import datetime
import json
import os
import sqlite3
import uuid

import bcrypt
from flask import Flask, g, request, redirect
import jwt

app = Flask("loginapp")

# base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
JWT_SECRET = '6XNTJJLXKJE-T3n3negM7ELGdY8lvUJbfV36QD6PWRE='

class User:
    def __init__(self, email, saved_surveys):
        self.email = email
        self.saved_surveys = saved_surveys

# days
SESSION_TIME = 30

SELECT_PASSWORD = "SELECT password FROM users WHERE email = ?"
INSERT_USER = "INSERT INTO users VALUES (?, ?)"

# error codes
EMAIL_ALREADY_EXISTS = 1
NOT_LOGGED_IN = 2
INVALID_CREDENTIALS = 3

if not os.path.exists("users.db"):
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    cursor.execute("""
        INSERT INTO users VALUES(
            'test@example.com',
            '$2b$12$Tk1B6g4JNIY1mIDkmdzOKeJO3aigf4zx.Y1KB7htIGTRbzdS2SxiC'
        )
    """)
    conn.commit()
else:
    conn = sqlite3.connect('users.db', check_same_thread=False)
    cursor = conn.cursor()


def create_jwt(user_id):
    payload = {
        "sub": user_id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def verify_jwt(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def get_user(email):
    return User(email, ['corn field', 'secret base'])
    
@app.before_request
def before_request():
    g.user = None
    session_id = request.cookies.get("session_id")
    if session_id:
        payload = verify_jwt(session_id)
        if payload:
            g.user = get_user(payload["sub"])
        
        
@app.route("/")
def index():
    if g.user is not None:
        content = ""
        for survey in g.user.saved_surveys:
            content += survey + "<br />"

        return """
            <html>
                <head></head>
                <body>
                    <input type="submit" id="logoutBtn" value="Log Out" />
                    <script type="text/javascript">
                        function $(id) {
                            return document.getElementById(id);
                        }
                        $("logoutBtn").addEventListener('click', function(e) {
                            let params = {
                                session_id: getCookie(session_id)
                            },
                            query = new URLSearchParams(params).toString();
                            
                            fetch("/logout?" + query).then(r => {
                                return r.json();
                            }).then(data => {
                                //TODO delete cookie
                                //TODO refresh page
                            });
                        });
                    </script>
                </body>
            </html>
        """
    else:
        return """
            <html>
                <head></head>
                <body>
                    <input type="text" name="email" id="email" />
                    <input type="password" name="password" id="password" />
                    <input type="submit" id="loginBtn" value="Log In" />
                    <br />
                    <br />
                    <input type="text" name="signUpEmail" id="signUpEmail" />
                    <input type="password" name="signUpPass" id="signUpPass" />
                    <input type="submit" id="signUpBtn" value="Sign Up" />
                    
                    <script type="text/javascript">
                        function $(id) {
                            return document.getElementById(id);
                        }
                        $("loginBtn").addEventListener('click', function(e) {
                            let params = {
                                email: $("email").value,
                                password: $("password").value
                            },
                            query = new URLSearchParams(params).toString();
                            
                            fetch("/login?" + query).then(r => {
                                return r.json();
                            }).then(data => {
                                let cookie = "session_id=" + data.session_id;
                                cookie += "; max-age=60;path=/" 
                                document.cookie = cookie;
                            });
                        });
                        $("signUpBtn").addEventListener('click', function(e) {
                            let params = {
                                email: $("signUpEmail").value,
                                password: $("signUpPass").value
                            },
                            query = new URLSearchParams(params).toString();
                            
                            fetch("/signup?" + query).then(r => {
                                return r.json();
                            }).then(data => {

                            });
                        });
                    </script>
                </body>
            </html>
        """

@app.route("/login")
def login():

    email = request.args.get('email')
    password = request.args.get('password')
    stored_password, = cursor.execute(SELECT_PASSWORD, (email,)).fetchone()
    
    if bcrypt.checkpw(password.encode('utf8'), stored_password.encode('utf8')):
        return json.dumps({
            "error": False,
            'session_id': create_jwt(email),
            "surveys": get_user(email).saved_surveys
        })
    else:
        return json.dumps({"error": True, "error_code": INVALID_CREDENTIALS})

@app.route("/signup")
def signup():
    try:
        email = request.args.get('email')
        password = request.args.get('password')
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        cursor.execute(INSERT_USER, (email, hashed_password))

    except sqlite3.IntegrityError:
        return json.dumps({"error": True, "error_code": EMAIL_ALREADY_EXISTS})
    
    return json.dumps({
        "error": False,
        "session_id": create_jwt(email)
    })

# TODO there is no server side logout logic, simply expire the cookie and
# cleanup the client UI

##@app.route("/logout")
##def logout():
##    session_id = request.cookies.get("session_id")
##    if session_id and session_id in sessions:
##        del sessions[session_id]
##        return json.dumps({"error": False})
##    
##    return json.dumps({"error": True, "error_code": NOT_LOGGED_IN})

if __name__ == "__main__":
    app.run(debug=True)
