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
                "job": user.get("job", {}),
                "location": user.get("location", {}),
                "keyword": user.get("keyword", {}),
            }
            user_researches.append(user_research)

        return user_researches


