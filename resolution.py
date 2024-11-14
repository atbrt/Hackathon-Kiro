import time
import random
from copy import *
from permutation import *
from fichiersjson import *
def permutation(i, j, l):
    a,b = l[i], l[j]
    l[j], l[i] = a,b

from cost import sommecout
from cost import coutsequencing

def resoudre(t1 ,t2 ,t3 ,n , fichier):
    #fichier = ""

    sigma = [i for i in range(n)]
    C = 0

    c = sommecout(fichier, sigma, None, 0)
    t = time.time()
    while time.time() - t< t1:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        permutation(a, b, sigma)
        cbis = sommecout(fichier, sigma, None, 0)
        if c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    C += c
    sigma0 = deepcopy(sigma)




    t = time.time()
    c = None
    while time.time() - t < t2:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        sigma1 = sigma.copy()
        permutation(a,b,sigma1)
        cbis = sommecout(fichier, sigma1, None, 1) + coutsequencing(fichier, sigma0, sigma1, 1)
        if c == None:
            c = cbis
        elif c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    C += C
    sigma1 = deepcopy(sigma)
    ###
    data=ouvrir(fichier)
    sigma = paint_exit(data,sigma)
    sigma2 = sigma.deepcopy()

    t = time.time()
    c = sommecout(fichier, sigma2, None, 2)
    while time.time() - t < t3:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        sigma3 = deepcopy(sigma)
        permutation(a,b,sigma2)
        cbis = sommecout(fichier, sigma3, None, 2) + coutsequencing(fichier, sigma2, sigma3, 2)
        if c == None:
            c = cbis
        elif c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    C += C
    sigma3 = deepcopy(sigma)


    sigma_list = [[sigma0, sigma0], [sigma1, sigma2], [sigma3, sigma3]]
    return (C, sigma_list)


    

print(resoudre(1,1,1,5,"tiny.json"))
