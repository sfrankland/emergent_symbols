import sys
import random
import numpy as np

# Prevent python from saving out .pyc files
sys.dont_write_bytecode = True
# Logging utility
from util import log

# Task generator
def create_task(args, train_shapes, test_shapes):

#generate codes for numbers.
	max_int = 50
	#size
	S=20
	k = np.random.randint(2, size=(max_int, S))

	#the "add 1" problem
	ones_x_=np.empty([max_int, S*2 + 4])
	ones_y_=np.empty([max_int, S])

# #the "add 2" problem.
	twos_x_=np.empty([max_int, S*2 + 4])
	twos_y_=np.empty([max_int, S])

for i in range(0,max_int-2):
    #add one
    ones_x_[i,:] = np.concatenate((k[i,:], k[0,:], [1,0,0,1]))
    #add two
    twos_x_[i,:] = np.concatenate((k[i,:], k[1,:], [0,1,1,0]))
    #add 1: target is i+1
    ones_y_[i,:] = k[i+1,:]
    #add 2: target is i+2
    twos_y_[i,:] = k[i+2,:]

	# Create training and test sets
	train_set = {'seq_ind': all_train_seq, 'y': all_train_targ}
	test_set = {'seq_ind': all_test_seq, 'y': all_test_targ}

	return args, train_set, test_set