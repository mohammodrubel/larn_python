l = [1,2,3,4,5,6]
fast_location = id(l)

print(fast_location)
l[0]=4
secondLocation = id(l)

print(secondLocation)