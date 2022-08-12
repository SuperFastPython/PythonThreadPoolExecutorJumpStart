# SuperFastPython.com
# example of waiting for the first task to fail
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_EXCEPTION

# custom task function executed by a worker thread
def task(number):
    # generate a random number between 0 and 1
    value = random()
    # block for a fraction of a second
    sleep(value)
    # check for a failure
    if value < 0.5:
        raise Exception(f'Task {number} Failed')
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
        done,_ = wait(futs, return_when=FIRST_EXCEPTION)
        # check that no tasks failed
        if len(done) == len(futs):
            print('No tasks failed')
        else:
            # get the first task to complete
            future = done.pop()
            # report the exception
            print(f'First fail: {future.exception()}')
