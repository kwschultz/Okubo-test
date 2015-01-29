#!/bin/bash


python ../vq/examples/pyvq.py --event_file events_three_fault_1kyr_dyn0-5_BASSgen1.h5 --event_file_type 'hdf5' --plot_prob_vs_t_fixed_dt

#events_two_fault_50k_multiproc_noAftershocks.h5
#ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5
#events_two_fault_1k_multiproc_noAftershocks.h5_argument('--plot_freq_mag', required=False, action='store_true',
#events_three_fault_1kyr_dyn0-5_BASSgen1.h5

# Plot options
# --plot_freq_mag
# --plot_mag_rupt_area
# --plot_mag_mean_slip
# --plot_prob_vs_t
# --plot_prob_vs_t_fixed_dt

