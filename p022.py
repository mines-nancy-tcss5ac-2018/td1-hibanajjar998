def listsortedfct(filepath):
    f=open(filepath,'r')
    l=[]
    for ligne in f:
        l+=ligne.split(sep='","')
    l[0]=l[0][1:]
    l[-1]=l[-1][:-1]    
    return sorted(l)

def score(list):
    n=ord('A')-1
    lsv=[ sum([ord(c)-n for c in nom]) for nom in list ]
    sc=[]
    for i in range(len(list)):
        sc+=[(i+1)*lsv[i]]
    return sc


def solve(filepath):
    ls=listsortedfct(filepath)
    sc=score(ls)
    return sum(sc)
    