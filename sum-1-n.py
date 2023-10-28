def sum1n(n):
    if n == 1:
        return 1
    else:
        return n + sum1n(n-1)


#Sample input = 5
print(sum1n(5))
