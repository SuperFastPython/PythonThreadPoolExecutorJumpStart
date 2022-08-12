# SuperFastPython.com
# example of waiting for all tasks to complete
from time import sleep
from random import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait

# custom task function executed by a worker thread
def task(number):
    # block for a fraction of a second
    sleep(random())
    # report value
    print(number)

# protect the entry point
if __name__ == '__main__':
    # start the thread pool
    with ThreadPoolExecutor(10) as exe:
        # issue all tasks and gather the futures
        futs = [exe.submit(task, i) for i in range(10)]
        # wait for all tasks to complete
        _ = wait(futs)
        # report a message
        print('All tasks are done!')
