import ray
import anyscale
import os

from compute import Fibs, TimeStamper

print("This demo connects to anyscale and computes fib sequences")

# This command will use the environment variable RAY_ADDRESS 
# to connect to a ray cluster.
# If RAY_ADDRESS begins with "anyscale://" then your program 
# uses an Anyscale cluster to run Ray.
os.environ["RAY_ADDRESS"]="anyscale://cluster-1"
ray.client().connect()

# The connection can also be expressed in code
#ray.client("anyscale://cluster-1").connect()
# Depending on your cloud, you may need to specify a cluster_compute
#ray.client("anyscale://alt-region").cluster_compute("alt-region").connect()

# iterate through a loop x times, running batches of size y
@ray.remote
def run_job():
    timestamper = TimeStamper()

    def get_next_nth_fib(n,batch_size):
        fib_actor = Fibs.remote()
        fibs = []
        for i in range(0,n,batch_size):
            fibs.append(fib_actor.next_n.remote(batch_size))
        result = [ray.get(x) for x in fibs]
        timestamper()
        return result

    print("Generating one number with each invocation")
    print(get_next_nth_fib(2000,1))
    print("Generating ten numbers with each invocation")
    print(get_next_nth_fib(2000,10))
    print("Generating 100 numbers with each invocation")
    print(get_next_nth_fib(2000,100))
    print("Generating all 200 numbers in one go")
    print(get_next_nth_fib(2000,1))

    print(timestamper)


obj = run_job.remote()
ray.get(obj)



