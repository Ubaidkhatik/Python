s1 = 'This is the python string using singhle quote'
s2 = "Python String using double qoutes "
s3 = """Python string using triple quotes"""
print(s1)
print(s2)
print(s3)


print("String Functioins: ")
str_funcs = 'Anthony Gonsalves'
#1. len
print(len(str_funcs))

# 2. find
print(str_funcs.find("th"))

 # 3.count
print(str_funcs.count("s"))

# 4. startswith
print(str_funcs.startswith("An"))

#5. endswith
print(str_funcs.endswith("s"))

#6. .capitalize
print(str_funcs.capitalize())

#7. .upper()
print(str_funcs.upper())

#8.lower()
print(str_funcs.lower())

#9. slicing
print(str_funcs[1:4])
#negative slicing
print(str_funcs[-4:-1])

#10.replace()
print(str_funcs.replace('Anthony', 'Peter'))

#11.title()
print(str_funcs.title())

