import requests
import os
import time
import utils

# class to get data from the orion context broker
class DataInfoUser:
    # ...

    @staticmethod
    def get_user_researches():
        # Remplacez cette URL par l'URL de l'entité utilisateur correspondante
        url = "http://localhost:1026/v2/entities?type=User"
        headers = {"Fiware-Service": "i4-s8", "Fiware-ServicePath": "/"}
        response = requests.get(url, headers=headers)
        users = response.json()

        print("Response:", response.text)
        print("Type of users:", type(users))

        user_researches = []
        for user in users:
            user_research = {
                "id": user.get("id"),
                "type": "User",
                "title": {"type": "String", "value": user.get("title", {}).get("value")},
                "location": {"type": "String", "value": user.get("location", {}).get("value")},
                "type_contrat": {
                    "type": "String",
                    "value": user.get("type_contrat", {}).get("value"),
                },
                "limit": {"type": "Number", "value": user.get("limit", {}).get("value")},
            }
            user_researches.append(user_research)

        return user_researches

        
    

