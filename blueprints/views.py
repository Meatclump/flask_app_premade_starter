from flask import Blueprint, redirect, url_for, render_template, request, session
from datetime import date
import modules.db_interface as db_interface
year = date.today().year #sample variable to send to templates

views_bp = Blueprint(name='views', import_name=__name__, template_folder='templates')

@views_bp.route('/', methods=['GET'])
def index():
    """ Default landing route """

    # If username is set in session, show logged in home page
    if 'username' in session:
        return redirect(url_for('views.home'))

    # redirect to login page if user is not logged in
    return redirect(url_for('views.login'))

@views_bp.route('/home', methods=['GET'])
def home():
    """ A logged in user will end up here """
    
    # Check if user is logged in
    if 'username' in session:
        # The user is logged in. Show their home page
        username = session['username']
        return render_template('home.html', year=year, username=username)

    # This shouldn't happen, but better safe than sorry
    return redirect(url_for('views.index'))

@views_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ Route for user registration """

    # The register button has been pressed. Verify input and create user if valid
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error_list = []

        if db_interface.user_exists(username):
            error_list.append(f"The username '{username}' already exists. Please choose a different one.")
        
        if len(username) < 3:
            error_list.append(f"Your username may not be shorter than 3 characters.")
        
        if username.isalpha() is False:
            error_list.append(f"Your username may only use english alphabetic characters")
        
        if len(password) < 6:
            error_list.append(f"Your password must be at least 6 characters. Please choose a different one.")
        
        if len(error_list)  > 0:
            return render_template('register.html', err=error_list)

        db_interface.register_user_to_db(username, password)
        print(f"Registered new user: '{username}'")

        return redirect(url_for('views.index'))

    return render_template('register.html', year=year)

@views_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Route for logging in """
    error_list = []

    # Post request
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # If username and password matches database, set in session and redirect to index
        if db_interface.verify_user(username, password):
            session['username'] = username
        
            print(f"User logged in: '{username}'")
            return redirect(url_for('views.home'))
        else:
            error_list.append("Incorrect username or password.")
    
    # Get request
    return render_template('login.html', err=error_list)

@views_bp.route('/logout')
def logout():
    """ Route for logging out """
    if 'username' in session:
        username = session['username']
        print(f"User logging out: '{username}'")

    session.clear()
    return redirect(url_for('views.index'))

@views_bp.errorhandler(404)
def not_found(e):
    return render_template('404.html', year=year)