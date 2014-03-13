import sys
sys.path.insert(0,"/home/kasey/Okubo-test/")
import test_plot
reload(test_plot)

import numpy as np
import os
import time


sys.path.insert(0,"/home/kasey/PyVC/")
from pyvc import vcplots
from pyvc import *

# Need to remove a cached file for Arial fonts to be used
if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.ca30che')
#=============================================================================




"""
#        DATA
DTTF        = [1000.0,1000.0,1000.0]   # depth to top of fault (Okubo's style)
_DIP        = [np.pi/2.0,np.pi/3.0,np.pi/6.0]
#_DIP        = [np.pi/5.0,np.pi/10.0,np.pi/4.0]
_L          = [10000.0,10000.0,10000.0]
_W          = [10000.0,10000.0,10000.0]
_C          = [DTTF[i] + _W[i]*np.sin(_DIP[i]) for i in range(len(_L))]   #meters
_US         = [5.0,0.0,0.0]
_UD         = [0.0,-5.0,5.0]
_UT         = [0.0,0.0,0.0]
_LAMBDA     = 3.2e10
_MU         = 3.0e10
_Xmin,_Xmax = [-20000.0,-20000.0,-20000.0],[30000.0,30000.0,30000.0]
_Nx         = 3000.0
_Ymin,_Ymax = [-25000.0,-25000.0,-25000.0],[25000.0,25000.0,25000.0]
_Ny         = 3000.0

##        SWITCHES
#*******************
SAVE         = True
_DV          = False
_DG          = True
_DZ          = False
_CLIMITS     = True
_suffix     = 'dg_paper_HIres'
_HIST        = False
_SHOW        = False
_NO_LABELS  = True
NUM_TICKS   = 7
FRAME_FONT  = 12
TICK_FONT   = 12
#*******************
for k in range(3):
	test_plot.cbar_plot(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],_DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],_LAMBDA,_MU,save=SAVE,DG=_DG,DZ=_DZ,CLIMITS=_CLIMITS,SUFFIX=_suffix,HIST=_HIST,SHOW=_SHOW,DV=_DV,NOLABELS=_NO_LABELS,frame_font=FRAME_FONT,tick_font=TICK_FONT,num_ticks=NUM_TICKS)
"""



#------------------------------------------------------------------------------
##  ANIMATION SWITCHES & KNOBS
#******************************
#center_evnum = 91382    #pick a large event to be the centerpiece
duration           = 100.0             # in years, make it small for test
start_year         = 0.0
EVENT_RANGE        = {'type':'year', 'filter':(start_year,start_year+duration)}
#sim_file          = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
sim_file             = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
#FIELD              = 'displacement'
#LENGTH          = 10.0
#FPS                   = 5.0
#FADE                = 1.0
#PLOT                = True
#MIN_MAG_MARK   = 6.5
output_directory      = 'animation_test_d/'
text_out          = 'slip_time_series.txt'

event_element_slips = {}
slip_time_series = {}

#
with VCSimData() as sim_data:
    sim_data.open_file(sim_file)
    
    geometry            = VCGeometry(sim_data)
    events              = VCEvents(sim_data)
    slip_rates          = geometry.get_slip_rates()
    events_in_range     = events.get_event_data(['event_number', 'event_year'],event_range = EVENT_RANGE)
    
    for evid in events_in_range['event_number']:
        this_event_element_slips = events.get_event_element_slips(evid)
        event_element_slips[evid] = this_event_element_slips
                
sim_time   = 0.0
DT         = 0.1 # 0.1yr evaluates field every 36.5 days

for block_id in slip_rates.keys():
    slip_time_series[block_id] = 0.0
    
time_values = np.arange(sim_time+DT,sim_time+duration+DT,DT)

for t in time_values:
    events_this_period = []
    for evid in events_in_range['event_number']:
        if t-DT < events_in_range['event_year'][evid] <= t+DT:
            events_this_period.append(evid)
            
        #loop over blocks and subtract slip_rate*dt to each
        #for those involved in events, add their event slips
        #append the total value to slip_time_series[block_id]
            
    
    
    
    
    #events         = VCEvents(sim_data)
    #center_evyear  = events.get_event_year(center_evnum)
#start_year         = round(center_evyear)-duration/2.0
#end_year           = round(center_evyear)+duration/2.0
#
#start_year  = 0.0
#end_year    = 100.0
#event_range={'type':'year','filter':(start_year,end_year)}

#vcplots.event_field_animation(sim_file, output_directory, event_range,
#    field_type=FIELD, fringes=True, padding=0.08, cutoff=None,
#    animation_target_length=LENGTH, animation_fps = FPS, fade_seconds = FADE,
#    min_mag_marker = MIN_MAG_MARK, force_plot=PLOT)
#------------------------------------------------------------------------------




#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
#sim_file = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
sim_file     = '/home/kasey/Okubo-test/ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
evnum      = 109382  # Mag = 8.0
#evnum      = 1455      # Mag = 7.83
#evnum      = 48467  # Mag = 7.99
#evnum      = 49261  # Mag = 7.63
#evnum       = 54526  # Mag = 7.73
#evnum      = 54358 # Mag = 7.79
out_file     =  '/home/kasey/Okubo-test/dg_plots/dg_'+str(evnum)+'_match.png'
FRINGES = True
FIELD       = 'gravity'
LAT_RANGE = (30.65,42.85)
LON_RANGE = (-125.52,-113.24)

#if FIELD == 'gravity':
#    FIELD_VALUE_DIR = 'animation_test_g'
#elif FIELD == 'displacement':
#    FIELD_VALUE_DIR = 'animation_test_d'
#elif FIELD == 'potential':
#    FIELD_VALUE_DIR = 'animation_test_v'


vcplots.plot_event_field(sim_file, evnum, output_file=out_file, field_type=FIELD,
                         fringes=FRINGES, padding=0.08, cutoff=None, save_file_prefix=None,
                         custom_lat_range=LAT_RANGE,custom_lon_range=LON_RANGE)
#------------------------------------------------------------------------------
"""


"""
sim_file = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
event_range={'type':'year','filter':(0,105)}
output_directory = 'animation_test_v/'
vcplots.event_field_animation(sim_file, output_directory, event_range,
    field_type='potential', fringes=True, padding=0.08, cutoff=None,
    animation_target_length=10.0, animation_fps = 2.0, fade_seconds = 1.0,
    min_mag_marker = 5.5, force_plot=True)
"""


"""
for k in range(len(_C)):
    test_plot.plot_for_cutoff(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],
                        _DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],
                        _LAMBDA,_MU,save=SAVE,SHOW=_SHOW,_CLIMS=_CLIMITS)
"""

"""
#=============================================================================
for k in range(3):
    # Need to remove a cached file for Arial fonts to be used
    if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
    
    test_plot.cbar_plot(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],
                        _DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],
                        _LAMBDA,_MU,save=SAVE,DG2=_DG2,DG=_DG,DZ=_DZ,
                        DH=_DH,DIFFZ=_DIFFZ,DIFFG=_DIFFG,CLIMITS=_CLIMITS,
                        SUFFIX=_suffix,HIST=_HIST,SHOW=_SHOW)

#111111111111111111111111111111111111111111111

center_evnum 	= 109382    #pick a large event to be the centerpiece
duration		= 100 			# in years, make it small for test
sim_file		= 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
with VCSimData() as sim_data:
	sim_data.open_file(sim_file)
	events			= VCEvents(sim_data)
	center_evyear	= events.get_event_year(center_evnum)
start_year	= round(center_evyear)-duration/2.0
end_year	= round(center_evyear)+duration/2.0
#print 'start year: {},end year: {},duration: {}'.format(start_year,end_year,end_year-start_year)
start_time	= time.time()

output_dir  = '../Dropbox/UCD/Stat_Mech_219B/'
tags        = ['mag_area','slip_rupture_length','frequency_mag','recurrence']
output_files= []
for k in range(len(tags)):
    fname = output_dir+tags[k]+'_'+str(duration)+'_ALLCAL2_nocreep.png'
    output_files.append(fname)
    

event_range={'type':'year','filter':(start_year,end_year)}

vcplots.magnitude_rupture_area(sim_file,output_files[0],event_range=event_range)
vcplots.average_slip_surface_rupture_length(sim_file,output_files[1],event_range=event_range)
vcplots.frequency_magnitude(sim_file,output_files[2],event_range=event_range)
#vcplots.plot_recurrence_intervals(sim_file,output_file=output_files[3],event_range=event_range)


print "Total time - {} seconds".format(time.time()-start_time)

"""












