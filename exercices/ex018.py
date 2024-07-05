#write a program that reads an angle and shows the value of the sine, cosine and tangent of that angle
from math import sin,cos,tan
a = float(input("angle: "))
print("OK! here are the results: \n sin {} \n cos {} \n tan {}" .format(sin(a),cos(a),tan(a)))