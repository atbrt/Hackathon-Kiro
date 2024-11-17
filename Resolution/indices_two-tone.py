
def indices_twopaint(dico, l):
    ensemble=[]
    for k in range(len(dico["vehicles"])):
        if dico["vehicles"][k]["type"]=="two-twone":
            ensemble.append(l.index(dico["vehicles"][k]["id"]))


    return ensemble




