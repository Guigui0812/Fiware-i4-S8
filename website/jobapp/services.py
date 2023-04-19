from dotenv import load_dotenv
import os
import requests
import json
import openai

load_dotenv()
SECRET_KEY = os.getenv("OPENAI_KEY")
openai.api_key = SECRET_KEY

class APIConnection:

    @staticmethod
    def clean_data(data):

        if "%29" in data:
            data = data.replace("%29", ")")
        if "%28" in data:
            data = data.replace("%28", "(")
        if "%27" in data:
            data = data.replace("%27", "'")
        if "%22" in data:
            data = data.replace("%22", '"')
        if "%3B" in data:
            data = data.replace("%3B", ";")

        return data

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
                "description": APIConnection.clean_data(job["description"]["value"])
            }
            jobs_list.append(job_data)

        return jobs_list
    
    @staticmethod
    def user_to_datamodel(user_data):

        # Create the data model
        data = {
            "id": user_data["name"],
            "type": "User",
            "password": { "type": "String", "value": user_data["password"] },
            "location": { "type": "String", "value": user_data["location"] },
            "job": { "type": "Array", "value": user_data["job"] },
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

    @staticmethod
    def get_user(username):

        response = requests.get(url="http://localhost:1026/v2/entities/" + username)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    @staticmethod
    def get_user_jobs(keywords_researched, location_researched, job_researched):

        response = requests.get(url="http://localhost:1026/v2/entities?type=Job&limit=1000")
        all_jobs = response.json()
        

        jobs_list = []

        print(jobs_list)

        for job in all_jobs:
            job_data = {
                "id": job["id"],
                "title": APIConnection.clean_data(job["title"]["value"]),
                "company": job["company"]["value"],
                "location": job["location"]["value"],
                "date": job["date"]["value"],
                "description": APIConnection.clean_data(job["description"]["value"])
            }
            jobs_list.append(job_data)

        i = 0
        while i < len(jobs_list):
            job = jobs_list[i]
            job_ok = False

            # Check if the job title contains the job researched
            for title in job_researched:
                print(job.get("title"))

                titles = title.split(" ")#split s'il y a des espaces dans le titre
               
                flag_test = True
                
                for subtitle in titles: 
                    
                    print(subtitle)

                    if subtitle.lower() not in job.get("title").lower():
                        flag_test = False
                
                if flag_test : 
                    job_ok = True
                
            
            # Check if the job title contains the keyword researched
            for keyword in keywords_researched:
                if keyword in job.get("description").lower():
                    job_ok = True

            if job_ok == False:
                jobs_list.pop(i)
            else:
                i += 1

        print(jobs_list)

        return jobs_list
    
class OpenAIConnection:

    @staticmethod
    def generate_motivation_letter(job_description):

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "J'ai besoin que tu écrives la lettre de motivation qui correspond à ce job en respectant certaines contraintes : à chaque retour chariot tu écris </br></br> dans le texte. C'est très important pour la mise en forme. Tu me renvoies le texte de la lettre avec écrit dedans </br></br> à chaque fois que ça change de paragraphe. Tu dois toujours respecter le format d'une lettre de motivation. Tu mets un </br></br> dès le début, après l'objet de la lettre, après Madame Monsieur, après les paragraphes, après la formule de politesse, la signature et à la fin. Il le faut, c'est important, sans ça le texte n'est pas exploitable. \n\n"
                   + "La description du job c'est ça : " + job_description + "\n\n"}])   

        return completion['choices'][0]['message']['content']