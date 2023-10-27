import os
import sys

def main():
    print(f"Parent[{os.getpid()}]: I am started. My PID {os.getpid()}.")

    child_pid = os.fork()
    if child_pid == 0:
        os.execve("./child", ["child"], {})
    else:
        print(f"Parent[{os.getpid()}]: I ran child process with PID {child_pid}.")

    child_pid, status = os.wait()
    if os.WIFEXITED(status):
        exit_status = os.WEXITSTATUS(status)
        print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {exit_status}.")
    else:
        print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated unexpectedly.")

if __name__ == "__main__":
    main()
