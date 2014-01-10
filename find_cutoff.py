import numpy as np
from matplotlib import pyplot as plt

fname = 'potential_change_vs_sqrt_area_distance.txt'

#test_val , dV = np.loadtxt(fname,unpack=True)
test_val , dV = [],[]
f = open(fname,'r')
total = 0
small = 0
large = 0

for line in f:
	if len(line) == 22:
		total+=1

		x = float(line.split()[0])
		y = float(line.split()[1])

		if abs(y) > pow(10,-7):
			test_val.append(x)
			dV.append(abs(y))
			large+=1

"""print "Small = "+str(small)
print "Large = "+str(large)
print "total  = "+str(total)
print "large frac = "+str(float(large)/float(total))
"""
plt.semilogy(test_val,dV,'.')

plt.show()
