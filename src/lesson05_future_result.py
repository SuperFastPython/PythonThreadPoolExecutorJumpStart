# SuperFastPython.com
# example of getting the result from a completed task
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# task function executed in a worker thread
def work():
    # block for a moment
    sleep(1)
    # return a message
    return 'All Done'

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor() as exe:
        # start one thread
        future = exe.submit(work)
        # get the result from the task, blocks
        result = future.result()
        # report the result
        print(f'Got Result: {result}')
