# SuperFastPython.com
# example of checking the status of an asynchronous task
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# task function executed in a worker thread
def work():
    # block for a moment
    sleep(0.5)

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor() as exe:
        # start one thread
        future = exe.submit(work)
        # confirm that the task is running
        running = future.running()
        done = future.done()
        print(f'Future running={running}, done={done}')
        # wait for the task to complete
        future.result()
        # confirm that the task is done
        running = future.running()
        done = future.done()
        print(f'Future running={running}, done={done}')
