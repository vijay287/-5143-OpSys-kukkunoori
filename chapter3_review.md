# Chapter 3 Review Questions
Name: Vijayaramakrishna
course: 5143 Operating System

##  What does it mean to preempt a process?

Preempting a process  means interrupting a task carried out by a computer system, kernel interrupts the computation and  forces the context switch  preempting the currently running process. Process can be prempted anytime when there is a higher priority process is available. A situation occurs when a higher priority process is waiting for system resources lower priority system is using system resources.then kernel preempts  that process to resume  execution  of the higher-priority process. In the  given system design, some operations performed by the system are not be preemptible. This  applies to kernel functions  and service interruption which, if not permittedto run completion, will lead   to produce race condition resulting in deadlock .


##  What is swapping and what is its purpose

Swapping is exchange of data between system hard disk and RAM. And it is also known as paging .the main purpose of swapping data is to read the required data from hard disk and brings it to ram so that it can be used by the application program .excessive swapping causes thrashing  and it is undesirable because it makes system to work slower , this causes mainly because of hard disk memory,it is slower than the ram. Virtual memory technique uses in system to keep memory in system  than actually exists. It creates aswap file in hard disk and   and sends all the program data to tha swap or paging file aand brings slowly to ram whenever it is needed.thhis is the main purpose of swapping.


##  List three general categories of information in a process control block.

Process identification: id of this process, id of the parent process and user id. Processor state information: program counter, status registers, and general-purpose registers. Three main categories are 
1.process identification data
2.process store data
3.process control data
Process control information:                                                                               
  Scheduling and  state information: process state, priority, scheduling-related information (amount of time waiting and time being executed), event (identity of event the process is awaiting before can be resumed).Data structuring: a process could be linked to other process in a queue.  Memory management: It  include pointers to page tables which describes the virtual memory assigned . Resource ownership and utilization. Process privileges: e.g. the memory that may be accessed, types of instructions that may be executed and the use of system utilities and services. Interprocess communication


##  Why are two modes (user and kernel) needed?

Two modes are required in computer because of  the system(cpu) has to execute the instructions and memory has to hold the instructions and data. It is when one program is running  at a time but nolonger it is the case now we have computers like run multiple programs at a time each needs its own memory space. switch the CPU quickly between programs to give the illusion that they are running at the same time.hold documents for several users, with the expectation that each user can protect their own files.allow multiple network connections simultaneously, where each connection  dealing with sensitive data.If every program had  access to the CPU, main memory and the peripheral devices, all concepts of separation of programs and the data in memory, on disk etc. would not exist.A program could look at all memory locations, including that of other programs, as well as read all the data on all of the attached disks, and read all the data being sent across the network.To prevent this we need two modes which are kernel mode and user modeIn kernel mode, the CPU has instructions to manage memory and how it can be accessed, plus the ability to access peripheral devices like disks and network cards. The CPU can also switch itself from one running program to another.In user mode, access to memory is limited to only some memory locations, and access to peripheral devices is denied. The ability to keep or relinquish the CPU is removed, and the CPU can be taken away from a program at any time.


##  What is the difference between an interrupt and a trap?

In any computer, during its normal execution of a program, there are some events that  cause the CPU to temporarily halt. Events like these are known as interrupts. Interrupts could be caused by either software or hardware faults. Hardware interrupts are called  Interrupts, and  software interrupts are called Exceptions or Traps. An Exception is an automatically generated software interrupt, while a Trap is a software-invoked interrupt initiated by the programmer
Interrupts are hardware interrupts, and  traps are software-invoked interrupts. Occurrences of hardware interrupts sometimes  disable other hardware interrupts, but this is not same  for traps. If you need to disallow hardware interrupts until a trap is served, you need to clear the interrupt flag. And usually the interrupt flag on the computer affects interrupts as opposed to traps. It means that clearing this flag will not prevent traps. Unlike traps, interrupts should preserve the previous state of the CPU.

##  Give three examples of an interrupt.

Here we have examples of interrupts are 
1.	Internal interrupt
2.	Software interrupt
3.	External interrupt

The External Interrupt takes place when any Input and output request for some Operation and the CPU will Execute that instructions first For Example When a Program is executed and when we move the Mouse on the Screen at tha time the CPU will handle this External interrupt first and after that it will resume with his Operation.
The Internal Interrupts are those which occurred due to Some Problem in the Execution Example When a user performing any Operation which contains any Error and which contains some type of Error. So that Internal Interrupts are those which are occurred by the Some Operations or by Some Instructions and the Operations those are not Possible but a user is trying for that Operation. And The Software Interrupts are those which are made some call to the System for Example while we are Processing Some Instructions and when we wants to Execute one more Application Programs.


##   What is the difference between a mode switch and a process switch?

A process switch is called when the processor switches from one thread or process to another. It  causes the contents of the cpu registers and instruction pointer has to be saved. The registers and instruction pointer for the new task will then be loaded into the processor and execution of the new process will start and resume. The old one  is no longer executing, but it's state is saved in memory to  the time kernel decides that it is ready to execute it again. It is what gives the illusion of multi tasking, while in reality, only a single process can run at a time on a cpu. A context switch could occur by hardware or software. A hardware interrupt could occur from a device like  keyboard,mouse,or system timer, causing code to begin executing the interrupt code. Software switches are occurred as a result of the kernel manually performing a task switch. This is how the scheduler usuallymakesacontextswitch.A mode switch is what is referred to when the cpu changes privilege levels. The kernel works at a higher privilege than a standard user task. If the user task to access things controlled by the kernel, it is necessary fro a mode switch to occur. The currently executing process does not change during a mode switch. The processor uses these modes to protect the OS from misbehaving or malicious programs, as well as controlling concurrent access to ram, io devices,etc. A mode switch must occur for a software context switch to occur. Only the Kernel can cause acontextswitch. 


