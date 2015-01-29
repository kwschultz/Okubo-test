#!/usr/bin/env python

from subprocess import call

pyvq      = "../vq/examples/pyvq.py"
sim_tag   = "--event_file"
sim_file  = "events_two_fault_100k.h5"
file_type = "hdf5"
file_tag  = "--event_file_type"
plot_arg  = "--plot_freq_mag"

arg_list = [pyvq,sim_tag, sim_file, file_tag, file_type, plot_arg]

call(arg_list)






