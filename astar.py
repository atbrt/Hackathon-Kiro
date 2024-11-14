def neighbor_test(l):
    voisins = [l-1, l+1]
    return voisins

from test import cookie

print(cookie())

def astar(initial_node, neighbor, target_node):
    """
    Attention:
    Ne marche que pour des graphes non orientés !
    Pour des graphes orientés, il faut changer la partie retour en arrière (complexité augemente un peu)

    initial_node: 
    noeud de départ initial du graphe

    neighbor: 
    fonction prenant en argument un noeud du graphe et renvoyant la liste de ses voisins

    target_node:
    noeud que l'on cherche à trouver
    """

    a_explorer = [initial_node]
    n = 0

    while n < len(a_explorer):
        noeud = a_explorer[n]
        if target_node == noeud:
            l = [noeud]
            while l[-1] != initial_node:
                v = neighbor(l[-1])
                for i in range(n):
                    if a_explorer[i] in v:
                        l.append(a_explorer[i])
                        n = i
            l.reverse()
            return l
        else:
            voisins = neighbor(noeud)
            nouveau = []
            for noeud_voisin in voisins:
                if voisins not in a_explorer:
                    nouveau.append(noeud_voisin)
            a_explorer =  a_explorer + nouveau
        n += 1
    return "not found"
