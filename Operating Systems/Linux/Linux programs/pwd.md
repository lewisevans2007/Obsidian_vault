#linux 
The `pwd` command prints the working directory.

## Example

```
user@computer:~$ pwd
/home/user
user@computer:~$ cd /
user@computer:~$ pwd
/
```

It is really only useful if you cant see the working directory form the shell.

## Usage

```
pwd: pwd [-LP]
    Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.
```