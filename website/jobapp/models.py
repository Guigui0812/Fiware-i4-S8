class Job:
    def __init__(self, job_id, job_title, job_description, job_location, job_posted_date, job_company):
        self.id = job_id
        self.title = job_title
        self.description = job_description
        self.location = job_location
        self.date = job_posted_date
        self.company = job_company