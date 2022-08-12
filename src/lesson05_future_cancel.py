# SuperFastPython.com
# example of canceling a task via it's future
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# custom function executed in a worker thread
def work(sleep_time):
    # block for a moment
    sleep(sleep_time)

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    with ThreadPoolExecutor(1) as exe:
        # start a long running task
        future1 = exe.submit(work, 2)
        running = future1.running()
        print(f'First task running={running}')
        # start a second
        future2 = exe.submit(work, 0.1)
        running = future2.running()
        print(f'Second task running={running}')
        # cancel the second task
        canceled = future2.cancel()
        print(f'Second task was canceled: {canceled}')
