import sys
sys.path.insert(0,"/home/kasey/Okubo-test/")
import test_plot
reload(test_plot)

import numpy as np
import os
import time
from matplotlib import pyplot as plt

sys.path.insert(0,"/home/kasey/PyVC/")
from pyvc import vcplots
from pyvc import vcanalysis
from pyvc import *

# Need to remove a cached file for Arial fonts to be used
if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.cache')
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

#sim_file             = '../VCModels/ALLCAL2_1-7-11_no-creep/ALLCAL2_1-7-11_no-creep_dyn-0-5_st-5.h5'
#sim_file = 'ALLCAL2_3_4_14_southern_SAF_no-creep_dyn-0-5_st-20_10000yr.h5'
#FIELD              = 'displacement'
#LENGTH          = 10.0
#FPS                   = 5.0
#FADE                = 1.0
#PLOT                = True
#MIN_MAG_MARK   = 6.5

duration           = 100.0             # in years, make it small for test
start_year         = 50.0
DT                 = 0.1
sim_time_range     = {'type':'year', 'filter':(start_year,start_year+duration)}
SOUTH_SAF_SECS     = {'filter':(13,14,15,16,17,18)}
sim_file           = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
#sim_file           = 'ALLCAL2_3_4_14_southern_SAF_no-creep_dyn-0-5_st-20_10000yr.h5'
#output_directory   = 'time_series_test/'
output_directory   = 'animation_south/'
#evnum              = 55
#out_file           = output_directory+'dg_field_'+str(evnum)+'.png'
FIELD              = 'gravity'
CUTOFF             = 1000.0
LENGTH             = 50.0
FPS                = 20.0
MAG_FILTER         = "<= 7.5"

#vcanalysis.sim_info(sim_file,show=35,section_filter=SOUTH_SAF_SECS,magnitude_filter=MAG_FILTER)

bad_evid = 191433
###   Event numbers selected as 10 events with largest magnitude <= 7.5 on southern SAF 
EVIDS_30    = [107556,183553,76977,33928,37557,252358,233381,225632,274396,77121,76324,138170,83894,171713,253346,4699,170663,35068,51659,67814,187742,143456,8877,9081,6348,269889,276933,150988,27209,197279]
EVIDS_10    = [107556,183553,76977,33928,37557,252358,233381,225632,274396,77121]

early    = [76977,33928,37557,77121,107556]
late     = [183553,252358,233381,225632,274396]
#extra = [188313,184777,13688,207677]

#event_range={'type':'year','filter':(2555,2655)}
#output_directory = 'animation_test_v/'
#vcplots.event_field_animation(sim_file, output_directory, event_range,
#    field_type='gravity', fringes=True, padding=0.08, cutoff=None,
#    animation_target_length=LENGTH/12.0, animation_fps = FPS, fade_seconds = 1.0,
#    min_mag_marker = 6.5, force_plot=True)

#vcplots.event_field_evolution(sim_file, output_directory, sim_time_range,
#    field_type='gravity', fringes=True, padding=0.08, cutoff=CUTOFF,
#    animation_target_length=LENGTH, animation_fps = FPS,
#    min_mag_marker = 5.5, start_year = start_year, duration=duration,section_filter=SOUTH_SAF_SECS,
#    force_plot=True)

#vcplots.average_field(sim_file,output_directory,EVIDS_10,field_type='gravity',pre=True,buffer=5.0,force_plot=True,section_filter=SOUTH_SAF_SECS,eq_slip_only=True,tag='eq')
vcplots.average_field(sim_file,output_directory,EVIDS_10,field_type='gravity',pre=True,buffer=5.0,force_plot=True,section_filter=SOUTH_SAF_SECS,backslip_only=True,tag='back')
vcplots.average_field(sim_file,output_directory,EVIDS_10,field_type='gravity',pre=True,buffer=5.0,force_plot=True,section_filter=SOUTH_SAF_SECS,eq_slip_only=True,tag='eq')



"""
with VCSimData() as sim_data:
    sim_data.open_file(sim_file)
    geometry    = VCGeometry(sim_data)
    events      = VCEvents(sim_data)
    event_data = events.get_event_data(['event_magnitude', 'event_year', 'event_number'], event_range=sim_time_range)
    
    slip_rates  = geometry.get_slip_rates()
    
    event_element_slips = {evid:events.get_event_element_slips(evid) for evid in event_data['event_number']}
    
    #avg_slip    = geometry.get_average_slip_time_series(event_data,event_element_slips,start_year=start_year,duration=duration,section_filter=SOUTH_SAF_SECS)
    
    #max_rate = []
    #avg_rate = 0.0
    #for bid in slip_rates.keys():
    #    rate = slip_rates[bid]
    #    avg_rate += rate
    #    if max_rate == []:
    #        max_rate = [bid,rate]
    #    else:
    #        if rate > max_rate[1]:
    #            max_rate = [bid,rate]
                
    #avg_rate /= float(len(slip_rates.keys()))
    
    #print "max rate: ",max_rate[1]
    #print "section:  ",geometry.get_section_name(geometry.sections_with_elements([max_rate[0]])[0])
    #print "avg_rate: ",avg_rate
    #print "max rate: ",max_rate[1]/avg_rate," avg_rate"

time_values = np.arange(start_year+DT,start_year+duration+DT,DT)

plt.clf()
plt.plot(time_values,avg_slip)
plt.title("Average time dependent slip on southern SAF")
plt.grid(True)
plt.xlabel("Simulated time")
plt.ylabel("Average slip(t) [m]")
plt.savefig("avg_slip.png",dpi=300)
"""


"""
# event_element_slips = dictionary indexed by event_id with entries being dictionaries of slips indexed by block_id
# slip_time_series    = dictionary indexed by block_id with entries being arrays of absolute slip at each time step

#-------------------------------------------------------------------------------
def get_slip_time_series(events,slip_rates,event_range,section_filter=None):
    import pickle
    
    # Convert slip rates from meters/second to meters/(decimal year)
    CONVERSION = 3.15576*pow(10,7)
    DT         = 0.1 # 0.1yr evaluates field every 36.5 days
    
    with VCSimData() as sim_data:
        sim_data.open_file(sim_file)
    
        geometry            = VCGeometry(sim_data)
        events              = VCEvents(sim_data)
        slip_rates          = geometry.get_slip_rates(section_filter=section_filter)

        if section_filter is not None:
            events_in_range = events.get_event_data(['event_number', 'event_year','event_magnitude'],
                                                      event_range = event_range,section_filter=section_filter)
        else:
            events_in_range = events.get_event_data(['event_number', 'event_year','event_magnitude'],
                                                      event_range = event_range)
        
        event_element_slips = {evid:events.get_event_element_slips(evid) for evid in events_in_range['event_number']}

    #Initialize blocks with 0.0 slip at time t=0.0
    slip_time_series = {block_id:[0.0] for block_id in slip_rates.keys()}


    #Initialize time steps to evaluate slip    
    time_values = np.arange(start_year+DT,start_year+duration+DT,DT)

    for k in range(len(time_values)):
        if k>0:
            # current time in simulation
            right_now = time_values[k]
        
            # back slip all elements by subtracting the slip_rate*dt
            for block_id in slip_time_series.keys():
                last_slip = slip_time_series[block_id][k-1]
                this_slip = slip_rates[block_id]*CONVERSION*DT
                slip_time_series[block_id].append(last_slip-this_slip)

            # check if any elements slip as part of simulated event in the window of simulation time
            # between (current time - DT, current time), add event slips to the slip at current time 
            # for elements involved
            for evid in events_in_range['event_number']:
                if right_now-DT < events_in_range['event_year'][evid] <= right_now:
                    for block_id in event_element_slips[evid].keys():
                        slip_time_series[block_id][k] += event_element_slips[evid][block_id]
                               
    out = open(outfile,'wb')                                         
    pickle.dump(slip_time_series,out)
    out.close()
#------------------------------------------------------------------------------ 
"""


        
"""
for event in events_in_range['event_number']:
    print "\nevent_id : %i\t year : %.5f\t magnitude : %.4f\t"%(event,events_in_range['event_year'][event],events_in_range['event_magnitude'][event])
    print "involved elements: "+str(sorted(event_element_slips[event].keys()))
"""


"""
    for block_id in slip_time_series.keys():
        this_series = slip_time_series[block_id]
        this_filename = output_directory+'element_'+str(block_id)+'_slips.png'

        plt.clf()
        plt.cla()
        plt.plot(time_values,this_series,label="element "+str(block_id))
        plt.axhline(y=0,xmin=0.0,xmax=time_values[-1],ls='--',color='k',lw=2)
        plt.xlabel('simulated time [decimal years]')
        plt.ylabel('accumulated slip on element [meters]')
        plt.legend()
        plt.savefig(this_filename,dpi=200)
        print "written to: "+this_filename
        
"""
    
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












