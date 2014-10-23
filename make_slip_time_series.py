import sys

import numpy as np
import os
import time
from matplotlib import pyplot as plt

sys.path.insert(0,"/home/kasey/PyVC/")
# Change this to match your directory, or edit your python path
#    or something so Python knows about the PyVC module

from pyvc import vcplots
from pyvc import vcanalysis
from pyvc import vcutils
from pyvc import *

#=============================================================================
sim_file  = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'

# Grab only those sections of interest
BAJA  = {'filter':(16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 56, 57, 69, 70, 73, 83, 84, 92, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 123, 124, 125, 126, 149)}

# Grab only those events that lie within the specified interval of sim time
# I believe we have to start at t=0.0 every time
duration = 2000.0
EV_RANGE = {'type':'year', 'filter':(0.0,duration)}
# DT is the time sample spacing in decimal years
dt       = 1.0

with VCSimData() as sim_data:
    sim_data.open_file(sim_file)

    # Fault model data extraction is done by vcgeometry.py
    geometry = VCGeometry(sim_data)

    # Event data extraction is done by vcevents.py
    events	 = VCEvents(sim_data)

    # Get event information, filter by section if specified
    event_data = events.get_event_data(['event_magnitude', 'event_year', 'event_number'], section_filter=BAJA,event_range=EV_RANGE)

    # event_element_slips = dictionary indexed by event_id with entries being dictionaries of slips (in meters) indexed by block_id
    event_element_slips = {evid:events.get_event_element_slips(evid) for evid in event_data['event_number']}

    # slip_time_series    = dictionary indexed by block_id with entries being arrays of absolute slip at each time step
    slip_time_series = geometry.get_slip_time_series(event_data,event_element_slips,DT=dt,duration=duration,section_filter=BAJA)








