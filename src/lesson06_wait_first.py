# SuperFastPython.com
# example of waiting for the first task to complete
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_COMPLETED

# custom task function executed by a worker thread
def task(number):
    # block for a fraction of a second
    sleep(random())
    # report that the task completed
    print(f'>task {number} is done')
    # return the task number
    return number

# protect the entry point
if __name__ == '__main__':
    # start the thread pool
    with ThreadPoolExecutor(10) as exe:
        # submit tasks and collect futures
        futs = [exe.submit(task, i) for i in range(10)]
        # wait until any task completes
        done,_ = wait(futs, return_when=FIRST_COMPLETED)
        # get the first task to complete
        future = done.pop()
        # get the result from the first task to complete
        result = future.result()
        # report the result
        print(f'Main first result: {result}')
