import sys
import math

def getAreaUclid(r):
    return math.pi * (r ** 2)

def getAreaTaxi(r):
    return 2 * (r ** 2)

_r = int(sys.stdin.readline())
print("{:.6f}".format(getAreaUclid(_r), 6))
print("{:.6f}".format(getAreaTaxi(_r), 6))

