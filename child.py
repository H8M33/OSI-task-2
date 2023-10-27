import os
import random
import sys

def main():
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child[{pid}]: I am started. My PID {pid}. Parent PID {ppid}.")

    exit_status = random.randint(0, 1)
    print(f"Child[{pid}]: I am ended. PID {pid}. Parent PID {ppid}.")
    sys.exit(exit_status)

if __name__ == "__main__":
    main()
