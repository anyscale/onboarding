import ray
import time
import numpy as np

# note this is still single-threaded because of reliance on internal state (?)
@ray.remote
class Fibs():
    def __init__(self, n=1):
        self.a = 0
        self.b = 1

    def next(self):
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return c

    def next_n(self, n):
        for i in range(0,n):
            self.next()
        return self.b


# note - not a ray.remote
class TimeStamper:
    def __init__(self):
        self.times = np.array([time.time()])
    def __call__(self):
        self.times = np.append(self.times,time.time())
        self.times[-2] = self.times[-1] - self.times[-2]
    def __str__(self):
        return str(self.times[:-1])








