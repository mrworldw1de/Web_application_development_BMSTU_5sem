import time
from contextlib import contextmanager

@contextmanager
def cm_timer_2():
    _start_time = time.perf_counter()
    yield _start_time
    elapsed_time = time.perf_counter() - _start_time
    _start_time = None
    print(f"Time: {elapsed_time:0.4f} seconds")

class cm_timer_1():
    def __init__(self):
            self._start_time = None

    def __enter__(self):
        self._start_time = time.perf_counter()


    def __exit__(self, type, value, traceback):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Time: {elapsed_time:0.4f} seconds")

#with cm_timer_1():
#    time.sleep(5.5)
#with cm_timer_2():
#    time.sleep(5.5)