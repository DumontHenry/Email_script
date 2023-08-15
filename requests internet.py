import requests
import json

# Request and process programmation.txt
response = requests.get('https://codeavecjonathan.com/res/programmation.txt')
if response.status_code == 200:
    response.encoding = "utf-8"
    if response.text:  # Check if the response has content
        print(response.text)
        try:
            pizza = json.loads(response.text)
            print("Nombre de pizzas :", len(pizza))
        except json.JSONDecodeError as e:
            print("Erreur de décodage JSON:", str(e))
    else:
        print("La réponse est vide.")
else:
    print("ERREUR code:", response.status_code)

# Request and process pizzas1.json
response = requests.get('https://codeavecjonathan.com/res/pizzas1.json')
if response.status_code == 200:
    response.encoding = "utf-8"
    if response.text:
        print(response.text)
        try:
            pizza = json.loads(response.text)
            print("Nombre de pizzas :", len(pizza))
        except json.JSONDecodeError as e:
            print("Erreur de décodage JSON:", str(e))
    else:
        print("La réponse est vide.")
else:
    print("ERREUR code:", response.status_code)

# Request and print the content of exemple.html
response = requests.get('https://codeavecjonathan.com/res/exemple.html')
if response.status_code == 200:
    response.encoding = "utf-8"
    if response.text:
        print(response.text)
    else:
        print("La réponse est vide.")
else:
    print("ERREUR code:", response.status_code)

# Request and save papillon.jpg
response = requests.get('https://codeavecjonathan.com/res/papillon.jpg')
if response.status_code == 200:
    if response.content:
        with open("papillon.jpg", "wb") as f:
            f.write(response.content)
        print("Écriture terminée")
    else:
        print("La réponse est vide.")
else:
    print("ERREUR code:", response.status_code)
