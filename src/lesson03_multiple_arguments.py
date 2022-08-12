# SuperFastPython.com
# example executing tasks concurrently with multiple arg
from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed in a worker thread
def task(number, value):
    # report a message
    print(f'Task using {value}')
    # block for a moment to simulate work
    sleep(value)
    # return a new value
    return number + value

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPoolExecutor(4) as exe:
        # prepare random numbers between 0 and 1
        values = [random() for _ in range(10)]
        # issue tasks to execute concurrently
        for result in exe.map(task, range(10), values):
            # report results
            print(result)
