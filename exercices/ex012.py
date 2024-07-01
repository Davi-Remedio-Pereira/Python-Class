#make a code display a given price with 5% discount
price = float(input("what's the price? "))
dis = price + (price/100)*5
print("the new price with 5% discount is {}" .format(dis))