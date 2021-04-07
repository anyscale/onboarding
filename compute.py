import ray

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
        for i in range(1,n):
            self.next()
        return self.b









