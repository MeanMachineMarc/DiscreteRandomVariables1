import MachineLib as M

#Let X be the discrete random variable: 'number of birdies, or better'.
#X ~ B(n, p), where n is the number of trials, and p is the probability of a birdie or better.
def probability(tail, n, p):
    if tail == 'L': 
       return (nCr * (p ** r) * (1 - p) ** (n - r))
    