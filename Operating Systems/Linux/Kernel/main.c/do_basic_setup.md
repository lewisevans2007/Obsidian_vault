#linux 
This function performs basic setup tasks such as command-line parsing, setting up early [[printk]], and initializing the system log.
## Code
```c
static void __init do_basic_setup(void)
{
	cpuset_init_smp();
	driver_init();
	init_irq_proc();
	do_ctors();
	do_initcalls();
}
```