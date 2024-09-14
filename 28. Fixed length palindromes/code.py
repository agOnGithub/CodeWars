from math import ceil
def palin(a, b):
    output = ''
    for i in range(ceil(a / 2)):
	    output += str(int((b - 1) / 10 ** (ceil(a / 2) - i - 1)) % 10 + int(i == 0))
    return int(output + output[::-1][(a % 2):])