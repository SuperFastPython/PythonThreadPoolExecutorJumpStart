# SuperFastPython.com
# example running a function in the thread pool
from concurrent.futures import ThreadPoolExecutor

# custom function to be executed in a worker thread
def task():
    # report a message
    print('This is another thread')

# protect the entry point
if __name__ == '__main__':
    # create the thread pool
    with ThreadPoolExecutor() as exe:
        # issue the task
        future = exe.submit(task)
        # wait for the task to finish
        future.result()
    # close the thread pool automatically
