import math


n=int(input())
a=int(input())

area=((a**2)*n)/(4*math.tan(math.pi/n))
print(int(area))