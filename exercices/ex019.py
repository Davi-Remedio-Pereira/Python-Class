#A teacher wants to draw one of his four students to erase the board. Make a program that helps them, reading their name and writing that of the chosen one
import random
n1 = str(input("First Student: "))
n2 = str(input("Second Student: "))
n3 = str(input("Third Student: "))
n4 = str(input("Fourth Student: "))
list = [n1, n2, n3, n4]
choice = random.choice(list)
print("The chosen one is...{}!" .format(choice))
