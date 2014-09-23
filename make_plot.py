import sys
import test_plot
reload(test_plot)

import numpy as np
import os
import time
from matplotlib import pyplot as plt

sys.path.insert(0,"/home/kasey/PyVC/")
from pyvc import vcplots
from pyvc import vcanalysis
from pyvc import vcutils
from pyvc import *

# Need to remove a cached file for Arial fonts to be used
if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.cache')
#=============================================================================


#M0 = 4.0*pow(10,20)
#print test_plot.mag_from_moment(M0)

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
_Xmin,_Xmax = [-30000.0,-30000.0,-30000.0],[40000.0,40000.0,40000.0]
_Nx         = 3000.0
_Ymin,_Ymax = [-35000.0,-35000.0,-35000.0],[35000.0,35000.0,35000.0]
_Ny         = 3000.0

##        SWITCHES
#*******************
SAVE         = True
_CLIMITS     = True
_suffix      = 'dg_dilat_paper'
field_type   = 'dilat_gravity'
_HIST        = False
_SHOW        = False
_NO_LABELS   = True
NUM_TICKS    = 7
FRAME_FONT   = 14
TICK_FONT    = 14
FREE_AIR     = False
XTICKS       = False
#*******************
for k in range(3):
	test_plot.cbar_plot(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],_DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],_LAMBDA,_MU,save=SAVE,CLIMITS=_CLIMITS,SUFFIX=_suffix,HIST=_HIST,SHOW=_SHOW,NOLABELS=_NO_LABELS,frame_font=FRAME_FONT,tick_font=TICK_FONT,num_ticks=NUM_TICKS,field_type=field_type,x_ticks=XTICKS,CBAR='bottom')
"""


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
#evnum              = 55
#out_file           = output_directory+'dg_field_'+str(evnum)+'.png'
FIELD              = 'gravity'
#CUTOFF             = 1000.0
CUTOFF             = None
LENGTH             = 50.0
FPS                = 20.0
MAG_FILTER         = "<= 7.0"

TEJON     = {'filter':(14,15)}
SF        = {'filter':(1,2,3,4,5,6,7,8,9,10)}
LP        = {'filter':(7,8,9,10)}
NR        = {'filter':[52]}
LA        = {'filter':(148,30)}
SECS      = [TEJON,SF,NR,LA]
SHOW      = 20
"""

#el_mc_evnum = 96646
# -------------------- Forecasting ---------------
sim_file  = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'

BAJA      = {'filter':(16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 56, 57, 69, 70, 73, 83, 84, 92, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 123, 124, 125, 126, 149)}
NORCAL    = {'filter':(1,2,3,4,5,6,7,8,9,10,36,38,39,40,41,42,43,44,45,46,47,48,49,50,51,138,139,140,141,142,167,168,169,170,171,172,181)}
sec_list = list(np.arange(181)+1)
sec_list.remove(11)
sec_list.remove(12)
sec_list.remove(19)
ALLCAL    = {'filter':sec_list}
NAPA =  {'filter':(50,44,45,169,170,171)}

###############
baja    = False
norcal  = False
napa    = True
loma_napa = False
allcal  = False
WEIBULL = True
MAGS    = ">= 6.0"
name    = "PAPER"
duration= 30000.0
#t_and_t0 = (3.0,4.0)
t_and_t0 = None
###############

if baja:
    start_year   = 17831.6  #Baja
    TAG          = 'baja_'+str(int(duration/1000.0))+'k_'+name+'_M'+MAGS.split()[-1]
    SECS         = BAJA
    DT           = 30.0
    #years_since  = 3.0
    years_since = 4.0
    
    
    if MAGS.split()[-1] == "7.5":
        BETA         = 1.2544
        TAU          = 129.5127
    elif MAGS.split()[-1] == "7.0":
        BETA         = 1.1018
        TAU          = 23.3027
        
elif allcal:
    start_year = 10000.0
    TAG        = 'allcal_'+str(int(duration/1000.0))+'k_'+name+'_M'+MAGS.split()[-1]
    SECS       = ALLCAL
    DT         = 30.0
    years_since = 62.0
    
    if MAGS.split()[-1] == "7.5":
        BETA         = 1.2004
        TAU          = 62.2997
    elif MAGS.split()[-1] == "7.0":
        BETA         = 1.0331
        TAU          = 10.3647
    
elif norcal:
    TAG         = 'norcal_'+str(int(duration/1000.0))+'k_'+name+'_M'+MAGS.split()[-1]
    SECS        = NORCAL
    DT          = 30.0
    #years_since = 0.0
    
    if MAGS.split()[-1] == "7.5":
        BETA         = 1.2966
        TAU          = 110.3578
        start_year   = 2380.8
        years_since = 108.0     
    elif MAGS.split()[-1] == "7.0":
        BETA         = 1.0973
        TAU          = 20.5765
        start_year   = 3115.5
        years_since  = 25.0 
    elif MAGS.split()[-1] == "7.3":
        BETA         = 1.1007
        TAU          = 41.3967
        start_year   = 2380.8
        years_since = 108.0  
    elif MAGS.split()[-1] == "7.4":
        BETA         = 1.1299
        TAU          = 63.8740
        start_year   = 2380.8 
        years_since = 108.0 
        
elif napa:
    start_year = 7716.0
    TAG        = 'napa_'+str(int(duration/1000.0))+'k_'+name+'_M'+MAGS.split()[-1]
    SECS       = NAPA
    DT         = 30.0
    years_since = 0.0
    
    if MAGS.split()[-1] == "6.0":
        BETA         = 0.9688
        TAU          = 33.3166
    elif MAGS.split()[-1] == "6.5":
        BETA         = 1.0755
        TAU          = 46.0693
            
        
elif loma_napa:
    start_year = 10138.8
    TAG        = 'loma_napa_'+str(int(duration/1000.0))+'k_'+name+'_M'+MAGS.split()[-1]
    SECS       = NAPA
    DT         = 30.0
    years_since = 0.0
    
    if MAGS.split()[-1] == "6.0":
        BETA         = 0.9784
        TAU          = 33.2155
        
"""
Napa        
=======================================
899 earthquakes 
---------------------------------------
avg interval	max interval
33.28		216.20
---------------------------------------
For t0 = 0.00 years
25% waiting time: 10.00 years
50% waiting time: 22.00 years
75% waiting time: 49.00 years
=======================================
"""
        

        
"""
Loma -> Napa
908 earthquakes 
---------------------------------------
avg interval	max interval
32.97		216.20
---------------------------------------
For t0 = 0.00 years
25% waiting time: 10.00 years
50% waiting time: 22.00 years
75% waiting time: 49.00 years
"""

"""
NorCal M>7.0
1520 earthquakes 
---------------------------------------
avg interval	max interval
19.71		190.42
---------------------------------------
For t0 = 11.00 years
25% waiting time: 6.00 years
50% waiting time: 13.00 years
75% waiting time: 24.00 years
"""
    

EV_RANGE    = {'type':'year', 'filter':(start_year,start_year+duration)}
vcplots.forecast_plots(sim_file, event_graph_file=None, event_sequence_graph_file=None, event_range=EV_RANGE, section_filter=SECS, magnitude_filter=MAGS, padding=0.08, fixed_dt=DT,weibull=WEIBULL,fname_tag=TAG,beta=BETA,tau=TAU,year_eval=years_since,P_t_t0_eval=t_and_t0)

#test_plot.fit_to_weibull(sim_file,BETA,TAU,event_range=EV_RANGE,magnitude_filter=MAGS,section_filter=SECS)

# ----------------- End Forecasting ---------------






# ----------------- Plotting event fields ---------------
"""
#plot_ids = [193054,9940,96646]
#plot_ids = [60019,231185,193054]
#tags     = ["Tejon_paper_20mugal","SF_paper_20mugal","Northridge_paper_20mugal"]
#plot_ids = [53043,53344]
#tags     = ["Loma_Prieta_candidate","Napa_candidate"]
plot_ids = [231185,96646]
tags     = ["SF_poster","ElMC_poster"]
CUTOFF   = None
FIELD    = 'dilat_gravity'
LAT_LON  = False
FRINGES  = True
HIRES    = True

for k in range(len(plot_ids)):
    TAG = tags[k]
    evid= plot_ids[k]
    
    vcplots.plot_event_field(sim_file, evid, 'local/', field_type=FIELD, padding=0.08, cutoff=CUTOFF,tag=TAG,lat_lon=LAT_LON,fringes=FRINGES,hi_res=HIRES)
"""
# ----------------- END Plotting event fields -----------





"""
for k in range(len(TAGS)):
    TAG = TAGS[k]
    EV_RANGE    = {'type':'year', 'filter':(start_year,start_year+(k+1)*10000)}
    vcplots.forecast_plots(sim_file, event_graph_file=None, event_sequence_graph_file=None, event_range=EV_RANGE, section_filter=SECS, magnitude_filter=MAGS, padding=0.08, fixed_dt=30.0,fname_tag=TAG)
    #vcplots.plot_forecast(sim_file, event_graph_file=None, event_sequence_graph_file=None, event_range=EV_RANGE, section_filter=NORCAL, magnitude_filter=MAGS, padding=0.08, fixed_dt=30.0,output_file="local/"+TAG+"_forecast.png")
"""



#SF_ids = [9940,71369,53163,69060,82904]
#for evid in SF_ids:
#    TAG = 'sf_search'
#    vcplots.plot_event_field(sim_file, evid, 'local', field_type='gravity', padding=0.08, cutoff=CUTOFF,tag=TAG)

#vcanalysis.event_sections(sim_file,el_mc_evnum)

#vcanalysis.cum_prob(sim_file, output_file, event_range=EV_RANGE, section_filter=BAJA, magnitude_filter=MAG_FILTER,plot_type=PLOT_TYPE)


# num       year      mag       slip [m]  rupt.len [km]
# 96646     17831.57  7.28      0.82      138.43
#vcplots.plot_event_field(sim_file, evnum, 'local', field_type='displacement', padding=0.08, cutoff=CUTOFF,tag=TAG)

#----------------- EQ hunting --------------------
"""
Napa_only_events = [168097, 6478, 197127, 123267, 267261, 186946, 39569, 251833, 247140, 8148, 176612, 103919, 171869, 18164, 146039, 50036, 107992, 59996]
Napa_only_years = [30491.240338917687, 1747.5899074185204, 35693.370627909986, 22529.086708134993, 48139.093874213759, 33883.849702347077, 7715.4004976180586, 45410.922680991636, 44567.554570983062, 2060.4421738168362, 32027.627820965194, 19116.453701417951, 31190.642924825341, 3882.1632034263889, 26577.658460504372, 9565.6155153407308, 19849.030083585647, 11339.761605784435]

Loma_events = [52095,194106,227982,233975,240651,138797,215928,10894,251303,53043,125265]
Loma_years  = [9901.2323535322394, 35168.138523346599, 41203.639369679993, 42270.534455852081, 43429.681499054794, 25254.743279807106, 39080.608740562078, 2566.2828671653174, 45326.887758374956, 10084.091735158539, 22872.440635772586]

Loma =  {'filter':(9,181)}
Napa =  {'filter':[50]}
mendo = {'filter':[1,159,160,161,162,163,164,165]}
sf_bay = {'filter':[5,6,7,42,43,36,140]}
MAGS = "<= 7.1"
index = 8
#start_year = Loma_years[index]
#end_year   = start_year + 75.0
start_year = 50.0
end_year = 19900.0
MIN_MAG = 6.8

#with VCSimData() as sim_data:
#    sim_data.open_file(sim_file)
#    events			= VCEvents(sim_data)
#    for evid in Loma_events:
#        year = events.get_event_year(evid)
#        Loma_years.append(year)
    
#print "\nLoma eivd-year = {}-{}\n".format(Loma_events[index],start_year)

these_ev = vcanalysis.detailed_sim_info(sim_file,show=20,section_filter=Loma,magnitude_filter=MAGS,event_range={'type':'year', 'filter':(start_year,end_year)},return_evnums=True,min_mag=MIN_MAG)

#print "\n",these_ev

for evnum in these_ev:
    vcanalysis.event_sections(sim_file,evnum)
print "\n"

#vcanalysis.event_sections(sim_file,53043)
#vcanalysis.event_sections(sim_file,53344)

# Forecast after Napa only (not after Napa and Loma)
#num       year      magnitude slip [m]  rupt.len [km]
#39569     7715.40   6.06      0.23      24.04

# Forecast after Loma Prieta then Napa
# num       year      magnitude slip [m]  rupt.len [km]
# 53043     10084.09  6.83      0.44      57.34         (Loma Prieta like)
# 53344     10138.01  5.08      0.05      3.00          (Napa like)
"""
#------------------- EQ hunting --------------------


"""
bad_evid = 191433
###   Event numbers selected as 10 events with largest magnitude <= 7.5 on southern SAF 
EVIDS_30    = [107556,183553,76977,33928,37557,252358,233381,225632,274396,77121,76324,138170,83894,171713,253346,4699,170663,35068,51659,67814,187742,143456,8877,9081,6348,269889,276933,150988,27209,197279]
EVIDS_10    = [107556,183553,76977,33928,37557,252358,233381,225632,274396,77121]

early    = [76977,33928,37557,77121,107556]
late     = [183553,252358,233381,225632,274396]
#extra = [188313,184777,13688,207677]

"""
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

"""
output_directory   = 'post_5_eq_fields/'

BUFFER             = 5.0
CUTOFF             = 1000.0
PRE1               = False
PRE2               = True
BACK1              = False
BACK2              = False
EQ1                = False
EQ2                = False
SECS               = (SOUTH_SAF_SECS,SOUTH_SAF_SECS)
field1dir          = 'post_5_fields/'
field2dir          = 'pre_5_fields/'
out_dir            = 'local/'
TAGS               = ['tejon_100mgal','northridge_100mgal','sf_100mgal']
PLOT_EVIDS         = [60019,193054,231185]
"""

"""
center_evnum = 109382
with VCSimData() as sim_data:
	sim_data.open_file(sim_file)
	events			= VCEvents(sim_data)
	center_evyear	= events.get_event_year(center_evnum)
start_year	= round(center_evyear)-duration/2.0
end_year	= round(center_evyear)+duration/2.0

event_range={'type':'year','filter':(start_year,end_year)}
event_range=None

pre = 'local/web_sim_full_'
output_files = [pre+'magn_rup_area.png',pre+'avg_slip_rup_len.png',pre+'freq_mag.png',pre+'recurr_intervals.png']
MAG_FILTER = None

vcplots.magnitude_rupture_area(sim_file,output_files[0],event_range=event_range,magnitude_filter=MAG_FILTER)
vcplots.average_slip_surface_rupture_length(sim_file,output_files[1],event_range=event_range,magnitude_filter=MAG_FILTER)
vcplots.frequency_magnitude(sim_file,output_files[2],event_range=event_range,magnitude_filter=MAG_FILTER)
#vcplots.plot_recurrence_intervals(sim_file,output_file=output_files[3],event_range=event_range,magnitude_filter=MAG_FILTER)

"""




"""
for k in range(len(PLOT_EVIDS)):
    evnum = PLOT_EVIDS[k]
    TAG   = TAGS[k]
    vcplots.plot_event_field(sim_file, evnum, out_dir, field_type='gravity', padding=0.08, cutoff=CUTOFF,tag=TAG)
    #print '\n'+TAG
    #vcanalysis.event_sections(sim_file,evnum)
"""



"""
search_evnums = vcanalysis.detailed_sim_info(sim_file,show=SHOW,section_filter=LA,magnitude_filter=MAGS[-1],return_evnums=True)
for evnum in search_evnums:
    vcanalysis.event_sections(sim_file,evnum)
"""


#BUFFER = 3.0
#output_directory = 'pre_3_fields/'
#vcplots.compute_composite_fields(sim_file,output_directory,EVIDS_10,field_type='gravity',pre=True,buffer=BUFFER,section_filter=SOUTH_SAF_SECS,cutoff=CUTOFF)

#vcplots.plot_backslip(sim_file, 1.0, section_filter=SOUTH_SAF_SECS)

#vcplots.diff_composite_fields(sim_file, (EVIDS_10,EVIDS_10),field1dir,field2dir,
#    field_type='gravity', fringes=True, padding=0.08, cutoff=None,
#    pre=(PRE1,PRE2),buffer=(BUFFER,BUFFER),section_filter=SOUTH_SAF_SECS,
#    backslip_only=(BACK1,BACK2),eq_slip_only=(EQ1,EQ2),tag=TAG)

#evnums = [193054,231185,60019]

#lat_lon = {'Los Angeles':(34.045536,-118.259297),'San Francisco':(37.773984,-122.418202),'Sacramento':(38.577646,-121.489948),'San Luis Obispo':(35.286790,-120.660601),'Santa Clarita':(34.388459,-118.539607),'Simi Valley':(34.266523,-118.780306),'Fort Bragg':(39.442104,-123.793432),'San Jose':(37.339686,-121.895108),'Bakersfield':(35.373937,-119.018800),'Fresno':(36.750055,-119.767782)}

#tags = ['Northridge','San Francisco','Fort Tejon']
#sites = [['Santa Clarita','Simi Valley','Los Angeles'],['Fort Bragg','San Francisco','San Jose'],['Los Angeles','Bakersfield','San Luis Obispo']]
"""
for k in range(len(evnums)):
    evnum = evnums[k]
    tag   = tags[k]
    cities= sites[k]
    with VCSimData() as sim_data:
        sim_data.open_file(sim_file)
        geometry    = VCGeometry(sim_data)
        #events      = VCEvents(sim_data)
        
        min_lat = geometry.min_lat
        max_lat = geometry.max_lat
        min_lon = geometry.min_lon
        max_lon = geometry.max_lon
        base_lat = geometry.base_lat
        base_lon = geometry.base_lon
        
        #slip_rates  = geometry.get_slip_rates()
        
        #event_element_slips = {evid:events.get_event_element_slips(evid) for evid in event_data['event_number']}
        
        EF = vcutils.VCGravityField(min_lat, max_lat, min_lon, max_lon, base_lat, base_lon, padding=0.08)

        output_directory = 'local/'
        field_values_directory = '{}field_values/'.format(output_directory)    
        PRE = '{}{}_'.format(field_values_directory, evnum)

        field_values_loaded = EF.load_field_values(PRE)

        print '\n{} - {}:'.format(tag,evnum)
        for city in cities:
            lat,lon = lat_lon[city]
            print city+'\t{:>6.3f}'.format(EF.get_field_value(lat,lon))
            #print lat,lon
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



