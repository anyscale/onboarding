import ray
import anyscale
import time
import numpy as np

from compute import Fibs

print("This demo connects to anyscale and computes fib sequences of 200 numbers serially and in different chatty ways")
anyscale.session("onboard-test").connect()

class Ts:
    def __init__(self):
        self.times = np.array([time.time()])
    def __call__(self):
        self.times = np.append(self.times,time.time())
        self.times[-2] = self.times[-1] - self.times[-2]
    def __str__(self):
        return str(self.times[:-1])

ts = Ts()
# iterate through a loop x times, running batches of size y
def runner(x,y):
    r = Fibs.remote()
    for i in range(0,x):
        final = r.next_n.remote(y)
    ts()

print("Starting Run, generating one number with each invocation")
runner(200,1)
print("Starting Run, generating ten numbers with each invocation")
runner(20,10)
print("Starting Run, generating 100 numbers with each invocation")
runner(2,100)
print("Starting Run, generating all 200 numbers in one go")
runner(1,200)

print(ts)


