#!/usr/bin/env python
import time
import sys

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
#vcplots.plot_event_field('../VirtualCalifornia/test/test_dyn-0-5_st-5.h5',
#						'local/image0.png',event_number,
#						field_type='gravity')
#----------------------------------------------------------


#----------------------------------------------------------
#  Do a test animation
#from pyvc import *
#from pyvc import vcplots
#center_evnum 	= 487847    #pick a large event to be the centerpiece
#duration		= 25 			# in years, make it small for test
#sim_file		= 'path/to/sim.h5'
#with VCSimData() as sim_data:
#	sim_data.open_file(sim_file)
#	events			= VCEvents(sim_data)
#	center_evyear	= events.get_event_year(center_evnum)
#start_year	= round(center_evyear)-duration/2.0
#end_year	= round(center_evyear)+duration/2.0
#print 'start year: {},end year: {},duration: {}'.format(start_year,end_year,end_year-start_year)
#start_time	= time.time()
#output_directory = 'path/to/animation/directory/'  #All of the animation assets will be stored here
#event_range={'type':'year','filter':(start_year,end_year)}
#animation_target_length is in seconds
#animation_fps is frames per second
#vcplots.event_field_animation(sim_file,output_directory,event_range,animation_target_length=10.0,animation_fps=15.0,field_type='gravity')
#print "Total time - {} seconds".format(time.time()-start_time)
#----------------------------------------------------------


#---------------- Make histogram of delta g values to get an idea of spread
evnum 		= 247
sim_file 	= '../VirtualCalifornia/test/test_dyn-0-5_st-5.h5' 

def get_dg_values(evnum,sim_file):
	from pyvc import *
	from operator import itemgetter
	from pyvc import vcplots
	
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
		event_element_slips = events.get_event_element_slips(evnum)
		ele_getter = itemgetter(*event_element_slips.keys())
		event_element_data = ele_getter(geometry)
		if len(event_element_slips) == 1:
			event_element_data = [event_element_data]

	EF = vcplots.VCGravityField(min_lat, max_lat, min_lon, max_lon, base_lat, base_lon, padding=padding)

	EF.calculate_field_values(event_element_data, event_element_slips, cutoff=cutoff)

	return EF.dG.flatten()

def plot_dg_hist(evnum,sim_file,Nbins):
	import pylab as P
	
	dg = get_dg_values(evnum,sim_file)
	
	n, bins, patches = P.hist(dg, Nbins, normed=1, histtype='stepfilled')
	P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)
	P.savefig('local/dg_hist_ev'+evnum+'.png',dpi=200)
	P.show()
	

	



















#-----------------------------------------------------------------------------
if __name__ == "__main__":
	pass
	#do things here with the <args> that you want this to do:
	#  >>> python movie_test.py <args>
	
