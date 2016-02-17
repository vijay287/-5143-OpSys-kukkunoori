// What are three objectives of an OS design?
The main objectives of Operating System design are
Convenience
Efficiency
Maintainability
Security
Convenience:  The main purpose of an operating system is to provide a convenient interface for users of a computer. The operating system makes use of a computer's hardware and provides services to computer users. The operating system provides some of its services, such as the computer mouse and keyboard, directly to computer users. It provides other services through application programs. However the operating system provides services, its design should make for convenience of use.
Efficiency: The efficiency of the sharing achieved by an system can be measured interms of the density utilization of the resources. Each item is allocated to the user  for certain amount of time.Each such item can be given a comparative weighting related to it’s capital and running cost and possibly also scarcity value; multiplying each  weight by the percentage of time in use.it is possible to obtain a figure for the density of utilization of the installations as a whole. Naturally  this figure depends on the degree of balance between the hardware configuration and work load of the user.
Maintainability:  Operating system should be easy to maintain and upgrade. It should be easy to upgrade an operating system when new computer hardware comes to the market. And it should also be possible to expand the system to include more services to meet user needs.
Security: Computer security is become a main issue now a days because of hackers.OS should provide a safe and secure environment to only to it’s authorized user to utilize it’s resources.

// What is the kernel of an OS?
Kernel is a computer program that manages i/o requests from software and translates them in to data processing instructions for central processing unit and other components of the system.kernel is afundamental part of computers ‘Operating system’.
The main code of the kernel is located in the main part of the memory which shouldn’t be overwritten by other.
 
Kernel performs executing processes and handling interrupts, in kernel space  whereas everything a user normally does, such as writing text in a text editor or running programs in a GUI (graphical user interface), is done in user space. This separation prevents user data and kernel data from interfering with each other and thereby diminishing performance or causing the system to become unstable (and possibly crashing).
Kernel works as a mediator between processes and computer hardware like
Central Processing System 
Memory Devices
Input/Output devices


// What is multiprogramming?
Multiprogramming is nothing but parallel processing in which several processes running on at the same time on a uniprocessor. Since there is only one processor.Operaating system executes programs all at atime in part by part. It divides the program and execute each part of the program, but to the user it appears os is executing all the programs at a time
If the machine has the capability to cause an interrupt after a  time interval, then the os will execute program for a given length of time, regain, and then execute another program in a given length of time.If  this mechanism does not present , the operating system has no choice but to  execute a program with the expectation, but not the certainty, then  the program will eventually return control to the operating system.
 




// What is a process?
     A Process means  program in execution , a process must go in a sequential manner, definition of process is as follows
A process is defined as an entity which represents the basic unit of work to be implemented in the system
Components of the process are
Object program –code to be executed
Data-   data which is used to execute the program
Resources-while exection of program it need some resources
Status-verifies the status of the program execution
A program by itself is not a process. It is a static entity made up of program statement while process is a dynamic entity. Program contains the instructions to be executed by processor.
A program takes a space at single place in main memory and continues to stay there. A program does not perform any action by itself.
New- process created
Ready-processor  ready to execute the process
Running-  program is running
Waiting- process is waiting for an event to take place
Termination- process is finished
 
// How is the execution context of a process used by the OS?

The OS has to Load executable from hard disk to main memory . Keep track of the states of each process currently executed . Make sure – No process monopolizes the CPU – No process starves to death – Interactive processes are responsive – Processes are shielded from one another
A process consists of  an executable ,associated data needed by the program (global data, dynamic data, shared data) . Execution context (or state) of the program,  Contents of data registers - Program counter, stack pointer - Memory allocation - Open file (pointers)

// list and expain five storage management responsibilities of a typical OS

 Process isolation
This is the prevention of data and instruction from interfering with each other process isolation helps this happen.

Automatic allocation and management
This is the process whereby allocation should be transported to the programmer.

Support of modular programming
Supports the program to be able to define programs modules and to create, destroy and alter the size of modules dynamically
.
 Protection and access control
This is the process of sharing memory this is desirable when sharing is needed by a particular application it also threatens the integrity of programs.

Long term storage
Is a process whereby memory is stored for a long period of time even when the computer is switch off it is stored in the RAM.
// Differnce between  Real Address &virtual address
 A physical address also called as real address, or binary address. is a memory address that is represented in a register of memory mapped I/O device  and the form of a binary number on the address bus circuitry in order to enable the data bus to access a particular storage cell of main

Virtual Address:
In computing, a virtual address space or address space is the set of ranges of  address Space that an operating system makes available to a process. which can be 4 bytes for 32-bit or 8 bytes for 64-bit Operating System versions. The range of virtual addresses usually starts at a low address and can extend to the highest address allowed by the computer's instruction set architecture and supported by the operating system's pointer size implementation.  This  provides several benefits, one of which is, if each process is given a separate address space, security through process isolation.

//Describe Round robin scheduling technique

Round robin is designed specifically for time sharing systems . A small unit of time also known as time slice or quantum is set/defined . The ready queue works like circular queue .Round robin  is the  scheduling algorithm used by the CPU during execution of the process. It is also known as cyclic executive  Round robin algorithm is simple and easy to implement .

processes in this algorithm are kept in the circular queue also known as ready queue .A small unit of time also known as time slice or quantum is set/defined . The ready queue works like circular queue .All.  Each New process is added to the tail of the ready/circular queue . It is similar tofirst come first serve  but the preemption  is the added functionality to switch between the processes .

// difference between monolithic Kernal & microkernel

Kernel: kernel is the indispensable and therefore most important part of an operating system. Roughly, an operating system itself consists of two parts: the kernel space (privileged mode) and the user space (unprivileged mode). Without that, protection between the processes would be impossible.
There are two different concepts of kernels:
•         monolithic kernel.
•         μ-kernel (micro kernel).

monolithic kernel:

It runs every basic system service like process and memory management, interrupt handling and I/O communication, file system, etc .The older approach is the monolithic kernel, of which Unix, MS-DOS and the early Mac OS are typical represents of. in kernel space.  The inclusion of all basic services in kernel space has three big drawbacks.

        1)   The kernel size increase.
   2)    Lack of extensibility.
        3)   The bad maintainability. 

To overcome these limitations of extensibility and maintain-ability, the idea of μ-kernels appeared at the end of the 1980’s. 

This is time and resource consuming because the compilation of a new kernel can take several hours and a lot of memory. Bug-fixing or the addition of new features means a recompilation of the whole kernel. Every time someone adds a new feature or fixes a bug, it means recompilation of the whole

micro kernel:
which was slower than its monolithic counterpart,. There is a server for managing memory issues, one server does process management, another one manages drivers, and so on The concept was to reduce the kernel to basic process communication and I/O control, That way, the μ-kernel is not a block of system services anymore, but represents just several basic abstractions and primitives to control the communication between the processes and between a process and the underlying hardware.and let the other system services reside in user space in form of normal processes.Because communication is not done in a direct way anymore, a message system is introduced, which allows independent communication and favors extensibility. the servers do not run in kernel space anymore, so called ”con-text switches” are needed, to allow user processes to enter privileged mode  .

//what is  multi threading?
One thing can performs multiple actions. The real usage of a thread is not about a single sequential thread, but rather using multiple threads in a single program. Each user request for a program or system service) is kept track of as a thread with a separate identity. the status of work on behalf of that thread is kept track of until the work is completed



