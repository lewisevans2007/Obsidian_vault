#python

`sys.argv` is part of the [[sys]] module. It is a [[list]] of [[string|strings]] representing the arguments passed to the program. `sys.argv[0]` is the name of the program.

```bash
python3 script.py arg1 arg2
```

```python
import sys
print(sys.argv) # ['script.py', 'arg1', 'arg2']
```

```python
import sys
print(sys.argv[0]) # 'script.py'
```

```python
import sys
print(sys.argv[1]) # 'arg1'
```

```python
import sys
print(sys.argv[2]) # 'arg2'
```
