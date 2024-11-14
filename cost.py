#Cout s
from permutation import inverse_perm

def resequencing_cost(sigma1, sigma2, c_s, delta_s):
    """
    sigma1: permutation de sortie du shop 
    sigma1: permutation d'entrée du shop suivant
    c_s: paramètre de resequencing
    """
    n = len(sigma1)
    S = 0
    sigma1inv = inverse_perm(sigma1)
    sigma2inv = inverse_perm(sigma2)
    for v in range(1, n+1):
        S += c_s*max(0, sigma1inv[v] - delta_s - sigma2inv[v])
    return S

def lot_change_cost(sigma0, sigma1, partition_list, cost_list):
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

    for i in range(len(partition_list)):
        partition = partition_list[i]
        cost = cost_list[i]
        for v in range(1, n-1):
            if not same_lot(sigma0[v],sigma0[v+1], partition):
                S+= cost
    return S

def rolling_window_cost(sigma0, sigma1, V_rlist, cost_list, w_rlist, M_rlist):
    n = len(sigma0)
    S = 0
    number_constraint = len(cost_list)
    for i in range(number_constraint):
        w_r = w_rlist[i]
        V_r = V_rlist[i]
        M_r = M_rlist[i]
        c = cost_list[i]
        for v in range(1, n-w_r+2):
            S2 = -M_r
            for a in range(v, v+w_r-1):
                if sigma0[a] in V_r:
                    S2 += 1
            S+= (max(0, S2)**2)*c
    return S

def size_contraint(sigma0, sigma1, V_blist, m_blist, M_blist, cost_list):
    n = len(sigma0)
    S = 0
    number_constraint = len(V_blist)
    for a in range(number_constraint):
        V_b = V_blist[a]
        cost = cost_list[a]
        m_b = m_blist[a]
        M_b = M_blist[a]
        for i in range(1, n):
            for j in range(i, n+1):
                if (i >= 2 and sigma0[i-1] not in V_b):
                    c = True
                    for b in range(i, j+1):
                        if sigma0[b] not in V_b:
                            c = False
                    if c:
                        if (j <= n-1 and sigma0[j+1] not in V_b):
                            S += cost* (max(0, m_b - j + i -1, j-i+1 - M_b))**2
    return S








