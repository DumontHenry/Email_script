# JSON
# Data Structure
import json

# Personne
#   Name : str
#   age : int
#   amis : [str]

# Paul
# 25
# Sophia, Maria, Jack
# Pierre
# 18
# Eric, Marc
"""
personne = {"Name" : "Paul",
            "age": 25,
            "amis": ["Sophia", "Maria", "Jack"]}

# Sérialiser DATA -> TXT "" (json) dumps
# Désérialiser TXT (json) -> DATA  loads

person_json = json.dumps(personne)
print("JSON: " + person_json)

f = open("fichier_json.txt", "w")
f.write(person_json)
f.close()
"""

f = open("file_json.txt", "r")
donnees_json = f.read()
f.close()

personne = json.loads(donnees_json)
print("Name:" + personne["Name"])