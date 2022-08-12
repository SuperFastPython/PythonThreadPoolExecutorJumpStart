# SuperFastPython.com
# example of executing tasks concurrently with timeout
from random import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError

# custom function to be executed in a worker thread
def task(number):
    # generate a random value between 0 and 1
    value = random()
    # report a message
    print(f'Task generated {value}')
    # block for a moment to simulate work
    sleep(number + value)
    # return a new value
    return number + value

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPoolExecutor(4) as exe:
        try:
            # issue tasks to execute concurrently
            for result in exe.map(task, range(10),
                timeout=2):
                # report results
                print(result)
        except TimeoutError:
            print('Gave up, took too long')
    # report that we will wait for the tasks to complete
    print('Waiting for tasks to complete...')
