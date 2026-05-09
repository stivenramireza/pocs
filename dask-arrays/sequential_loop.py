from time import sleep

def inc(x):
    sleep(1)
    return x + 1

data = [1, 2, 3, 4, 5, 6, 7, 8]

results = []
for x in data:
    y = inc(x)
    results.append(y)
    
print(results)