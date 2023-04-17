from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import utils
import json

# Create a class to scrap the research result from indeed
class IndeedJobsScraper():
    def __init__(self, titre, lieu, type_contrat, limit):
        self.titre = titre.capitalize()
        self.lieu = lieu.capitalize()
        self.type_contrat = ",".join([keyword for keyword in type_contrat if keyword]) # Convertir la liste en chaîne de caractères avec "," comme séparateur, en excluant les éléments vides
        self.page = 0
        self.limit = limit * 0
        self.scrap = True
        self.url = "https://fr.indeed.com/emplois?q=" + titre + "&l=" + lieu + "&sc=0kf%3Ajt%28" + type_contrat + "%29%3B&start=" + str(self.page)
        self.url = self.url.replace(' ', '+')
        self.jobs_list = []

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

    def run_scrap_research_result(self):

        while self.scrap:

            if (self.scrap_result_page() == True) and (self.page <= self.limit):
                self.page += 10 # les pages sur indeed sont de 10 en 10
            else:
                self.scrap = False
                self.driver.quit()

    def store_jobs(self):

        # Do : check if the job is already in the database 

        for job in self.jobs_list:
            utils.DataInsertion.insert_data(job, "http://localhost:1026/v2/entities", {"Content-Type": "application/json"})

    def scrap_job_details(self, details_url, cpt):
 
        self.driver.get(details_url)

        # Wait for the page to load
        self.driver.implicitly_wait(5)

        # Get the job title
        h1 = self.driver.find_element(By.CSS_SELECTOR, "h1.jobsearch-JobInfoHeader-title")
        job_title = h1.text

        # Get the job location
        div = self.driver.find_element(By.CSS_SELECTOR, "div.eu4oa1w0")
        job_location = div.text

        # Get the job description
        div = self.driver.find_element(By.CSS_SELECTOR, "div.jobsearch-jobDescriptionText")
        job_description = div.text

        self.jobs_list[cpt - 1]["title"] = utils.DataCleaner.clean_data(job_title)
        self.jobs_list[cpt - 1]["location"] = utils.DataCleaner.clean_data(job_location)
        self.jobs_list[cpt - 1]["description"] = utils.DataCleaner.clean_data(job_description)

    def scrap_result_page(self):

        self.driver.get(self.url)
        print(self.url)

        # Wait for the page to load
        self.driver.implicitly_wait(5)

        # Get the job title and the url
        elements = self.driver.find_elements(By.CSS_SELECTOR, "a.jcs-JobTitle")

        for element in elements:
                
            job = {
                "id": element.get_attribute("id"),
                "url": element.get_attribute("href")
            }

            self.jobs_list.append(job)

        # get span that contains the job publication date
        elements = self.driver.find_elements(By.CSS_SELECTOR, "span.date")
        
        for element in elements:
            self.jobs_list[elements.index(element)]["date"] = element.text

        # get span that contains the company name
        elements = self.driver.find_elements(By.CSS_SELECTOR, "span.companyName")

        for element in elements:
            self.jobs_list[elements.index(element)]["company"] = element.text

        cpt = 1

        # get the job details
        for job in self.jobs_list:
            self.scrap_job_details(job["url"], cpt)
            cpt += 1
            time.sleep(3)

# tant que il y a des utilisateurs dans la base
# on récupère les jobs qui correspondent à leur recherche
# on les stocke dans la base

#boucler sur tous les utilisateurs
# Obtenez les préférences des utilisateurs
users = utils.DataInfoUser.get_user_researches()
# Exemple d'utilisation
orion_url = "http://localhost:1026"
#utils.DataInfoUser.delete_all_jobs(orion_url)


for user in users:
    print(user)
    job_value = ", ".join(user["job"])  # Convert list to string
    location_value = user["location"]
    keyword_value = user["keyword"]

    print(job_value, location_value, keyword_value)

    if not job_value or not location_value:
        print("One of the fields is empty. Skipping this user.")
        continue
    job_scraper = IndeedJobsScraper(
        titre=job_value,
        lieu=location_value,
        type_contrat = "apprenticeship",
        limit=20  # You can change this value to determine the search results limit
    )
    job_scraper.run_scrap_research_result()
    print(job_scraper.jobs_list)
    job_scraper.store_jobs()


#pb limite pour tous les users 


