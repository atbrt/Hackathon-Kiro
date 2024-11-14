import json 
from test_permutation import indices_twopaint
def ouvrir(fichier):
    with open(fichier, 'r') as f:
        data=json.load(f)
    return data
    

def creerjson(data):
    with open('fichier résultats.json', 'w'):
        json.dump(data)

