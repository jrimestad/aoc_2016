import math
import os
import numpy as np

def mostCommon(filename):
    counter = []
    for line in open(filename, "r"):
        for index, char in enumerate(line.strip()):
            if len(counter) < index + 1:
                counter.append({char: 1})
            else:
                if char in counter[index]:
                    counter[index][char] = counter[index][char] + 1
                else:
                    counter[index][char] = 1                    

    res = ""
    for entry in counter:
        res += max(entry.iterkeys(), key=(lambda key: entry[key]))
    
    print res
    
def leastCommon(filename):
    counter = []
    for line in open(filename, "r"):
        for index, char in enumerate(line.strip()):
            if len(counter) < index + 1:
                counter.append({char: 1})
            else:
                if char in counter[index]:
                    counter[index][char] = counter[index][char] + 1
                else:
                    counter[index][char] = 1                    

    res = ""
    for entry in counter:
        res += min(entry.iterkeys(), key=(lambda key: entry[key]))
    
    print res
    
print(mostCommon(os.path.dirname(__file__) + "/test1.txt"))
print(mostCommon(os.path.dirname(__file__) + "/input.txt"))
print(leastCommon(os.path.dirname(__file__) + "/test1.txt"))
print(leastCommon(os.path.dirname(__file__) + "/input.txt"))
