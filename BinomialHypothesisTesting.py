import MachineLib as M

#Let X be the discrete random variable: 'number of birdies, or better'.
#X ~ B(n, p), where n is the number of trials, and p is the probability of a machine achieving a birdie or better.
def B_test(significance_level, tail, r, n, p):
    if tail == 'L':
       print("H0: p =", str(p), "\nH1: p <", str(p))
       test_statistic = M.bin_P(tail, r, n , p)
       if test_statistic <= significance_level:
          return "Reject H0, as", str(test_statistic), "≤", str(significance_level), ". Thus, there is sufficient evidence at the", str(significance_level), "significance level to accept H1, and support the claim that p <", str(p), "."
       
       else:
          return "Accept H0, as", str(test_statistic), "≥", str(significance_level), ". Thus, there is insufficient evidence at the", str(significance_level), "significance level to accept H1, and support the claim that p <", str(p), "."
        
    elif tail == 'U':
       print("H0: p =", str(p), "\nH1: p >", str(p))
       test_statistic = M.bin_P(tail, r, n , p)
       if test_statistic <= significance_level:
          return "Reject H0, as", str(test_statistic), "≤", str(significance_level), ". Thus, there is sufficient evidence at the", str(significance_level), "significance level to accept H1, and support the claim that p >", str(p), "."
       
       else:
          return "Accept H0, as", str(test_statistic), "≥", str(significance_level), ". Thus, there is insufficient evidence at the", str(significance_level), "significance level to accept H1, and support the claim that p >", str(p), "."
    
    else:
       print("H0: p =", str(p), "\nH1: p ≠", str(p))

print(B_test(0.05, 'U', 15, 100, 0.12))
