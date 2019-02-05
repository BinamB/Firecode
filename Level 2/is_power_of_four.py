import math

def dec_to_bin(number):
    bin = []
    while number != 0:
        remainder = number%2
        number = math.floor(number/2)
        bin.insert(0, int(remainder))
    return bin


def is_power_of_four(number):
    bin = dec_to_bin(number)
    for i in range(1,len(bin)-1):
        if bin[i] != 0 or len(bin)%2 == 0:
            return False
    return True