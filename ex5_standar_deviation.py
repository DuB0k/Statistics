from sys import stdin
from math import sqrt

#arrayLength = int(stdin.readline())
#array = stdin.readline().split()
arrayLength = 5
array = "10 40 30 50 20".split()

sumNum = 0
mean = 0.0
sumSquaredMean = 0

array = list(map(int, array))

for item in array:
    sumNum = sumNum + item

mean = sumNum / arrayLength
#print(mean)

for item in array:
    sumSquaredMean = sumSquaredMean + pow((item - mean), 2)
#print(sumSquaredMean)

standarDeviation = sqrt(sumSquaredMean/arrayLength)
print("%.1f" %standarDeviation)
