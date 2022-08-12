# SuperFastPython.com
# example initializing worker threads in the pool
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed in a worker thread
def task(number):
    # report a message
    print(f'Worker executing task {number}...')
    # block for a moment
    sleep(1)

# initialize a worker in the thread pool
def init():
    # report a message
    print('Initializing worker...')

# protect the entry point
if __name__ == '__main__':
    # create and configure the thread pool
    with ThreadPoolExecutor(2, initializer=init) as exe:
        # issue tasks to the thread pool
        _ = exe.map(task, range(4))
