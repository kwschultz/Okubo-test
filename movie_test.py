#!/usr/bin/env python
import time
import sys
import numpy as np
import os

if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.cache')

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
"""from pyvc import vcplots
#******************************************
evnum = 109382
sim_file = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
#*******************************************
out_file      = 'local/dg_field_{}_test.png'.format(evnum)
vcplots.plot_event_field(sim_file,evnum,output_file=out_file,
						save_file_prefix='animation_test_g/field_values/'+str(evnum)+'_',
						field_type='gravity')
"""
#----------------------------------------------------------

#----------------------------------------------------------
from pyvc import *
from pyvc import vcplots
center_evnum 	= 109382    #pick a large event to be the centerpiece
duration		= 100 			# in years, make it small for test
sim_file		= 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'


vcanalysis.sim_info('ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5',show=20,)


"""
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
							animation_fps=30.0,field_type='gravity',force_plot=False)

print "Total time - {} seconds".format(time.time()-start_time)


"""

#----------------------------------------------------------
