#linux 
> [!info]- This document was created using artificial intelligence
> This document was created using artificial intelligence and may not make sense in some areas.

`nlink_t` is a data type used in the [[C]] language and commonly used in the [[Linux]] kernel and other operating systems. It stands for "link count type" and is used to represent the number of hard links to a file.

In [[the Linux file system]], a hard link is an additional name (link) assigned to an existing file. All hard links for a given file have the same inode number, which means they refer to the same data blocks on the disk. When a file is created, it has at least one hard link, which corresponds to its original name. Additional hard links can be created using the `link()` system call or by using the `ln` command in the shell.