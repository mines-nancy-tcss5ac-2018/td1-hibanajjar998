def listsortedfct(filepath):
    """ Cette fonction permet de mettre les noms du fichier fulepath dans une liste alphabétiquement ordonnée"""
    f=open(filepath,'r')
    l=[]
    for ligne in f:
        l+=ligne.split(sep='","')
    l[0]=l[0][1:]
    l[-1]=l[-1][:-1]    
    return sorted(l)

def score(list):
    """ Cette fonction permet de créer la liste des scores des noms contenus dans une liste de départ (list) """
    n=ord('A')-1
    lsv=[ sum([ord(c)-n for c in nom]) for nom in list ]
    sc=[]
    for i in range(len(list)):
        sc+=[(i+1)*lsv[i]]
    return sc


def solve(filepath):
    """ Solve problem 22
    Returns the global score of the filepath. """
    ls=listsortedfct(filepath)
    sc=score(ls)
    return sum(sc)

print("Le score total de l'ensemble du fichier p022_names est :",solve('p022_names.txt'))
    