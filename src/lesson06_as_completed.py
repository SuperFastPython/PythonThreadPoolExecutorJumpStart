# SuperFastPython.com
# example of handling results in task completion order
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# custom function executed by a worker thread
def task(number):
    # block for a fraction of a second
    sleep(random())
    # return task number
    return number

# protect the entry point
if __name__ == '__main__':
    # start the thread pool
    with ThreadPoolExecutor(10) as exe:
        # submit tasks and collect futures
        futs = [exe.submit(task, i) for i in range(10)]
        # handle task results as they are completed
        for future in as_completed(futs):
            # retrieve the result
            result = future.result()
            # report the result
            print(f'> result for task {result}')
