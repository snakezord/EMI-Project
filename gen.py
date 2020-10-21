from random import *
import os
import errno

N_INPUT_FOLDERS = 10
N_INPUTS_MAX = 10000
n = 100

for x in range(N_INPUT_FOLDERS):
    j=0
    k=0
    l=0
    while(n < N_INPUTS_MAX):        
        if(n > 0 and n <= 1000):    #steps:       
            n = 100 + 100*(j)
            j += 1
        if(n > 1000 and n <= 10000):
            n = 500 + 500*(k)
            k += 1
        if(n > 10000 and n <= 100000):
            n = 1000 + 1000*(l)
            l += 1
        eps = 0.01                  #this values where never changed:
        maxr = n/2
        filename = "/Users/romanzhydyk/Desktop/MEI/projeto/newdata/input"+str(x+1)+"/data_"+str(n)+".in"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        f = open(filename,"w")
        f.write(str(eps) + " " + str(n))
        for i in range(n):
            f.write(" " + str(randint(1,maxr)))
        f.write("\n")

        f.close()
    n = 100