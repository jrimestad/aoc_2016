import math
import os

def keylock(filename):
    keymap = {(0,0):1, (1,0):2, (2,0):3,
              (0,1):4, (1,1):5, (2,1):6,
              (0,2):7, (1,2):8, (2,2):9}
    key = ""
    x = 1
    y = 1
    for line in open(filename, "r"):
        for char in line:
            if char == 'L':
                x = max(0, x - 1)
            if char == 'R':
                x = min(2, x + 1)
            if char == 'U':
                y = max(0, y - 1)
            if char == 'D':
                y = min(2, y + 1)
        key = key + str(keymap[(x,y)])
    return key

def keylock_advanced(filename):
    keyarray = [[None, None, "1", None, None], 
                [None, "2", "3", "4", None],
                ["5", "6", "7", "8", "9"],
                [None, "A", "B", "C", None],
                [None, None, "D", None, None]]
                
    key = ""
    x = 0
    y = 3
    for line in open(filename, "r"):
        for char in line:
            if char == 'L':
                tmpx = max(0, x - 1)
                if not keyarray[y][tmpx] is None:
                    x = tmpx
            if char == 'R':
                tmpx = min(4, x + 1)
                if not keyarray[y][tmpx] is None:
                    x = tmpx
            if char == 'U':
                tmpy = max(0, y - 1)
                if not keyarray[tmpy][x] is None:
                    y = tmpy
            if char == 'D':
                tmpy = min(4, y + 1)
                if not keyarray[tmpy][x] is None:
                    y = tmpy
        key = key + str(keyarray[y][x])
    return key

print(keylock(os.path.dirname(__file__) + "/test1.txt"))
print(keylock(os.path.dirname(__file__) + "/input.txt"))
print(keylock_advanced(os.path.dirname(__file__) + "/test1.txt"))
print(keylock_advanced(os.path.dirname(__file__) + "/input.txt"))
