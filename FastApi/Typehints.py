a = 10

print(type(a))

a = '10'
print(type(a))

print("-" * 20)

text: str = "100"
text1: str = "Pooja"

print(type(text))
print(type(text1))

text2: str = 100

print(type(text2))

print("reverse a list")

# Here parameter type is unknown
def fun(param):
    param.reverse()
    return param

print(fun(['1','2']))

# using typehint
def fun(param: list) ->list:
    param.reverse()         # color changed of reverse() because we defined with typehint
    return param

print(fun(['1','2']))

# without typehints
def fullname(fname,lname):
    return fname.title() + " " + lname.title()

print(fullname("pooja","dhere"))

# With typehints
def fullname(fname:str, lname:str) ->str:
    return fname.title() + " " + lname.title()

print(fullname("pooja","dhere"))
