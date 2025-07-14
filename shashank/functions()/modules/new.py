# from pgm1 import fun,fun1
# fun()
# fun1()

# from pgm1 import *   # to select all together
# fun()
# fun1()

# from pgm1 import fun,fun1
# from pgm2 import fun,fun1
# # fun()
# fun1()                             this kind of program over rides 1st statement
# fun()
# fun1()

import pgm1
import pgm2
pgm1.fun()
pgm1.fun1()
pgm2.fun()
pgm2.fun1()