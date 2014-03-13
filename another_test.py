from matplotlib import pyplot as plt

fig 		= plt.figure()

ax			= fig.add_axes((0.1,0.1,.9,.9))

ax.plot([0,1,2,3,4,5],[1,1,2,1,2,1])

cb_ax		= fig.add_axes((0.5,0.5,0.25,0.25))

cb_ax.plot([0,1,2,3,4,5],[1,1,2,1,2,1])

cb_tick_labs= [item.get_text() for item in ax.xaxis.get_ticklabels()]

for lab in cb_tick_labs:
	print labcb

plt.show()

