#code a program that receives the adjacent and opposite sides of a right triangle and calculates its hypotenuse
from math import hypot
ca = float(input("adjacent side: "))
co = float(input("opposite side: "))
##print("with given numbers, the hypotenuse is {}!".format(sqrt(pow(ca,2) + pow(co,2))))
#the method above was my first try, but I discovered the math.hypot command a little after
print("with given numbers, the hypotenuse is {}!" .format(hypot(ca,co)))