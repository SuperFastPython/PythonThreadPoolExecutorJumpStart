# SuperFastPython.com
# example of setting the worker thread name prefix
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading

# custom task function executed in the thread pool
def task(number):
    # block for a moment
    sleep(1)

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor(4,
        thread_name_prefix='Downloader') as exe:
        # issue many tasks to the pool
        _ = exe.map(task, range(20))
        # report all thread names
        for thread in threading.enumerate():
            print(thread)
