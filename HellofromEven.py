# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:08:00 2016

@author: Prady
"""
from mpi4py import MPI
comm = MPI.COMM_WORLD
if comm.Get_rank()%2==0:
    print ("hello from process {}".format(comm.Get_rank()))
else:
    print ("Goodbye from process {}".format(comm.Get_rank()))


