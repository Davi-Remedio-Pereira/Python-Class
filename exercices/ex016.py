#make a program that receive a float number and display the integer part of said number
from math import floor
n = float(input("write a float number and press enter: "))
print("the given number is {}, and it integer part is {}" .format(n,floor(n)))