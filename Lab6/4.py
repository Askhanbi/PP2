# Built Function ex4

import math, time

SQ = int(input())
milisc = int(input())
time.sleep(0.001 * milisc)

print("Square root of", SQ, " after ", milisc, " miliseconds is ", math.sqrt(SQ) )