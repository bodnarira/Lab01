from contextlib import contextmanager
from threading import Lock

class RWLock:
    def __init__(self):
        self.w_lock = Lock()
        self.r_lock = Lock()
        self.r_count = 0

    def r_acquire(self):
        self.r_lock.acquire()
        self.r_count += 1
        if self.r_count == 1:
            self.w_lock.acquire()
        self.r_lock.release()

    def r_release(self):
        assert self.r_count > 0
        self.r_lock.acquire()
        self.r_count -= 1
        if self.r_count == 0:
            self.w_lock.release()
        self.r_lock.release()

    def w_acquire(self):
        self.w_lock.acquire()

    def w_release(self):
        self.w_lock.release()

    @contextmanager   # use with -WITH-
    def r_locked(self):
        try:
            self.r_acquire()
            yield
        finally:
            self.r_release()

    @contextmanager   # use with -WITH-
    def w_locked(self):
        try:
            self.w_acquire()
            yield
        finally:
            self.w_release()
            

class Level:
    def __init__ (self):
        self.rwlock = RWLock()
        
    def load (self):
        with self.rwlock.r_locked():
            # level is reading from the file
            pass
        
    def save (self):
        with self.rwlock.w_locked():
            # level is writing to the file
            pass
        
