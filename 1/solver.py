import math
import os

def blocksAway(filename):
    with open(filename, "r") as problem:
        tokens = problem.read().split(", ")
        x = 0
        y = 0
        rot = 0
        for token in tokens:
            if 'L' in token:
                #Go left
                rot = rot - 90
            if 'R' in token:
                #go right
                rot = rot + 90
            
            dist = int(token[1:])
            radRot = math.radians(rot)
            #print "dist:{} angle:{} rad:{} sin:{} cos:{}".format(dist, rot, radRot, math.sin(radRot), math.cos(radRot) )
            x += dist * math.sin(radRot)
            y += dist * math.cos(radRot) 
            
        return abs(x) + abs(y)


def firstRevisit(filename):
    with open(filename, "r") as problem:
        tokens = problem.read().split(", ")
        x = 0
        y = 0
        rot = 0
        visited = {(0,0):True}
        for token in tokens:
            if 'L' in token:
                #Go left
                rot = rot - 90
            if 'R' in token:
                #go right
                rot = rot + 90
                            
            dist = int(token[1:])
            radRot = math.radians(rot)
            for _ in range(dist):
                x += int(math.sin(radRot))
                y += int(math.cos(radRot))
                    
                #print "dist:{} angle:{} rad:{} sin:{} cos:{}".format(dist, rot, radRot, math.sin(radRot), math.cos(radRot) )

                print("token:{} x:{} y:{}".format(token, x, y))
                if visited.has_key((x,y)):
                    return (x,y)
                
                visited[(x, y)] = True
        return None
#print("x:{} y:{} dist:{}".format(x, y, abs(x)+abs(y)))

print(blocksAway(os.path.dirname(__file__) + "/prob1.txt"))
print(blocksAway(os.path.dirname(__file__) + "/prob2.txt"))
print(blocksAway(os.path.dirname(__file__) + "/prob3.txt"))
print(blocksAway(os.path.dirname(__file__) + "/problem.csv"))
print(firstRevisit(os.path.dirname(__file__) + "/prob4.txt"))
print(firstRevisit(os.path.dirname(__file__) + "/problem.csv"))
