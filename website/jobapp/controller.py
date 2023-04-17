from .models import Job, User
from .services import APIConnection
from werkzeug.security import generate_password_hash, check_password_hash

def get_all_jobs():
    jobs = APIConnection.get_all_jobs()
    return jobs

def get_jobs(username):

    data = APIConnection.get_user(username)

    user_data = {
        "name": data["id"],
        "password": data["password"]["value"],
        "location": data["location"]["value"],
        "job": data["job"]["value"],
        "keyword": data["keyword"]["value"]
    }

    user = User(user_data["name"], user_data["location"], user_data["job"], user_data["keyword"], user_data["password"])

    jobs = APIConnection.get_user_jobs(user.keywords, user.location, user.job)

    return jobs

def create_user(data):

    # Création d'un dictionnaire avec les données du formulaire
    user_data = {
        "name": data.get("name"),
        "password": generate_password_hash(data.get("password")),
        "location": data.get("location"),
        "job": [],
        "keyword": []
    }

    # Ajout des métiers dans la liste
    for job in data.getlist("job"):
        print(job)
        user_data["job"].append(job)

    # Ajout des mots clés dans la liste
    for keyword in data.getlist("keyword"):
        print(keyword)
        user_data["keyword"].append(keyword)

    print(user_data)

    APIConnection.post_user(user_data)

def check_user(username, password):
    data = APIConnection.get_user(username)

    if data is None:
        return False
    else:

        print(data)

        user_data = {
            "name": data["id"],
            "password": data["password"]["value"],
            "location": data["location"]["value"],
            "job": data["job"]["value"],
            "keyword": data["keyword"]["value"]
        }

        user = User(user_data["name"], user_data["location"], user_data["job"], user_data["keyword"], user_data["password"])

        if check_password_hash(user.password, password):
            return True
        else:
            return False