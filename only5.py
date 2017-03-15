# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:42:26 2017

@author: Prady
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank=comm.Get_rank()
if comm.Get_size()==5:
    print("Success!")    
else:
    if rank==0:
        print("Error: This program must run with 5 processes")
        
import numpy        
dot = numpy.array([0.])