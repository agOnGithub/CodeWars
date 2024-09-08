def narcissistic( value ):
    digits = [int(d) for d in str(value)]
    sum = 0

    for d in digits:
        sum += d**len(digits)
    
    return sum == value