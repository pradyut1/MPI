import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n = comm.Get_size()


randNum = numpy.zeros(1)

if rank!=n-1:
    randNum=numpy.random.random_sample(1)
    print ("Process {} drew the number {}".format(rank, randNum[0]))
    comm.Send(randNum,dest=rank+1)
    
else:
    randNum=numpy.random.random_sample(1)
    print ("Process {} drew the number {}".format(rank, randNum[0]))
    comm.Send(randNum,dest=0)
    
        

if rank!=0:
    comm.Recv(randNum,source=rank-1)
    print ("Process {} received the number {}".format(rank, randNum[0]))
else:
    comm.Recv(randNum,source=n-1)
    print ("Process {} received the number {}".format(rank, randNum[0]))




