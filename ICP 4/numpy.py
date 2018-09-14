# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:31:32 2018

@author: farid
"""

import numpy as np
a=np.random.randint(20,size=(15))
counts = np.bincount(a)
print (a)
print (np.argmax(counts))