

import json 

def ouvrir(fichier):
    with open(fichier, 'r') as f:
        data=json.load(f)
    return data
from permutation import invert_permutation

def resequencing_cost(sigma1, sigma2, c_s, delta_s):
    """
    sigma1: permutation de sortie du shop 
    sigma1: permutation d'entrée du shop suivant
    c_s: paramètre de resequencing
    """
    n = len(sigma1)
    S = 0
    sigma1inv = invert_permutation(sigma1)
    sigma2inv = invert_permutation(sigma2)
    for v in range(0, n):
        S += c_s*max(0, sigma1inv[v] - delta_s - sigma2inv[v])
    return S


def lot_change_cost(sigma0, sigma1, partition, cost):
    n = len(sigma0)
    S = 0
    def same_lot(i,j,partition):
        """
        Une partition est une liste de liste avec les éléments
        """
        for liste in partition:
            if i in liste:
                if j in liste:
                    return True
        return False
    for v in range(1, n-1):
        if not same_lot(sigma0[v],sigma0[v+1], partition):
            S+= cost
    return S

#a = lot_change_cost([1,2,3,4,5], None, [[1,2], [3,4,5]], 1)
#print(a)

def rolling_window_cost(sigma0, sigma1, V_r, cost, w_r, M_r):
    n = len(sigma0)
    S = 0

    for v in range(1, n-w_r+2):
        S2 = -M_r
        for a in range(v, v+w_r-1):
            if sigma0[a] in V_r:
                S2 += 1
        S+= (max(0, S2)**2)*cost
    return S

#a = rolling_window_cost([1,2,3,4,5], None, [1,2,3], 1, 1, 3)
#print(a)

def size_contraint(sigma0, sigma1, V_b, m_b, M_b, cost):
    n = len(sigma0)
    S = 0
    for i in range(0, n-1):
        for j in range(i, n):
            c = True
            if (i >= 2 and sigma0[i-1] not in V_b):
                for b in range(i, j+1):
                    if sigma0[b] not in V_b:
                        c = False
                if c:
                    if (j <= n-2 and sigma0[j+1] not in V_b):
                        S += cost* (max(0, m_b - j + i -1, j-i+1 - M_b))**2
    return S


def sommecout(fichier, sigma1, sigma2, k):
    somme=0
    dico=ouvrir(fichier)
    shop=dico["shops"][k]
    
    for contrainte in dico["constraints"]:
        if contrainte["shop"]==shop["name"]:
                if contrainte["type"]=="lot_change":
                    partition=contrainte["partition"]
                    cout=contrainte["cost"]
                    somme+=lot_change_cost(sigma1, sigma2, partition, cout)
                    
                elif contrainte["type"]=="batch_size":
                    vehic=contrainte["vehicles"]
                    cost=contrainte["cost"]
                    mini=contrainte["min_vehicles"]
                    maxi=contrainte["max_vehicles"]
                    somme+=size_contraint(sigma1, sigma2, vehic, mini, maxi, cost)
                    
                else:
                    vehic2=contrainte["vehicles"]
                    cost=contrainte["cost"]
                    w=contrainte["window_size"]
                    m=contrainte["max_vehicles"]
                    somme+=rolling_window_cost(sigma1, sigma2, vehic2, cost, w, m)
                    
    return somme
    

def coutsequencing(fichier, sigma1, sigma2, k):
    somme=0
    dico=ouvrir(fichier)
   
    shop=dico["shops"][k]
    c_s=dico["parameters"]["resequencing_cost"]
    delta_s=shop["resequencing_lag"]
    somme+=int(resequencing_cost(sigma1, sigma2, c_s, delta_s))
    return somme

def sortiedico(fichier, tableau):
    dico=ouvrir(fichier)
    dicos={}
    for i in range(len(tableau)):
        nouveau={"entry":tableau[i][0], "exit":tableau[i][1]}
        nom=dico["shops"][i]["name"]
        dicos[nom]=nouveau
        
    return dicos

def sortiefinale(fichier, tableau, nom_sortie):
    dico=sortiedico(fichier, tableau)
   
    with open(nom_sortie, 'w') as f:
        json.dump(dico, f)









