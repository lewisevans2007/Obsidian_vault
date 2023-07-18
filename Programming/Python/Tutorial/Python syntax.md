#python

The syntax of the [[Python]] programming language is the set of rules that defines how a Python program will be written and interpreted (by both the runtime system and by human readers). The Python language has many similarities to Perl, C, and Java. However, there are some definite differences between the languages.

## Basic Rules of the Python syntax

In python the following rules apply:

- Python is case sensitive
- Python statements must be on a new line
- Python statements must be indented properly
- Function definition in Python starts with the keyword def followed by the function name and parentheses ( ( ) )
- The colon ( : ) is used to indicate the end of the function header
- The indented statements define different blocks of code

## Statements

Instructions that a Python interpreter can execute are called statements. For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc. are other kinds of statements which will be discussed later.

## Multi-line statement

In Python, the end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:

### Compliant code

```python
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
```

### Non-compliant code

```python
a = 1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9
```

```python
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
```

### Multi line statements in functions

In a function call if you need to use multiple lines when defining a variable in a function call, you can use a comma and a new line to use multiple lines. For example:

```python
def my_function(a, b, c,
                d, e, f):
    print(a, b, c, d, e, f)
```

## Quotation in Python

Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal:

```python
my_string = 'Hello'
my_string = "Hello"
my_string = '''Hello'''
my_string = """Hello"""
```

Triple quotes are used to span the string across multiple lines. For example, all the following are legal:

```python
my_string = '''Hello, welcome to
           the world of Python'''
```

## Colons

The colon (:) is an important character in Python syntax. It is used in the following cases:

- After the if, elif and else statements, to mark the end of the condition
- After the for and while loops, to mark the end of the loop header
- After the function header, to mark the end of the header
- After the class header, to mark the end of the header

### Example

```python
if a > b:
    print(a)
else:
    print(b)
```

```python
for i in range(10):
    print(i)
```

```python
def my_function(a, b):
    return a + b
```

```python
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
```