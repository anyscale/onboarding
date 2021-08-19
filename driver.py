import ray
import anyscale
import os

from compute import run_job

print("This demo connects to anyscale and computes fib sequences")

# This command will use the environment variable RAY_ADDRESS 
# to connect to a ray cluster.
# If RAY_ADDRESS begins with "anyscale://" then your program 
# uses an Anyscale cluster to run Ray.
ray.init()

N = 200
print(f"Getting the {N}th fibonnaci number for you, a few times")
ray.get([run_job.remote(N) for i in range(5)])



