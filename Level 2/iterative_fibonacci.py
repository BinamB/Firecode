def better_fibonacci(n):
    num1 = 1
    num2 = 0
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(2, n+1):
            temp = num1 + num2
            num2 = num1
            num1 = temp
        return num1