#!/bin/bash

# Ignore this PYTHONPATH
#PYTHONPATH=/Users/kasey/vq/build/quakelib/python/


#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5   --diagnostics

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5   --event_shear_stress

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_stressTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_6kyr_22June2015.h5   --diagnostics

#-----------
#python ../vq/pyvq/pyvq/pyvq.py --event_file ../Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --event_id 2497 --lld_file ../TsunamiSquares/Channel_Islands.txt --field_eval

#python ../vq/pyvq/pyvq/pyvq.py --event_file ../Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5 --event_id 1157 --field_plot --field_type displacement --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5

#-----------

#python ../vq/pyvq/pyvq/pyvq.py --event_file ../Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --summary 100 --use_trigger_sections 144

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_allcal_3km_noShocks_greensTrim_8June2015.h5   --max_year 4200 --diagnostics

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_May29_allcal5km_no_taper_NoShocks_20kyr_0-5dyn.h5 --plot_freq_mag 1 --use_sections 25 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --max_year 2000

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_May29_allcal5km_no_taper_gen1shocks_10kyr_0-5dyn.h5   --all_stat_plots --wc94

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/single_vert_strikeslip_LeftLateral_fault_10000.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/single_vert_strikeslip_RightLateral_fault_10000.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_10x10km_fault_3333mElements.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 30 --levels -30 -20 -10 0 10 20 30 --small_model

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/vert_strikeslip_LeftLateral_strike270_fault_10km.txt --field_plot --field_type "gravity" --uniform_slip 5 --colorbar_max 50 --levels -50 -40 -30 -20 -10 0 10 20 30 40 50 --small_model

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_all_cal_fault_5km_20kyr_noShocks.h5   --field_plot --field_type "gravity" --colorbar_max 20 --levels -20 -10 -5 -2.5 -1 0 1 2.5 5 10 20 --event_id 440
#---------------------------------------------

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_allcal_5km_250kyr.h5   --summary 10

#events_allcal_5km_250kyr.h5
#=======================================================
#evid	year		mag	area[km^2]	slip[m]
#-------------------------------------------------------
#141045	49096.9		8.052	6180.0393	7.2314
#168015	57812.6		7.643	6478.0736	1.6837
#3459	1893.3		7.416	5699.3955	0.8732
#2262	1327.0		7.416	5571.9664	0.8929
#7648	3617.9		7.408	6583.0380	0.7342
#924	631.3		7.405	5002.1039	0.9583
#2699	1527.4		7.400	5452.9425	0.8646
#1484	921.8		7.392	4975.6842	0.9206
#46307	17451.3		7.387	3134.8454	1.4352
#3275	1809.3		7.376	4475.1209	0.9679
#-------------------------------------------------------


#---------------------------------------------
#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "gravity" --colorbar_max 20 --event_id 141045 --levels -20 -10 -5 -2.5 -1 0 1 2.5 5 10 20

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "dilat_gravity" --colorbar_max 20 --event_id 141045 --levels -20 -10 -5 -2.5 -1 0 1 2.5 5 10 20

##python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "geoid" --colorbar_max .01 --event_id 128 --levels -.01 -.005 -.0025 -.00125 0 .00125 .0025 .005 .01 

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "insar" --event_id 128

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --all_stat_plots --wc94 --min_magnitude 4

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_norcal_fault_5km_5kyr_dyn0-5_BASSgen0.h5   --all_stat_plots --wc94

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --traces

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_norcal_fault_5km_5kyr_dyn0-5_BASSgen0.h5   --field_plot --field_type "gravity" --event_id 1414 --colorbar_max 20

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 7.5 --use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#--use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_3000.h5 --traces --use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#---------------------------------------------


#python ../vq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_10x10km_fault_3333mElements.txt --field_plot --field_type "gravity" --uniform_slip 5 --colorbar_max 500 --levels -500 -400 -300 -200 -100 0 100 200 300 400 500 --small_model

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --traces

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_500x300km_fault_50000mElements.txt --field_plot --field_type "geoid" --uniform_slip 10 --colorbar_max .05 --levels -.05 -.04 -.03 -.02 -.01 0 .01 .02 .03 .04 .05 --small_model

#python ../vq/pyvq/pyvq.py --model_file ../VQModels/vert_strikeslip_LeftLateral_500x300km_fault_100kmElements.txt --field_plot --field_type "geoid" --uniform_slip 10 --colorbar_max .01 --levels -.01 -.0075 -.005 -.0025 0 .0025 .005 .0075 .01 --small_model

#python ../vq/pyvq/pyvq.py --greens --field_type "gravity" --plot_name "strikeslip_dip90_LL" --uniform_slip 5 --colorbar_max 50 --levels -50 -40 -30 -20 -10 0 10 20 30 40 50 --rake 0 --dip 90 --DTTF 1000

#python ../vq/pyvq/pyvq.py --greens --field_type dilat_gravity --plot_name strikeslip_dip90_LL --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 --rake 0 --dip 90 --DTTF 1000

#python ../vq/pyvq/pyvq.py --event_file events_eqsim_ucerf2_no-creep_no_taper_noAftershocks_8kyr_0-5dyn_3km.h5   --plot_freq_mag 4

#python ../vq/pyvq/pyvq.py --event_file events_small_ca_6fault_50kyr_dyn0-5_BASSgen0.h5   --plot_freq_mag 4


#thrust_dip30_fault_10km.txt
#vert_strikeslip_fault_10km.txt
#normal_dip60_fault_10km.txt
#events_small_ca_6fault_50kyr_dyn0-5_BASSgen0.h5
#events_two_fault_50k_multiproc_noAftershocks.h5
#ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5
#events_two_fault_1k_multiproc_noAftershocks.h5
#events_three_fault_1kyr_dyn0-5_BASSgen1.h5

# ----------------- Example usage --------------------------

# Frequency magnitude plot for all events in the sim file
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_freq_mag 1

# Frequency magnitude plot including a b=1 line, only using EQs that produce slip on sections 1,2,3 (must also specify a model file)
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_freq_mag 1 --model_file path/to/model.txt --use_sections 1 2 3

# Magnitude vs Rupture Area plot for all events in the sim file
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_mag_rupt_area

# Plot prob vs time of 3.0 < Mag < 6.0 earthquakes for all events in the sim file
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_prob_vs_t --min_magnitude 3.0 --max_magnitude 6.0

# Plot conditional prob vs time of Mag > 5.5 earthquakes, and plotting a weibull curve with beta=1.2 and tau=19
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_cond_prob_vs_t --min_magnitude 5.5 --beta 1.2 --tau 19

# Plot waiting times vs time for Mag > 6.0 earthquakes
# python path/to/vq/examples/pyvq.py --event_file path/to/sim_file.h5   --plot_waiting_times --min_magnitude 6.0


# ----- Currently working plot options (with examples) -------------------------------------------
# --plot_freq_mag 1 (normal) or 2 (add a b=1 line) or 3 (add UCERF2 observed rates with errorbars) or 4 (add b=1 and UCERF2 rates)
# --plot_mag_rupt_area
# --plot_mag_mean_slip
# --plot_prob_vs_t
# --plot_prob_vs_t_fixed_dt
# --plot_cond_prob_vs_t
# --plot_waiting_times
# --min_magnitude 5.0
# --max_magnitude 7.9
# --use_sections 1 2 3 4
# --field_plot
# --field_type
# --field_savefile
# --colorbar_max 20

