def status(a):
    result = [1, 2, 3]
    for i in result:
        if a >= int(sum(result)):
            return a / result
    return i

print(status(5))