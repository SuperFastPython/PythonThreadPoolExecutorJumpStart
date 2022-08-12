# SuperFastPython.com
# example reporting the details of a default pool
from concurrent.futures import ThreadPoolExecutor

# protect the entry point
if __name__ == '__main__':
    # create a thread pool
    exe = ThreadPoolExecutor()
    # report the status of the thread pool
    print(exe._max_workers)
    # shutdown the thread pool
    exe.shutdown()
