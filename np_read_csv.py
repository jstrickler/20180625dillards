#!/usr/bin/env python
import numpy as np

a = np.loadtxt(
    'DATA/columns_of_numbers.txt',
    usecols=[1, 3],
    skiprows=1,
    dtype=np.int32
)

print(a)
print(a.shape)
print(a.size)


