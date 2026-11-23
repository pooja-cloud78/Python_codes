
""" Type hints are optional annotations that specify the intended types of variables and functions. 
Python does not enforce them at runtime; they are used by external tools such as IDEs and type checkers.
"""
a = 10
print(type(a))    #int type

a = '10'
print(type(a))    #str type

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
def fun1(param: list) ->list:
    param.reverse()         # color changed of reverse() because we defined with typehint
    return param

print(fun1(['1','2']))

# without typehints
def fullname(fname,lname):
    return fname.title() + " " + lname.title()

print(fullname("pooja","dhere"))

# With typehints
def fullname1(fname:str, lname:str) ->str:
    return fname.title() + " " + lname.title()

print(fullname1("pooja","dhere"))

""" Types in Typehint
1. str
2. int
3. bool
4. bytes
5. float
"""

def get_items(item_a:str,item_b:int,item_c:bool,item_d:bytes,item_e:float):
    return item_a,item_b,item_c,item_d,item_e

print(get_items("Pooja",100,True,b"a",3.14))

print("**************Any type****************")
from typing import Any
def fun_name(param:Any):     # when type is unknown
    return param

print(fun_name(7.888))
print(fun_name("dfsdfs"))

print("**************generic types****************")

""" Generic type
1. list[str]
2. tuple[int,int,int]
3. set[bytes]
4. dict[str,str]
"""
# list
def process_list(items:list[str])->None:
    for item in items:
        print(item)

print(process_list(["aa","bb","cc"]))

print("-" * 20)

# tuple and set
def process_tuple_set(item_t:tuple[int,int,str],item_s:set[bytes]):
    return item_t, item_s

print(process_tuple_set((5,6,'a'),{b"a"}))

print("-" * 20)

# dict
def process_dict(prices:dict[str,int]):
    for item_name,item_price in prices.items():
        print(item_name,"->",item_price)

print(process_dict({"chair":100,"table":250}))     

""" Union
Declare variable accepting multiple types using '|'
"""

def process_id(item: int | str):
    print("ID:", item, " of type", type(item))

process_id("Pooja")    
process_id(50)    

# None with union
def Greet(data:str | None = None):
    if data is not None:
        print("hello", data)
    else:
        print("Hello Friend")    

Greet("Pooja")
Greet()

# Iterable (Unknown type it may be list,tuple or set)
from collections.abc import Iterable
def reverse_array(item:Iterable[str]) ->list[str]:
    return list(item)[::-1]

print(reverse_array(["1","2","3"]))

print("-" * 20)
#Typehint with class
class person:
    def __init__(self, name:str):
        self.name = name

def get_name(one_person:person)->str:
    return one_person.name

p = person("pooja")     
print(get_name(p))   