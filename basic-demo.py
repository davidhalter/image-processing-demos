#!/usr/bin/env python
from pylab import *
import time

o = ones((100, 100))

for i in range(100):
    o[:,i] = i*0.1;
    
o[6:8,:] = 0;
o[5:6,:] = 0.5;
o[15:16,:] = 1.5;

print o
print matrix('1 2 3;3 2 1')

stacked = vstack((o,o[:30]))
print shape(stacked)
imshow(stacked)

show()