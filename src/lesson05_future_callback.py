# SuperFastPython.com
# example of adding a done callback to a task
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# callback function to call when a task is completed
def custom_callback(future):
    # report a message
    print(f'Custom callback got: {future.result()}')

# custom task function executed in a worker thread
def work():
    # block for a moment
    sleep(1)
    # return a result
    return 99

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor() as exe:
        # execute the task
        fut = exe.submit(work)
        # add the custom callback
        fut.add_done_callback(custom_callback)
