from flask import Flask, render_template, request, url_for, redirect, jsonify
from bson.json_util import dumps
from .models import Job
from .controller import get_all_jobs, create_user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def get_all_jobs_route():
    jobs = get_all_jobs()
    return render_template('jobs.html', jobs=jobs)

@app.route('/users')
def fill_user_form():
    return render_template('users.html')

@app.route('/create_user', methods=['POST'])
def post_data():
    data = request.form
    create_user(data)
    return 'Formulaire soumis avec succès'