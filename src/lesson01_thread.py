# SuperFastPython.com
# example of running a function in a new thread
from threading import Thread

# custom function to be executed in a new thread
def task():
    # report a message
    print('This is another thread')

# protect the entry point
if __name__ == '__main__':
    # define a task to run in a new thread
    thread = Thread(target=task)
    # start the task in a new thread
    thread.start()
    # wait for the thread to terminate
    thread.join()
