# SuperFastPython.com
# example of timeout while waiting for task result
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError

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
        try:
            # get the result from the task, blocks
            result = future.result(timeout=0.5)
            # report the result
            print(f'Got Result: {result}')
        except TimeoutError:
            print('Gave up waiting for a result')
