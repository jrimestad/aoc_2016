import sys
import unittest as ut

tests = {
"abba[mnop]qrst" : True,
"abcd[bddb]xyyx" : False,
"aaaa[qwer]tyui" : False,
"ioxxoj[asdfgh]zxcvbn" : True
}

def isTLS(address):
    """TLS = Transport Layer Snooping"""
    
    # print address
    inside = '[' in address[0:2]
    found = False
    for index in range(2, len(address)-2):
        if not inside:
            inside = address[index] == '['
        else:
            inside = not address[index] == ']'
        
        # print inside  
        prefix = address[index-2:index]
        postfix = address[index:index+2]
        # print(prefix + " == " + postfix[::-1])
        
        if prefix == postfix[::-1] and prefix != prefix[::-1]:
            # print str(index) + " : " + address[0:index] + " : " + address[index:]
            if inside:
                return False
            else:
                found = True

    return found    
    
correct = 0
for (key, val) in tests.items():
    if isTLS(key) != val:
        print("Failed on ip " + str(key))
    else:
        # print "correct"
        correct += 1
assert(correct == len(tests))

res = 0
lines = 0
for line in open("input.txt", "r"):
    lines += 1
    if isTLS(line):
        res += 1

print "lines: " + str(lines) + " correct: " + str(res)

def isSSL(address):
    """SSL = Super Secret listening"""
    
    return False
    
assert(isSSL("aba[bab]xyz") == True)
assert(isSSL("xyx[xyx]xyx") == False)
assert(isSSL("aaa[kek]eke") == True)
assert(isSSL("zazbz[bzb]cdb") == True)
