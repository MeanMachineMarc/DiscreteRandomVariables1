import MachineLib

#Let X be the discrete random variable: 'number of birdies, or better'.
#X ~ B(n, p), where n is the number of trials, and p is the probability of a machine achieving a birdie or better.
def bin_P(tail, r, n, p):
    r = int(r)
    n = int(n)
    p = float(p)

    if tail == 'L': #P(X <= r)
       total_probability = (1 - p) ** n 
       for r in range (1, (r + 1)): #Sum of probabilities up to and including r
           total_probability = total_probability + (MachineLib.nCr(n, r) * (p ** r) * (1 - p) ** (n - r))
        
       return MachineLib.round_xsf(total_probability, 4)

    elif tail == 'M': #P(X = r)
       if r > 0: #P(X = r), r > 0
          return MachineLib.round_xsf((MachineLib.nCr(n,r) * (p ** r) * (1 - p) ** (n - r)), 4)
       
       else: #P(X = 0)
          return MachineLib.round_xsf(((1 - p) ** n), 4)

    else: #P(X >= r)
       if r > 0: #P(X >= r), r > 0
          return MachineLib.round_xsf((1 - bin_P('L', (r - 1), n, p)), 4)
       
       else: #P(X >= 0)
          return 1