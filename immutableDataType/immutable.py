a =10

first_location=id(a)

a=20

seoncd_location = id(a)

b = (1,2,3)
firstTuppleLocation = id(b)

b = (1,2,3,4)
secondTuppleLocation = id(b)

# এর মাদ্ধমে বুঝা যাচ্ছে এ এর লকেশন ইমিউটিবল । 
# জখনই মডিফাই করার চেষ্টা করবো সে নতুন নতুন করে তার অস্তিত্ব তৈরি করবে 

# print(first_location)
# print(first_location)
# print(seoncd_location)

c = frozenset([1,2,3,4])
firstFrozen = id(c)
c = frozenset([1,2,3,4,5])
secondFrozen = id(c)

print(firstFrozen)
print(secondFrozen)
