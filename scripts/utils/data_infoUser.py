import requests
import os
import time
import utils

class DataInfoUser:
    # ...
    @staticmethod
    def get_user_researches():
        # Remplacez cette URL par l'URL de l'entité utilisateur correspondante
        url = "http://localhost:1026/v2/entities?type=User"
        response = requests.get(url)
        users = response.json()

        print("Response:", response.text)
        print("Type of users:", type(users))

        user_researches = []
        for user in users:
            user_research = {
                "id": user.get("id"),
                "type": "User",
                "job": user.get("job", {}).get("value", ""),
                "location": user.get("location", {}).get("value", ""),
                "keyword": user.get("keyword", {}).get("value", []),
            }
            user_researches.append(user_research)

        return user_researches

    @staticmethod
    def delete_all_jobs(orion_url):
        headers = {
        "Accept": "application/json"
        }

        # Récupérer la liste de tous les jobs
        response = requests.get(f"{orion_url}/v2/entities?type=Job", headers=headers)
        jobs = response.json()

        # Supprimer chaque job de la base de données
        for job in jobs:
            job_id = job["id"]
            print(f"Suppression du job {job_id}...")
            response = requests.delete(f"{orion_url}/v2/entities/{job_id}", headers=headers)

            if response.status_code == 204:
                print(f"Job {job_id} supprimé avec succès.")
            else:
                print(f"Échec de la suppression du job {job_id}. Code d'état: {response.status_code}. Message: {response.text}")




