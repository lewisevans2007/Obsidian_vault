#python

In [[Python]] comments can be used to explain Python code. Comments can be used to make the code more readable. Comments can be used to prevent execution when testing code.

## Example

```python
# This is a comment
print("Hello, World!")
```

You can can also use a multiline comment when you want to comment out multiple lines of code.

## Example

```python
"""
This is a comment
written in
more than just one line
"""
```

## Comments in functions and classes

Comments can be used to also explain functions and classes.

```python
def my_function():
    """
    This function prints "Hello, World!"
    and returns nothing
    """
    print("Hello, World!")
```

Ideally you should follow this syntax for comments in functions and classes:

```python
def add(a, b):
    """
    Adds two numbers together

    Parameters:
        a (int): The first number
        b (int): The second number
    
    Returns:
        int: The sum of a and b
    """
    return a + b
```

In the example above, the comment explains what the function does, what parameters it takes, and what it returns. This is a good practice to follow if you want to make your code more readable and easier to understand by others.

## Comment TODO

When writing code, you can use the comment TODO to mark a part of the code that you want to come back to later to finish or fix.

```python
# TODO: This shows that you need to to do something
```

## Comment XXX

When writing code, you can use the comment XXX to show that something is wrong or has something unexpected.

```python
# XXX: This shows that something is wrong
```

## Other comment types

There are other comment types that you can use in Python. These are not recommended to use, but you can use them if you want to.

```python
# !!!: Bug
# ???: Question
# !!!: Warning
# FIX: Fix this
# HACK: Hack this
# NOTE: Note this
# REVIEW: Review this
```

## Commenting out code

You can use comments to comment out code that you don't want to run. This is useful when testing code.

```python
print("Hello")
# print("World")
```

In this example only `print("Hello")` will be executed, because `print("World")` is commented out.