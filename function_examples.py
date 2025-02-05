def greet(): #Def is defining that when using greet, it will print Hello!
    """
    Simple function that just prints hello
    :return: None
    """
    #Those are docstrings, used to explain the function
    print("Hello!")

greet()
greet()
greet()

def greet2(name):
    """
    Simple function that greets a person
    :param The name of a person
    :return: None
    """
    print(f"Hello,{name}")

greet2("Alonso")

def special_op(a=1, b=1):
    """
    Special op is 10xa+b
    :param a: first number
    :param b: second number
    :return: value: 10a+b
    """
    return 10*a+b

print(special_op(10,2))
print(special_op(2,10))
result = special_op(8,9)
print(f"the special op for 8 and 9 is: {result}")
print(special_op(b=8,a=9))
print(special_op())
print(special_op(a=9))

#Calling functions within a function
def bond_greet(name):
    print(f"The name is {name}")

def bond_name(first_name="Ortiz",last_name="Alonso"):
    return f"{last_name}, {first_name} {last_name}"

print(bond_name("Bond","James"))
bond_greet(bond_name("James","Bond"))
...