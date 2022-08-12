# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait

# custom task function executed by a worker thread
def work():
    # block a moment
    sleep(1)
    # raise an exception
    raise Exception('Something bad happened!')
    # never gets here

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor() as exe:
        # execute our task
        future = exe.submit(work)
        # wait for the task to be done
        wait([future])
        # get the exception
        exception = future.exception()
        print(f'Task exception={exception}')
        # get the result from the task
        try:
            result = future.result()
        except Exception:
            print('Unable to get the result')
