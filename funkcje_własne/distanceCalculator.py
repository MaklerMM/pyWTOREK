from math import sqrt

def distanceCalculator (p1, p2):
    return sqrt(pow(p2[0] - p1[0],2) + pow(p2[1] - p1[1],2))


p1 = [1,1]
p2 = [-1, -1]

print(distanceCalculator(p1,p2))