PID stands for process identifier. It is commonly used in programs to specify a process running on a system. Most operating systems including [[Windows]], [[Linux]] and [[MacOS]] have PID's

## PID's in Linux
In [[Linux]] you can find information about a PID from the [[proc]] directory.

Lets have a look at the proc directory
```
1
107
109
138
139
144
145
197
2
205
<ALL OTHER FILES>
```

You can see the PID's of each procs here lets `cd` into one

```
arch_status
attr
auxv
cgroup
clear_refs
cmdline
comm
coredump_filter
cpuset
cwd -> /
environ
exe -> /usr/lib/systemd/systemd
fd
fdinfo
gid_map
io
limits
map_files
maps
mem
mountinfo
mounts
mountstats
net
ns
oom_adj
oom_score
oom_score_adj
pagemap
personality
projid_map
root -> /
sched
schedstat
setgroups
smaps
smaps_rollup
stack
stat
statm
status
syscall
task
timens_offsets
timers
timerslack_ns
uid_map
wchan
```
In this folder you can see the information about this PID.