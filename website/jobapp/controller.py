from .models import Job
from .services import APIConnection

def get_all_jobs():
    jobs = APIConnection.get_all_jobs()
    return jobs

def create_user(data):

    # Création d'un dictionnaire avec les données du formulaire
    user_data = {
        "name": data.get("name"),
        "location": data.get("location"),
        "job": data.get("job"),
        "keyword": []
    }

    # Ajout des mots clés dans la liste
    for keyword in data.getlist("keyword"):
        print(keyword)
        user_data["keyword"].append(keyword)

    print(user_data)

    APIConnection.post_user(user_data)