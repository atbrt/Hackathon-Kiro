import numpy as np

def invert_permutation(p):
    """Return an array s with which np.array_equal(arr[p][s], arr) is True.
    The array_like argument p must be some permutation of 0, 1, ..., len(p)-1.
    """
    p = np.asanyarray(p) # in case p is a tuple, etc.
    p=p-1
    s = np.empty_like(p)
    s[p] = np.arange(p.size)
    s=s+1
    return s

print(invert_permutation([5,4,1,3,2]))
