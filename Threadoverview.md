# 1.Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.
Thread1.py has two threads A & B which are independent to each other. so they gets executed independent to each other and prints the value. Wher in Thread2.py, it consists of two  threads A & B which are sharing the same  global variable "shared counter". So these  threads are dependent.
# 2.After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?
Yes, when we run Thread3.py it fix the problems that took place in Threads2.py with the help of lock method.when we use the  lock method,one thread access the global variable and locks it’s access then another thread cannot acccess that variable until it finish the work .Once the work is done it unlocks that variable.

#3.Comment out the join statements at the bottom of the program and describe what happens.
ThreadA and ThreadB starts execution while main thread completes before other thread does.
# 4.What happens if you try to Ctrl-C out of the program before it terminates?
Pressing Ctrl + c while a program is running in python it causes python to raise a KeyboardInterupt exception.But the interrupt is can’t be  handled as there is suitable catch block for that exception, this will catch all exceptions including the KeyboardInterupt that we just made.If keyboard interrupt exception occurs rapidly then it comes out of the program and terminates it.

# 5.Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.
As there is no lock for Shared Counter there is a race condition. The IF statement value gets varied as the shared counter variable is used by both the threads.

# 6.Does uncommenting the lock operations clear up the problem in question 5?
Yes when the lock section is uncommented, each thread has a indvidual right to sharedNumber at a specific point in time and No thread will print because they both have correct values at each point in the execution.

