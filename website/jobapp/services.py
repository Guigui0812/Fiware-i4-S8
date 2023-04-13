import requests
import json

class APIConnection:

    @staticmethod
    def get_all_jobs():
        response = requests.get(url="http://localhost:1026/v2/entities?type=Job")

        all_jobs = response.json()

        jobs_list = []

        for job in all_jobs:
            job_data = {
                "id": job["id"],
                "title": job["title"]["value"],
                "company": job["company"]["value"],
                "location": job["location"]["value"],
                "date": job["date"]["value"],
                "description": job["description"]["value"]
            }
            jobs_list.append(job_data)

        return jobs_list
    
    @staticmethod
    def user_to_datamodel(user_data):

        # Create the data model
        data = {
            "id": user_data["name"],
            "type": "User",
            "location": { "type": "String", "value": user_data["location"] },
            "job": { "type": "String", "value": user_data["job"] },
            "keyword": { "type": "Array", "value": user_data["keyword"] }
                      
        }

        return data
    
    @staticmethod
    def convert_to_json(data):
        data = json.dumps(data, indent=4)
        return data

    @staticmethod
    def post_user(data):

        data_to_post = APIConnection.user_to_datamodel(data)
        data_to_post = APIConnection.convert_to_json(data_to_post)
        print(data_to_post)
        response = requests.post(url="http://localhost:1026/v2/entities", headers={"Content-Type": "application/json"}, data=data_to_post)

        if response.status_code != 201:
            print(response.text)        