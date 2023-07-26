#python

In [[Python]] you use variables to store values. Variables are created when you assign a value to it. Variables do not need to be declared with any particular type and can even change type after they have been set.

## Example

```python
a = 5
b = "John"
c = 4.5
d = True
e = ["apple", "banana", "cherry"]
```

## Casting

If you want to specify the data type of a variable, this can be done with casting. There are many different data types in python, but the most common ones are:

- `str` - [[Programming/Data types/String]]
- `int` - [[Integer]]
- `float` - [[Float]]
- `bool` - [[Boolean]]
- `list` - [[List]]
- `tuple` - [[Tuple]]

To cast a variable to a specific data type, you simply wrap the variable in the data type you want to cast it to.

```python
str()
int()
float()
bool()
list()
tuple()
```

### Casting example

This example wont work since you can't add a string and an integer together.

```python
x = "5"
y = 5
z = x + y
print(z)
```

result:

```python
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

To fix this, we can cast the variable `x` to an integer.

```python
x = "5"
y = 5
z = int(x) + y
print(z)
```

result:

```python
10
```