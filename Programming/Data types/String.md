In programming a string is a data type that is used to represent text. It is usually represented by a sequence of characters. Strings are among the most commonly used data types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable. 

## Python example

```python
var1 = 'Hello World!'
var2 = "Python Programming"
```

Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

## C String arrays

In C programming, a string is a sequence of characters terminated with a null character \0. For example −
```c
char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
```
or
```c
char greeting[] = "Hello";
// The above is equivalent to the following
// {'H', 'e', 'l', 'l', 'o', '\0'}
```