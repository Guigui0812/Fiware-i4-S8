import requests
import os
import time
import utils

# Class to insert data in the orion context broker
class DataInsertion:

    @staticmethod
    def job_to_datamodel(job_data):

        # Create the data model like the one in the csv_to_datamodel function
        data = {
            "id": job_data["id"],
            "type": "Job",
            "title": { "type": "String", "value": job_data["title"] },
            "company": { "type": "String", "value": job_data["company"] },
            "location": { "type": "String", "value": job_data["location"] },
            "date": { "type": "String", "value": job_data["date"] },
            "description": { "type": "String", "value": job_data["description"] }
        }

        return data

    @staticmethod
    def insert_data(data, url, headers):

        data = DataInsertion.job_to_datamodel(data)
        data = utils.DataCleaner.convert_to_json(data)
        response = requests.post(url, headers=headers, data=data)

        if response.status_code != 201:
            print(response.text)

        time.sleep(1)
