#linux 
> [!info]- This document was created using artificial intelligence
> This document was created using artificial intelligence and may not make sense in some areas.

`ino_t` is a data type used in the [[C]] language and commonly used in the [[Linux]] kernel and other operating systems. It stands for "inode type" and is used to represent inode numbers. In the context of [[the Linux file system]], an inode is a data structure that contains metadata information about a file, such as its ownership, permissions, size, timestamps, and pointers to the actual data blocks on the disk.

The `ino_t` data type is an [[integer]] type, and its size depends on the architecture and configuration. It is used to uniquely identify each inode in the filesystem. Since inodes are unique within a filesystem, `ino_t` is used as a compact representation of inode numbers.