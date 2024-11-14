import numpy as np

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
    i=tau_arr.pop(t-1)
    tau_arr.insert(t+delta_t,i)
    return tau_arr

def composition(permu1,permu2):
    #renvoi permu1 rond permu 2
    return np.array(permu1)[np.array(permu2)-1]