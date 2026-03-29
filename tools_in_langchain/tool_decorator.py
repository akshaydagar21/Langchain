# Step 1 - create a function

def multiply(a, b):
    """Multiply two numbers"""
    return a * b


# Step 2 - add type hints

def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Step 3 - add tool decorator

from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Invoke the tool
result = multiply.invoke({"a": 3, "b": 5})
print(result)


print(multiply.name)
print(multiply.description)
print(multiply.args)