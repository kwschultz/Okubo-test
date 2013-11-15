#!/usr/bin/env python
import time
import sys
import numpy as np

sys.path.insert(0,"/home/kasey/PyVC/")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#If you want to adjust the look of the gravity plots all of the plot properties
#     are in the __init__ method of the VCGravityFieldPlotter class. These
#     settings will apply to the still images and the animations so you can
#     get the look right in a still before running the animation.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#----------------------------------------------------------
#  Look at sim info
#from pyvc import vcanalysis
#vcanalysis.sim_info('test_dyn-0-5_st-5.h5',show=2000)
#----------------------------------------------------------

#----------------------------------------------------------
#  Plot a still image of gravity change from 1 event
#from pyvc import vcplots
#event_number  = 487847
#out_file      = 'local/dg_field_{}.png'.format(event_number)
#sim_file      = 'demo_big.h5'
#vcplots.plot_event_field(sim_file,out_file,event_number,
#						field_type='gravity')
#----------------------------------------------------------

#----------------------------------------------------------
#******************************************
#evnum = 109382
#sim_file = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
#*******************************************
"""
from pyvc import *
from pyvc import vcplots
center_evnum 	= 109382    #pick a large event to be the centerpiece
duration		= 100 			# in years, make it small for test
sim_file		= 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
with VCSimData() as sim_data:
	sim_data.open_file(sim_file)
	events			= VCEvents(sim_data)
	center_evyear	= events.get_event_year(center_evnum)
start_year	= round(center_evyear)-duration/2.0
end_year	= round(center_evyear)+duration/2.0
print 'start year: {},end year: {},duration: {}'.format(start_year,end_year,end_year-start_year)
start_time	= time.time()
output_directory = 'animation_test_g'  #All of the animation assets will be stored here
event_range={'type':'year','filter':(start_year,end_year)}
#animation_target_length is in seconds
#animation_fps is frames per second
vcplots.event_field_animation(sim_file,output_directory,event_range,animation_target_length=60.0,
							animation_fps=30.0,field_type='gravity',force_plot=True)

print "Total time - {} seconds".format(time.time()-start_time)
"""
#----------------------------------------------------------



#---------------- Make histogram of delta g values to get an idea of spread
def get_dg_field(evnum,sim_file):
	from pyvc import *
	from operator import itemgetter
	from pyvc import vcplots
	import sys
	
	output_directory		= 'animation_test_g/'
	field_values_directory  = '{}field_values/'.format(output_directory)
	
	padding = 0.01
	cutoff	= None

	start_time = time.time()
	with VCSimData() as sim_data:
		sim_data.open_file(sim_file)	
		events = VCEvents(sim_data)
		geometry = VCGeometry(sim_data)
		min_lat = geometry.min_lat
		max_lat = geometry.max_lat
		min_lon = geometry.min_lon
		max_lon = geometry.max_lon
		base_lat = geometry.base_lat
		base_lon = geometry.base_lon
		event_data = events[evnum]
		
	
		EF = vcplots.VCGravityField(min_lat, max_lat, min_lon, max_lon, base_lat, base_lon, padding=padding)
			
		field_values_loaded = EF.load_field_values('{}{}_'.format(field_values_directory, evnum))
	
	if field_values_loaded:
		sys.stdout.write('loaded'.format(evnum))
		# If they havent been saved then we need to calculate them
	elif not field_values_loaded:
		sys.stdout.write('processing '.format(evnum))
		sys.stdout.flush()
						
		event_element_slips = events.get_event_element_slips(evnum)
		ele_getter = itemgetter(*event_element_slips.keys())
		event_element_data = ele_getter(geometry)
		if len(event_element_slips) == 1:
			event_element_data = [event_element_data]
						
		sys.stdout.write('{} elements :: '.format(len(event_element_slips)))
		sys.stdout.flush()
						
		EF.calculate_field_values(
			event_element_data,
			event_element_slips,
			cutoff=cutoff,
			save_file_prefix='{}{}_'.format(field_values_directory, evnum)
		)
	return EF,event_data[3]

#-----------------------------------------------------------------------------

def plot_dg_hist(evnum,sim_file,BINS=100):
	from matplotlib import pyplot as plt
	
	UNIT 				= pow(10,-8) #microgals
	
	event_field,mag		= get_dg_field(evnum,sim_file)
	dg          		= event_field.dG.flatten()
	dg_hist,bin_edges 	= np.histogram(dg/UNIT, bins=BINS, density=True, normed=True)
	
	x = np.linspace(bin_edges[0],bin_edges[-1],len(dg_hist))
	plt.clf()
	plt.figure()
	
	LABEL =	'M = '+str(round(mag,2))
	plt.plot(x,dg_hist,label=LABEL,color='g')
	plt.legend(loc=2)
	#plt.xlabel(r'$\Delta g \ [\mu gal]$')
	
	plt.savefig('local/dg_hist_ev'+str(evnum)+'.png',dpi=200)
	plt.clf()



#evnum = 487847
#sim_file = 'demo_big.h5'
#DG_MIN,DG_MAX = -25.0,25.0
#NBIN          = 100
#binner = np.linspace(DG_MIN,DG_MAX,NBIN)
#plot_dg_hist(evnum,sim_file,BINS=binner)

#evnum 		= 247
#sim_file 	= '../VirtualCalifornia/test/test_dyn-0-5_st-5.h5' 
#-----------------------------------------------------------------------------
#if __name__ == "__main__":
#	import sys
	#evnums 		= [247,326,101,269,220]
#	sim_file	= '../VirtualCalifornia/test/test_dyn-0-5_st-5.h5'
#	sim_file	= 'demo_big.h5'
#	plot_dg_hist(int(sys.argv[1]),sim_file,100)
	
	#do things here with the <args> that you want this to do:
	#  >>> python movie_test.py <args>
	
