import ray
import anyscale

from compute import Fibs, TimeStamper

print("This demo connects to anyscale and computes fib sequences of 200 numbers serially and in different chatty ways")

# This command will use the environment variable RAY_ADDRESS to connect to a ray cluster
# If the URL begins with "anyscale://" then your program uses an Anyscale cluster.
ray.client().connect()

# The connection can also be expressed in code
#ray.client("anyscale://cluster-1").cluster_compute("anastasia_def").connect()

# iterate through a loop x times, running batches of size y
def get_next_nth_fib(n,batch_size):
    fib_actor = Fibs.remote()
    fibs = []
    for i in range(0,n):
        fibs.append(fib_actor.next_n.remote(batch_size))
    result = [ray.get(x) for x in fibs]
    timestamper()
    return result

@ray.remote
def run_job():
    timestamper = TimeStamper()
    print("Starting Run, generating one number with each invocation")
    print(get_next_nth_fib(200,1))
    print("Starting Run, generating ten numbers with each invocation")
    print(get_next_nth_fib(20,10))
    print("Starting Run, generating 100 numbers with each invocation")
    print(get_next_nth_fib(2,100))
    print("Starting Run, generating all 200 numbers in one go")
    print(get_next_nth_fib(1,200))

    print(timestamper)
    
ray.get(run_job.remote())


