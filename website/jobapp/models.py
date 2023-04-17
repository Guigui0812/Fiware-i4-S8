class Job:
    def __init__(self, job_id, job_title, job_description, job_location, job_posted_date, job_company):
        self.id = job_id
        self.title = job_title
        self.description = job_description
        self.location = job_location
        self.date = job_posted_date
        self.company = job_company

class User:
    def __init__(self, user_name, user_location, user_job, user_keywords, user_password):
        self.name = user_name
        self.password = user_password
        self.location = user_location
        self.job = user_job
        self.keywords = user_keywords