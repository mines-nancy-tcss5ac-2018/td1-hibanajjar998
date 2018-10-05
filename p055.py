def reverse(num):
    return int(str(num)[::-1])

def isLychrel(n):
    i=1
    while i<=50 and n+reverse(n)!=reverse(n+reverse(n)):
        i+=1
        n+=reverse(n)
    return i==51

def solve(seuil):
    """ Solve problem 55
    Returns how many Lychrel numbers we have below (seuil) """
    LN=0
    for i in range(seuil):
        if isLychrel(i): LN+=1
    return LN
    
print("Il existe ",solve(10000),' nombre de Lychrel inférieurs à 10 000.')