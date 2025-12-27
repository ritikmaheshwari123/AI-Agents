## In python, modules and packages helps in organizing the code into manageable sections.
## A module is a single file (or files) that are imported under one import and used.
## A package is a collection of modules in directories that give a package hierarchy.

import math 

math.sqrt(16)  # Using the sqrt function from the math module

from math import sqrt,pi

print(sqrt(25))  # Using the sqrt function from the math module
print(pi)        # Using the pi constant from the math module

import numpy as np
np.array([1,2,3])

from math import *
sqrt(81)

from package.math import addition

print(addition(5,10))

from package.subpackage.subpacakge import printSubpackage

printSubpackage()