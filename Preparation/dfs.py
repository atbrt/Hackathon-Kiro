import time


def neighbor_test(l):
    voisins = []
    for i in range(5):
        voisins.append(l + [i])
    return voisins

def score_test(l):
    if len(l) == 5:
        return sum(l)
    else:
        return -1



def dfs(initial_state, neighbor, score, max_time):
    """
    initial_state: 
    point de départ initial du graphe

    neighbor: 
    fonction prenant en argument un noeud du graphe et renvoyant la liste de ses voisins

    score: 
    fonction de score. 
    Renvoi -1 si le noeud du graphe donné en argument n'est pas une réponse valable.
    Sinon, renvoi la valeur du score.

    time:
    temps max que l'on donne à l'algo pour tourner. 
    Au bout de ce temps il renverra la meilleure solution trouvée.
    """

    best_score = None
    solution_best_score = None
    a_explorer = [initial_state]
    n = 0
    deja_vu = []
    t = time.time()


    while n < len(a_explorer) and (time.time()-t) < max_time:
        noeud = a_explorer[n]
        s = score(noeud)
        if s != -1:
            if best_score == None:
                best_score = s
                solution_best_score = noeud
            elif s < best_score:
                best_score = s
                solution_best_score = noeud
        else:
            voisins = neighbor(noeud)
            nouveau = []
            for noeud_voisin in voisins:
                if voisins not in a_explorer:
                    nouveau.append(noeud_voisin)
            a_explorer =  a_explorer[:n+1] + nouveau + a_explorer[n+1:]
        n += 1
    return best_score, solution_best_score


d = dfs(initial_state = [], neighbor = neighbor_test, score = score_test, max_time = 100)
print(d)
