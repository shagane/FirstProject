from functools import reduce
import re

mylist = list(map(lambda x: x*2, [1, 2, 3]))
mylist2 = [x*2 for x in range(1, 4)]
print (mylist)
print(mylist2)

myfilter = list(filter(lambda x: x%2 == 0, [2, 4, 5, 6, 9, 10, 12, 13]))
print(myfilter)

newlistforreduce = [1, 2, 3, 4, 5, 6, 9, 12, 8, 9, 10, 1, 2, 3, 4, 15, 95]
myreduce = reduce(lambda x, y : (x+y)/2,  newlistforreduce)
print(myreduce)
print (reduce(lambda x, y: x+y, [1,2,3,5,6,9]))
all_max = reduce(lambda a,b: a if (a > b) else b, newlistforreduce)
print("max=", all_max)

# list comprehension
newlist1 = [x**2 for x in range(2, 12, 2)]
print(newlist1)
odds = [x for x in range(10) if x % 2 != 0]
# [1, 3, 5, 7, 9]

[x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]
# если нужно записать else, то все пишется в начале, потом for

vec = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
[digit for lst in vec for elem in lst for digit in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

names = ['Tom', 'Dick', 'Harry']
ages = [50, 35, 60]
newdict = dict(zip(names, ages))
newone = list(zip(names, ages))
print(newone)


item = '"articul":"1G5YC90000"'
def pattern_strip(item):
    x = r'"\w+":"'
    y = r'\w+'
    z = '"'
    newitem = ''
    if item == x + y + z:
        newitem = y
    else:
        pass
    return newitem

print(pattern_strip(item))

