import time
start = time.time()


def sumitup(n):
    total = 0
    for i in range(n):
        total = total + i
    return total


print(sumitup(1000000))
print(time.time() - start)
