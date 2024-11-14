import time
import random

def permutation(i, j, l):
    a,b = l[i], l[j]
    l[j], l[i] = a,b

def cout(shop, i):
    pass

def cout_re(shop, i):
    pass



def resoudre(t1 ,t2 ,t3 ,n , fichier):
    fichier = ""

    sigma = [i for i in range(n)]
    C = 0

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
    C += c
    sigma0 = sigma.deepcopy()




    t = time.time()
    c = None
    while time.time() < t2:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        sigma1 = sigma.copy()
        permutation(a,b,sigma1)
        cbis = cout(fichier, sigma, None, 1) + cout_re(fichier, sigma, sigma1, 1)
        if c == None:
            c = cbis
        elif c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    C += C
    sigma1 = sigma.deepcopy()

    ###
    sigma = paint_transition(sigma)
    sigma2 = sigma.deepcopy()

    t = time.time()
    c = cout(fichier, sigma2, None, 2)
    while time.time() < t3:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        sigma3 = sigma.copy()
        permutation(a,b,sigma2)
        cbis = cout(fichier, sigma3, None, 0) + cout_re(fichier, sigma, sigma3, 0)
        if c == None:
            c = cbis
        elif c < cbis:
            permutation(a, b, sigma)
        else:
            c = cbis
    C += C
    sigma3 = sigma.deepcopy()


    sigma_list = [[sigma0, sigma0], [sigma1, sigma2], [sigma3, sigma3]]
    return (C, sigma_list)


    

