#!/usr/bin/python3
import os
import random
import time
import sys

pid = os.getpid()
ppid = os.getppid()
t = int(sys.argv[1])
print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")
time.sleep(t)

exit_status = random.randint(0, 1)
print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")
os.exit(exit_status)

