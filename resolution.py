import time
import random

def permutation(i, j, l):
    a,b = l[i], l[j]
    l[j], l[i] = a,b

def cout(shop, i):
    pass



def resoudre(t1 ,t2 ,t3 ,n , fichier):
    fichier = ""

    sigma = [i for i in range(n)]


    c = cout(fichier, sigma, None, 0)
    t = time.time()
    while time.time() < t1:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        permutation(a, b, sigma)
        cbis = cout(fichier, sigma, None, 0)
        if c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    
    sigma0 = sigma.deepcopy()

    

    t = time.time()

    

