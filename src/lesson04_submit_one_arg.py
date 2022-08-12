# SuperFastPython.com
# example issuing an asynchronous task with an argument
from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed in a worker thread
def task(number):
    # generate a random value between 0 and 1
    value = random()
    # report a message
    print(f'Task generated {value}')
    # block for a moment to simulate work
    sleep(value)
    # return a new value
    return number + value

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPoolExecutor() as exe:
        # issue an asynchronous task
        future = exe.submit(task, 100)
        # get the result once the task completes
        result = future.result()
        # report the result
        print(result)
