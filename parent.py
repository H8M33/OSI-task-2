#!/usr/bin/python3
import os
import random
import sys

n = int(sys.argv[1])

print(f"Parent[{os.getpid()}]: I am started. My PID {os.getpid()}.")
def child_fork():
    child_pid = os.fork()
    if child_pid == 0:
        os.execl("./child.py", "./child.py", str(random.randint(5, 10)))
    else:
        print(f"Parent[{os.getpid()}]: I ran child process with PID {child_pid}.")

    child_pid, status = os.wait()
    return child

for i in range (n):
    child = child_fork()
    
while n > 0:
    child_pid, status = os.wait()
    if status != 0:
        child = child_fork()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.')
        n -= 1

os._exit(os.EX_OK)

