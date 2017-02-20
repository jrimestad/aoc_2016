import sys
import numpy as np
import collections as c
import operator

def comp(obj1, obj2):
    if obj1[1] == obj2[1]:
        return ord(obj2[0]) - ord(obj1[0]) #Sort by char value
    return obj1[1] - obj2[1] #Sort by count

def isRealRoom(roomName):
    # print roomName
    code = roomName[roomName.rfind('[')+1:roomName.rfind('[')+6]
    name = roomName[0:roomName.rfind('-')]
    num = int(roomName[roomName.rfind('-')+1:roomName.rfind('[')])
    print num
    count = c.Counter(name.replace('-', '')).items()
    count.sort(cmp=comp)
    res = ""
    # print(count)
    for (key, val) in count[-5:][::-1]:
        res += key
    # print res
    # print code
    return (res == code, num)

assert(isRealRoom("aaaaa-bbb-z-y-x-123[abxyz]") == (True, 123))
assert(isRealRoom("a-b-c-d-e-f-g-h-987[abcde]") == (True, 987))
assert(isRealRoom("not-a-real-room-404[oarel]") == (True, 404))
assert(isRealRoom("totally-real-room-200[decoy]") == (False, 200))

counter = 0
val = 0
for line in open("input.txt"):
    (isValid, roomNum) = isRealRoom(line)
    if isValid:
        counter += 1
        val += roomNum
    
print val
