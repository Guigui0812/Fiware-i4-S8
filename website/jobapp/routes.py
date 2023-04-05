from flask import Flask, render_template, request, url_for, redirect, jsonify
from bson.json_util import dumps
from .models import Job
from .controller import get_all_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jobs')
def get_all_jobs_route():
    jobs = get_all_jobs()
    return render_template('jobs.html', jobs=jobs)

    