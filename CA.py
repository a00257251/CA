from flask import Flask, make_response
from flask.ext.mysql import MySQL
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, json

from flask import Flask, Response, redirect, url_for, request, session, abort
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user
from json import dumps
mysql = MySQL()
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'twitter'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

items_list = [];

class User(UserMixin):

    def __init__(self, id):
        self.id = id


    def __repr__(self):
        return "%d/%s/%s" % (self.id)

    @property
    def username(self):
        user = self.get_user()
        return user['username']

    @property
    def is_admin(self):
        user = self.get_user()
        return user['is_admin']

    def get_user(self):
        return find_user_by_id(self.id)

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == 'POST':
        username = request.form['inputName']
        password = request.form['inputPassword']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_login', (username, password))
        data = cursor.fetchall()
        items_list = [];
        for item in data:
            i = {
                'id': item[0],
                'username': item[1],
                'password': item[2],
            }
            items_list.append(i)
        userjson = dumps(items_list)
        print(userjson)
        for i in items_list:
            id = i['id']
            uusername = i['username']

            print(id)
        if (items_list == []):
            return Response('<p>Wrong user</p>')
        else:
            resp = make_response((redirect('/loginDash')))
            resp.set_cookie('userID', uusername)
            user = User(id)
            login_user(user)
            return resp
    else:
        return render_template('login.html')

userjson = dumps(items_list)
def find_user_by_id(user_id):
    for _user in items_list:
        if _user['id'] == user_id:
            return _user
    return None

def find_user_by_username(username):
    for _user in items_list:
        if _user['username'] == username:
            return _user
    return None


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    resp = make_response((redirect('/')))
    resp.set_cookie('userID', "")
    return resp


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    user = find_user_by_id(userid)
    return User(userid)


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:

            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser', (_name, _email, _password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        return render_template('/')






@app.route('/' , methods=['GET'])
def hello_world():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run()
