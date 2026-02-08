# emplicit conversion 

x = 10
y = 10.3

z = x + y 

# expelicite conversion 

x = 123 

y = float(x)
convert = str(x)


# get error 
name = "rubel"

mainName = int(name)

try:
    name = "rubel"
    x = int(name)
    print(x)

except Exception as e :
    print(e)


print(x)
print(y)
print(y)
print(convert)
print(name)