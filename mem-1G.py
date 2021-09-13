#!/usr/bin/python
import numpy
result = []
for i in range(1024) :
        result.append(numpy.random.rand(1024, 1024))
print (len(result))
