def solve(n):
    """ Solve the problem 16
    Returns the sum of the digits of 2**n """
    l1=str(2**n)
    l2=[int(i) for i in l1]
    return sum(l2)

assert(solve(15)==26)

def solvebis(n):
    return sum( int(c) for c in str(2**n))