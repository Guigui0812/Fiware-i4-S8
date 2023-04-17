from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from .models import Job
from .controller import create_user, check_user, get_jobs

app = Flask(__name__)
app.config.from_object('config')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the login page
@app.route('/login')
def login():
    return render_template('connexion.html')

# Request for login
@app.route('/login', methods=['POST'])
def login_post():
    username = request.json['username']
    password = request.json['password']
    
    if check_user(username, password):
        # Connexion successfull
        session['username'] = username
        print('Connexion réussie')
        return jsonify({'status': 'success', 'message': 'Connexion réussie'})
    else:
        # Connexion failed
        print('Nom d\'utilisateur ou mot de passe invalide')
        return jsonify({'status': 'error', 'message': 'Nom d\'utilisateur ou mot de passe invalide'})

# Route to display all jobs
@app.route('/jobs')
def get_jobs_route():
    username = session.get('username')
    jobs = get_jobs(username)
    return render_template('jobs.html', jobs=jobs)

# Route to register a new user
@app.route('/register')
def fill_user_form():
    return render_template('registration.html')

# Request POST for register a new user
@app.route('/register', methods=['POST'])
def post_data():
    data = request.form
    create_user(data)
    return 'Formulaire soumis avec succès'