import numpy as np
from matplotlib import pyplot as plt

import sys
sys.path.insert(0,"/home/kasey/Okubo-test/")
import test_plot
reload(test_plot)

fname = 'test2.txt'

#test_val , dV = np.loadtxt(fname,unpack=True)
X , Y = [],[]
f = open(fname,'r')
total = 0
small = 0
large = 0
LIMIT = pow(10,-9)

for line in f:
	if len(line) <= 24:
		if len(line) >= 20:
			total+=1

			x = float(line.split()[0])
			y = float(line.split()[1])

			if abs(y) > LIMIT:

				X.append(x)
				Y.append(abs(y))
				large+=1


print "\nincluded fraction = "+str(float(large)/float(total))

plt.semilogy(X,Y,'.',c='r')

#### Histogram
NUM_BINS = 20
min_val,max_val = min(X),max(X)
dv_bin_vals,counts = test_plot.hist_1d(X,bmin=min_val,bmax=max_val,norm=True,num_bins=NUM_BINS) 

#FRAME_LIM = plt.ylim()[0]
FRAME_LIM = LIMIT
for k in range(NUM_BINS):
	if counts[k] < FRAME_LIM:
		counts[k] = FRAME_LIM

#### Put all outer values into the last bin
#small = total - large
#counts[-1] += small

A = plt.ylim()[1]

#### Plotting
plt.semilogy(dv_bin_vals,A*counts,color='k',ls='--')

"""
plt.tick_params(axis='y',bottom='off',top='off',right='off',
			labelbottom='off',labeltop='off',labelright='off')
plt.tick_params(axis='x',top='off')
plt.legend(loc=2)
img_ax		= plt.gca()
img_ax.set_xlabel(r'Cutoff values',labelpad=-1)
"""
plt.show()
