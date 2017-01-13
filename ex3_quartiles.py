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
#arrayLength = 10
#array   = "3 7 8 5 12 14 21 15 18 14".split()
arrayLength = 9
array   ="3 7 8 5 12 14 21 13 18".split()


array = list(map(int, array))
array = sorted(array)
print(array)

median = 0.0
q1 = 0
q2 = 0
q3 = 0

middle = 0
lowerHalf = []
upperHalf = []

if arrayLength % 2 != 0:
    middle = int((arrayLength-1)/2) 
    q2 = array[int(middle)]
    upperHalf = array[(middle+1):arrayLength]
else:
    middle = int(arrayLength/2)
    q2 = int(calculateMedianOfSortedArray(array))
    upperHalf = array[middle:arrayLength]

middle = int(middle)

lowerHalf = array[0:middle]

print('low ',lowerHalf)
print('up  ',upperHalf)

q1 = int(calculateMedianOfSortedArray(lowerHalf))
q3 = int(calculateMedianOfSortedArray(upperHalf))

print(q1)
print(q2)
print(q3)
