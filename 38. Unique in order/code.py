def unique_in_order(sequence):
    n = []
    for x in sequence:
        if len(n) < 1 or not x == n[len(n) - 1]:
            n.append(x)
    return n