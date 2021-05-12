import time
from mpi4py import MPI

from logger import log

RING = {
    0: 1,
    1: 2,
    2: 3,
    3: 0
}


class MPIInstance:
    def __init__(self):
        self.comm = MPI.COMM_WORLD
        self.size = self.comm.Get_size()
        self.rank = self.comm.Get_rank()
        self.elected = False


    def receive(self):
        data = self.comm.recv()
        log(f"{self.rank} received a {data['tag']}"
            f" message from {data['sender']}.")

        time.sleep(0.1)
        return data

    def send(self, data):
        self.comm.send(data, dest=RING[self.rank], tag=0)
