from math import log, sqrt

def isPP(n):
    for k in range(2, int(sqrt(n))+ 1):
        if k ** int(round(log(n, k))) == n:
            return ([k, int(round(log(n, k)))])        
    return None