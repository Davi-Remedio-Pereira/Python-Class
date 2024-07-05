#A teacher wants to draw one of his four students to erase the board. Make a program that helps them, reading their name and writing that of the chosen one
import random
list = []
choice = random.randint(1,4)
while len(list) != 4:
    list = input("Student Name: ")
print("The chosen one is...{}!" .format())
