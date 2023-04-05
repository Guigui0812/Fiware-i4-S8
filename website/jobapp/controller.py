from .models import Job
from .services import APIConnection

def get_all_jobs():
    jobs = APIConnection.get_all_jobs()
    return jobs