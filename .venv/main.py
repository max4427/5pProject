from flask import Flask, request

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(__name__)
users = {}
profiles = {}


@app.route('/sign_up', methods=["POST"])
def sign_up():
    new_user = {"first_name": request.form["first_name"], "last_name": request.form["last_name"],
                "password": request.form["password"], "phone": request.form["phone"],
                "username": request.form["username"]}

    if new_user["username"] in users:
        # user is already exists
        return f"The username {new_user['username']} is already in the system so check if you already have an account."

    users[new_user['username']] = new_user
    return app.send_static_file("login.html")


@app.route('/registration')
def registration():
    f = app.send_static_file("registration.html")
    # todo: inside the sign_up html page, you should pass the form information to a new registration endpoint
    return f

@app.route('/sign_in', methods=["POST"])
def sign_in():
    f = request.form
    username = request.form['username']
    password = request.form['password']
    if username not in users:
        # user does not exist
        return f"Username {username} does not exist, maybe you should sign up?"

    user: dict = users[username]
    user_pass = user.get("password")
    if password != user_pass:
        # incorrect password
        return f"Password is incorrect, please try again"

    return app.send_static_file("Home_page.html")


@app.route('/login')
def login():
    f = app.send_static_file("login.html")
    return f


@app.route('/home_page')
def home_page():
    f = app.send_static_file("Home_page.html")
    return f


@app.route('/personal_area')
def personal_area():
    f = app.send_static_file("personal_area.html")
    return f


@app.route('/create_new_profile', methods=["POST"])
def create_new_profile():
    print("")
    f = request.form
    return "got picture"


@app.route('/profiles')
def profiles():
    f = app.send_static_file("profiles.html")
    # First_Name = request.form["First name"]
    # Last_Name = request.form["Last name"]
    # ID = request.form["ID"]
    # Medicine = request.form["Medicine"]
    #
    # if ID in profiles:
    #     # The profile is already exists
    #     return f"check if the profile you entered is already exists"
    #
    # profiles["First_Name"] = First_Name
    # profiles["Last_Name"] = Last_Name
    # profiles["ID"] = ID
    # profiles["Medicine"] = Medicine
    return f

# todo: add endpoint for getting all of the information from the "add profile" form
# todo: create profile dictionary and add it to the global profiles dictionary

if __name__ == '__main__':
    app.run(port=5000)