import ray
import anyscale
import os

from compute import run_job

print("This demo connects to anyscale and computes fib sequences")

# This command will use the environment variable RAY_ADDRESS 
# to connect to a ray cluster.
# If RAY_ADDRESS begins with "anyscale://" then your program 
# uses an Anyscale cluster to run Ray.
os.environ["RAY_ADDRESS"]="anyscale://cluster-2"
ray.client().connect()

# The connection can also be expressed in code
#ray.client("anyscale://cluster-1").connect()
# Depending on your cloud, you may need to specify a cluster_compute
#ray.client("anyscale://alt-region").cluster_compute("alt-region").connect()


N = 20000
print("Getting the {N}th fibonnaci number for you, a few times")
obj = run_job.remote(N)
ray.get(obj)



