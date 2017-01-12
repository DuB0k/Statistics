from sys import stdin

#arrayLength = int(stdin.readline())
#array = stdin.readline().split()

arrayLength = 10
array = "4978 11735 14216 14470 38120 51135 64630 67060 73429 99233".split()

sumNum = 0
mean = 0.0
median = 0.0
mode = 0

array = list(map(int, array))

for item in array:
    sumNum = sumNum + item

mean = sumNum / arrayLength

array = sorted(array)

#If N is an odd number  -> median = X(n+1)/2
if arrayLength % 2 != 0:
    median = array[int((arrayLength+1)/2)]
#If N is an even number -> median = (X(n/2)+ X((n/2)+1))/2
else:
    auxMidLow = int((arrayLength/2)-1)
    auxMidHig = int(arrayLength/2)
    median = (array[auxMidLow] + array[auxMidHig]) / 2

auxCount = 0
maxCount = 0


for item in array:
    auxCount = array.count(item)
    if auxCount > maxCount:
        maxCount = auxCount
        mode = item

print("mean ",mean)
print("median ",median)
print("mode ",mode)
