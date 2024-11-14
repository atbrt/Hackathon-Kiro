import numpy as np
from fichiersjson import *
def invert_permutation(p):
    """retourne l'inverse de la permutation p
    """
    p = np.asanyarray(p) # in case p is a tuple, etc.
    p=p-1
    s = np.empty_like(p)
    s[p] = np.arange(p.size)
    s=s+1
    return s

def tau(t,delta,n):
    tau_arr=np.arange(1,n+1).tolist()
    delta_t=min(delta,n-t)
    i=tau_arr.pop(t+delta_t-1)
    tau_arr.insert(t-1,i)
    return tau_arr

def composition(permu1,permu2):
    #renvoi permu1 rond permu 2
    return np.array(permu1)[np.array(permu2)-1]

def indices_twopaint(dico, l):
    #dico = le data loader par le json
    #l la permutation
    ensemble=[]
    for k in range(len(dico["vehicles"])):
        if dico["vehicles"][k]["type"]=="two-tone":
            ensemble.append(l.index(dico["vehicles"][k]["id"]))
    return np.array(ensemble)+1

def paint_exit(data,sigma):
    delta=data["parameters"]["two_tone_delta"]
    n=len(sigma)
    sigma_exit=invert_permutation(sigma)
    
    t_u_list=np.sort(indices_twopaint(data,sigma))
    u_list= np.array(sigma)[t_u_list-1]
    u_list=u_list.tolist()
    
    while u_list != []:
        u=u_list.pop(0)
        t_u=(sigma_exit)[u-1]
        tau_u=tau(t_u,delta,n)
        sigma_exit=composition(tau_u,sigma_exit)
        
    return invert_permutation(sigma_exit)
