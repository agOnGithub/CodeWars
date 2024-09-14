def remov_nb(n):
    sum = n*(n + 1)/2  
    return [(x, (sum - x) / (x + 1)) for x in range(1, n+1) if (sum - x) % (x + 1) == 0 and 1 <= (sum - x) / (x + 1) <= n]