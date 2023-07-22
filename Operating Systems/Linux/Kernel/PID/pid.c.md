#linux
In [[linux]] [[PID|process ID]] is a unique number assigned to each process. It is used to identify the process. [[PID|Process ID]] is always unique, but after [[PID|process ID]] 32768 it starts reusing the [[PID|process ID]]. In the [[Linux]] Kernel the file `kernel/pid.c` handles pid's.

## Functions in pid.c

- [[alloc_pid]]
- [[free_pid]]