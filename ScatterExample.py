import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
LENGTH = 3

#create vector to divide
if rank == 0:
        #the size is determined so that length of recvbuf evenly divides the
        #length of sendbuf
        x = numpy.linspace(1,size*LENGTH,size*LENGTH)
else:
        #all processes must have a value for x
        x = None

#initialize as numpy array
x_local = numpy.zeros(LENGTH)

#all processes must have a value for x. But only the root process
#is relevant. Here, all other processes have x = None.
comm.Scatter(x, x_local, root=0)

#you should notice that only the root process has a value for x that
#is not "None"
print ("process {} x:{}".format(rank, x))
print ("process {} x_local:{}".format(rank, x_local))