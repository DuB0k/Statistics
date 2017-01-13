from sys import stdin

def calculateMedianOfSortedArray(array):
    array = sorted(array)
    arrayLength = len(array)

    #If N is an odd number  -> median = X(n+1)/2
    if arrayLength % 2 != 0:
        median = array[int((arrayLength-1)/2)]
    #If N is an even number -> median = (X(n/2)+ X((n/2)+1))/2
    else:
        auxMidLow = int((arrayLength/2)-1)
        auxMidHig = int(arrayLength/2)
        median = (array[auxMidLow] + array[auxMidHig]) / 2

    return median

#arrayLength = int(stdin.readline())
#array = stdin.readline().split()
#frec  = stdin.readline().split()
arrayLength = 6
array = "6 12 8 10 20 16".split()
frec  = "5 4 3 2 1 5".split()

array = list(map(int, array))
frec  = list(map(int, frec))
dataset = []

indexFrec = 0
for x in array:
    i = frec[indexFrec]
    indexFrec += 1
    for y in range(0,i):
        dataset.append(x)

dataset = sorted(dataset)
#print(array)
#print(frec)
#print(dataset)

median = 0.0
q1 = 0
q3 = 0

arrayLength = len(dataset)
array = dataset

middle = 0
lowerHalf = []
upperHalf = []

if arrayLength % 2 != 0:
    middle = int((arrayLength-1)/2)
    upperHalf = array[(middle+1):arrayLength]
else:
    middle = int(arrayLength/2)
    upperHalf = array[middle:arrayLength]

middle = int(middle)

lowerHalf = array[0:middle]

#print('low ',lowerHalf)
#print('up  ',upperHalf)

q1 = calculateMedianOfSortedArray(lowerHalf)
q3 = calculateMedianOfSortedArray(upperHalf)
interquartile = q3 - q1

#print(q1)
#print(q3)
print("%.1f" %interquartile)
