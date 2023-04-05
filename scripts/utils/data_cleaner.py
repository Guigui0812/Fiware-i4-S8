import re
import json

class DataCleaner:

    @staticmethod
    def clean_data(data):
        
        # Remove all the new line characters
        data = data.replace('\n', '')

        # Remove all the white spaces at the beginning and at the end of the data
        data = data.strip()

        # Remove all special characters
        data = data.replace('é', 'e')
        data = data.replace('è', 'e')
        data = data.replace('ê', 'e')
        data = data.replace('à', 'a')
        data = data.replace('â', 'a')
        data = data.replace('ô', 'o')
        data = data.replace('î', 'i')
        data = data.replace('ï', 'i')
        data = data.replace('ç', 'c')
        data = data.replace('ù', 'u')
        data = data.replace('û', 'u')
        data = data.replace('ä', 'a')
        data = data.replace('ë', 'e')
        data = data.replace('ï', 'i')
        data = data.replace('ö', 'o')
        data = data.replace('ü', 'u')
        data = data.replace('ÿ', 'y')
        data = data.replace('Ë', 'E')
        data = data.replace('Ï', 'I')
        data = data.replace('Ö', 'O')
        data = data.replace('Ü', 'U')   
        data = data.replace('Ÿ', 'Y')
        data = data.replace('À', 'A')
        data = data.replace('Â', 'A')
        data = data.replace('Æ', 'A')
        data = data.replace('Ç', 'C')
        data = data.replace('È', 'E')
        data = data.replace('É', 'E')
        data = data.replace('Ê', 'E')
        data = data.replace('et', ' ')
        data = data.replace('<', '%3C')
        data = data.replace('>', '%3E')
        data = data.replace('(', '%28')
        data = data.replace(')', '%29')
        data = data.replace(';', '%3B')
        data = data.replace('"', '%22')
        data = data.replace("'", '%27')
        data = data.replace('=','%3D')
        data = data.replace('\n', '')

        return data
    
    @staticmethod
    def convert_to_json(data):
        data = json.dumps(data, indent=4)
        return data