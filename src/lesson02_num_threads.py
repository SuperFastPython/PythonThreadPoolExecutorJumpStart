# SuperFastPython.com
# example of setting a large number number of workers
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# custom task function executed in the thread pool
def task(number):
    # block for a moment
    sleep(1)
    # report a message
    if number % 100 == 0:
        print(f'>task {number} done')

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor(1000) as exe:
        # issue many tasks to the pool
        _ = exe.map(task, range(1000))
