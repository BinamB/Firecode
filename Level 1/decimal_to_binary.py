import math

def dec_to_bin(number):
    bin = []
    while number != 0:
        remainder = number%2
        number = int(math.floor(number/2))
        bin.insert(0, str(remainder))
    return (''.join(bin))