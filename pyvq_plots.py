#!/usr/bin/env python

from subprocess import call

pyvq     = "../vq/examples/pyvq.py"
sim_file = "--event_file events_two_fault_100k.h5"
file_type= "--event_file_type hdf5"
plot_arg = "--plot_freq_mag "

call([pyvq, sim_file, file_type, plot_arg])






