#time to paint, folks! make a code, it needs to calculate the area of a wall, after that display the results and the tint used (every bucket is equivalent to 2m²)
height = float(input("please, type the height of your wall: "))
width = float(input("and the width: "))
a = height * width
print("your wall have a area of: {}, And you'll need {} buckets to paint the entire wall" .format(a, a/2))