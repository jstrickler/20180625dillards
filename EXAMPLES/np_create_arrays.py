#!/usr/bin/env python
import numpy as np

# from nested sequences
a_nest = np.array([[1,2,3],[4,5,6],[7,8,9],[20,30,40]])
print(a_nest)
print("# dims", a_nest.ndim)
print("shape", a_nest.shape)
print()

# with zeros
a_zeros = np.zeros([3,5])
print(a_zeros)
print()

# with ones
a_ones = np.ones([2,3,4,5])
print(a_ones)
print()

# with uninitialized values
a_empty = np.empty([3,8])
print(a_empty)
