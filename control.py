import ray
import anyscale
import time
import numpy as np

from compute import Fibs

print("This demo connects to anyscale and computes fib sequences of 200 numbers serially and in different chatty ways")
anyscale.session("minimal").connect()

start = time.time()
times = np.array([])
times = np.append(times,time.time())

# iterate through a loop x times, running batches of size y
def runner(times, x,y):
    r = Fibs.remote()
    for i in range(0,x):
        final = r.next_n.remote(y)
    times = np.append(times,time.time())
    return times

print("Starting Run, generating one number with each invocation")
times = runner(times, 200,1)
print("Starting Run, generating ten numbers with each invocation")
times = runner(times, 20,10)
print("Starting Run, generating 100 numbers with each invocation")
times = runner(times, 2,100)
print("Starting Run, generating all 200 numbers in one go")
times = runner(times, 1,200)

times = times - start
deltas = [times[x] - times[x-1] for x in range(1,len(times))]

print(deltas)



