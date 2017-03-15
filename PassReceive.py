#passRandomArray.py
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = comm.Get_size()

randNum = numpy.zeros(n)

if rank == 1:
        randNum = numpy.random.random_sample(n)
        print ("Process {} drew the number {}".format(rank, randNum))
        comm.Send(randNum, dest=0)

if rank == 0:
    print ("Process {} before receiving has the number {}".format(rank, randNum))
    comm.Recv(randNum, source=1)
    print ("Process {} received the number {}".format(rank, randNum))
   