# What is a variable?
# -------------------------------
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Anand"
d = None

# What is a Data Type?
# -------------------------------
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

a = 1.2
print(type(a))
b = "1"
print(type(b))
c=True
print(type(c))
d=None
print(type(d))

# 1. Numeric data: int, float, complex
# -------------------------------
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i
complexNumber = complex(8,2)
print(complexNumber,type(complexNumber))

# 2. Text data: str
# -------------------------------
# str: "Hello World!!!", "Python Programming"
str = "Hello World!!!"
print(str,type(str))

# 3. Boolean data:
# -------------------------------
# Boolean data consists of values True or False.
print(True)

# 4. Sequenced data: list, tuple
# -------------------------------
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

tuple2 = (a,b)
print(tuple2,":",type(tuple2))

# 5. Mapped data: dict
# -------------------------------
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

dict1 = {"name":"Anand","age":25}
print(dict1)