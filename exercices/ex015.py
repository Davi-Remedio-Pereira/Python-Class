#We need to rent a car, can you calculate the price for us?
d = float(input("how many days did you rent the car? "))
km = float(input("and kilometers? "))
print("the price of the car rent in days is ${:.2f}brl, with a extra ${:.2f}brl for the kilometers traveled. Giving a total of ${:.2f}brl" .format(d*60,km*0.15,(d*60)+(km*0.15)))