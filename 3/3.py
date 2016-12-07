import sys
import numpy as np

def isTriangle((x,y,z)):
    return x + y > z and x + z > y and y + z > x
    
counter = 0

for line in open("input.txt"):
    values = line.split()
    if isTriangle((int(values[0]), int(values[1]), int(values[2]))):
        print values
        counter += 1
        
print "Real triangles: " + str(counter)

counter = 0
array = np.fromfile("input2.txt", sep=' ')
a = np.reshape(array , (len(array) / 3, 3))
a = np.transpose(a)
for row in np.reshape(a, (len(array) / 3, 3)):
    if isTriangle(row):
        counter += 1
        
print "Real Col triangles: " + str(counter)
# print array
