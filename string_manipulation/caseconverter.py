case_converter = "Hello wolrd"

print(case_converter.upper(),case_converter.lower(),case_converter.capitalize(),case_converter.title(),case_converter.swapcase())

print(case_converter.replace("wolrd", "programmer"))

demo = "hello world are you mad?"
print(demo.split(" "))

demo2 = "hello-world-are-you-mad?"
print(demo2.split("-"))

my_list = ["fardin","tazbeed","voumik"]

print("_".join(my_list))

demo_text = "         Hello World           "

print(demo_text.strip())
print(demo_text.lstrip())
print(demo_text.rstrip())