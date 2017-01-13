from sys import stdin

#arrayLength = int(stdin.readline())
#array = stdin.readline().split()
#weights = stdin.readline().split()

arrayLength = 10
array   = "10 40 30 50 20 10 40 30 50 20".split()
weights = "1 2 3 4 5 6 7 8 9 10".split()


array   = list(map(int, array))
weights = list(map(int, weights))

mean = 0.0
sumWeight = 0

for x, y in zip(array, weights):
    mean = mean + (x * y)
    sumWeight = sumWeight + y

mean = mean / sumWeight
print("%.1f" %mean)
