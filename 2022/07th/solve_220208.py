# BOJ 1297
import math
from sys import stdin

d, h, w = map(int, stdin.readline().split(' '))
z = math.sqrt(h * h + w * w)
print(int(d * h // z), int(d * w // z))
