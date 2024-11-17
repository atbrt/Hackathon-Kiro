import json 

def ouvrir(fichier):
    with open(fichier, 'r') as f:
        data=json.load(f)
    return data
    

def creerjson(data):
    with open('fichier résultats.json', 'w'):
        json.dump(data)

