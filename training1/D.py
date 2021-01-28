import time
start_time = time.time()

a, b = map(int, input().split())
print((a ** b) % (10 ** 9 + 7))
print("%s seconds" % (time.time() - start_time))