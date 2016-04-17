#!/bin/bash

# Ignore this PYTHONPATH
#PYTHONPATH=/Users/kasey/vq/build/quakelib/python/


## ========= Returning VQ to VC-type CA model ===============

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_singleFaultFlat_fault_dip90_3km_5kr_dyn0-1_stressDrops0-5_NoDynDrops_RUPTURE_DEV.txt --sweep_file ~/Desktop/RUNNING/sweeps_singleFaultFlat_fault_dip90_3km_5kr_dyn0-1_stressDrops0-5_NoDynDrops_RUPTURE_DEV.txt --model_file ~/VQModels/singleFaultFlat_dip90_fault_3000mElements_drops0-5.txt --fault_time_series --max_year 5000 --use_faults 0 --dt 1.0 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_singleFaultFlat_fault_dip90_3km_5kr_dyn0-1_stressDrops0-5_NoDynDrops_RUPTURE_DEV.txt --sweep_file ~/Desktop/RUNNING/sweeps_singleFaultFlat_fault_dip90_3km_5kr_dyn0-1_stressDrops0-5_NoDynDrops_RUPTURE_DEV.txt --model_file ~/VQModels/singleFaultFlat_dip90_fault_3000mElements_drops0-5.txt --diagnostics --max_year 5000


#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/VQModels/UCERF3/UCERF3_VQmeshed_from_EQSIM_ReIndexed_AseismicCut_0-11_April12_taper_renorm_drops0-5.txt --fault_length_distribution --no_titles

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_50kyr_dyn0-3_stressDrops0-5_dynDrops_MagFix.h5 --all_stat_plots --UCERF3 --no_titles --label "$\eta = 0.3, \ \Delta M = 0.5$"


##### PLOTS FROM ALIREZA TO DEBUG #####################
# Region
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --probability_table --t0 3.08 11 12.17 --magnitudes 5 6 6.5 --t 1 5 10
#-------------------------------------------
#                   1 yr 	5 yr 	10 yr 
#(N=21688)	M > 5	0.37	0.89	0.99
#(N=13825)	M > 6	0.25	0.66	0.89
#(N=5224)	M > 6.5	0.10	0.38	0.61
# THE WHOLE REGION::::
#                                1.0yr 	5.0yr 	10.0yr 	25.0yr 
#(N= 13825)	M > 6.0	  t0=18.0	0.20	0.71	0.91	0.99
#(N=  5224)	M > 6.5	  t0=18.0	0.09	0.39	0.61	0.92
#(N=   555)	M > 7.0	  t0=34.6	0.01	0.06	0.09	0.21

#
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --probability_table --t0 3.08 11 12.17 --magnitudes 5 6 6.5 --t 1 5 15
#                   1.0 yr 	5.0 yr 	15.0 yr 
#(N=21688)	M > 5.0	0.37	0.89	0.99
#(N=13825)	M > 6.0	0.25	0.66	0.97
#(N=5224)	M > 6.5	0.10	0.38	0.76
#-------------------------------------------

# Kun-Banan
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --use_faults 65 --probability_table --t0 11 11 --magnitudes 5 6 --t 1 5 10
#-------------------------------------------

# Golbaf-Sirch
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --probability_table --t0 18 18 34.6 --magnitudes 6 6.5 7 --t 1 5 10 25 --use_faults 54
#
#                                1.0yr 	5.0yr 	10.0yr 	25.0yr 
#(N=  1594)	M > 6.0	  t0=18.0	0.04	0.16	0.28	0.55
#(N=   551)	M > 6.5	  t0=18.0	0.01	0.04	0.09	0.18
#(N=    44)	M > 7.0	  t0=34.6	0.00	0.00	0.00	0.02

#-------------------------------------------

##### ########## ----------- ######## #####################


#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/VQModels/UCERF3/UCERF3_VQmeshed_from_EQSIM_Elsinore_Only_no_taper_ReFaulted_ReSectioned_ReElemented_drops0-5.h5 --traces


#python ../vq/pyvq/pyvq/pyvq.py --event_file events_single_strike_3km.txt --sweep_file sweeps_single_strike_3km.txt --model_file single_strike_3km.txt --fault_time_series --max_year 1000 --use_faults 0


##### COMPARING RE-FAULTED STRIKE-FIXED to NON RE-FAULTED STANDARD UCERF3 both with ASEISMIC CUT 011
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_Standard_AseismicCut_0-11_TaperRenorm_10kyr_dyn0-3_stressDrops0-5_DynDrops.h5  ~/Desktop/RUNNING/UCERF3_ReIndexed_AseismicCut_0-11_March12_TaperRenorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5  --label "Original UCERF3" "Re-Faulted and Re-Aligned UCERF3"  --all_stat_plots --UCERF3 --min_magnitude 5 --min_slip -10  --max_year 10000  --no_titles --min_magnitude 6 #--min_num_elements 10


#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/singleFaultFlat_fault_dip90_3km_114kyr_dyn0-3_stressDrops0-5_dynDrops.h5 --model_file ~/VQModels/singleFaultFlat_dip90_fault_3000mElements_drops0-5.txt --fault_time_series --use_faults 0 --dt 100 --label "Single flat fault" --max_year 100000

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/singleFaultFlat_fault_dip90_3km_100kr_dyn0-1_stressDrops0-5_dynDrops.h5 --model_file ~/VQModels/singleFaultFlat_dip90_fault_3000mElements_drops0-5.txt --event_id 310 --event_movie

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/singleFaultFlat_fault_dip90_3km_100kr_dyn0-1_stressDrops0-5_dynDrops.h5 --model_file ~/VQModels/singleFaultFlat_dip90_fault_3000mElements_drops0-5.txt --event_id 311 --event_movie


############ Begin   FAULT CORRELATIONS   ################################

## ------------ LA BASIN AND MOJAVE FAULTS ISOLATED -------------------
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5  --all_stat_plots --min_slip -10 --UCERF3  --min_magnitude 5 --label "LA Basin and Mojave Faults only"

# --------- Look at the effect of tapering on the stats for Mojave EQs in the LA Basin + Mojave sims
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5  --all_stat_plots --min_slip -10 --UCERF3  --min_magnitude 5 --label "no taper" "tapering" "renormalized tapering"

# ------- Make a time series plot and save the time series for Mojave faults for each taper type
## 10 million year sim to try and find equilibrium
##### First, taper
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_10Myr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_drops0-5.h5 --fault_time_series --use_faults 91 92 723 --dt 500 --label "Johnson Valley" "Kickapoo" "Homestead Valley" --max_year 10000000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_10Myr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_drops0-5.h5 --fault_time_series --use_faults 152 108 185 226 236 240 122 109 113 --dt 500 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre" --max_year 10000000 --full_time_range

##### Next, taper_renorm  
##!!!!!!!!!!!!!!!!
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_10Myr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_drops0-5.h5 --fault_time_series --use_faults 91 92 723 --dt 500 --label "Johnson Valley" "Kickapoo" "Homestead Valley" --max_year 10000000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_10Myr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_drops0-5.h5 --fault_time_series --use_faults 152 108 185 226 236 240 122 109 113 --dt 500 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre" --max_year 10000000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_drops0-5.h5 --fault_time_series --use_faults 91 92 723 --dt 10 --label "Johnson Valley" "Kickapoo" "Homestead Valley" --max_year 200000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_drops0-5.h5 --fault_time_series --use_faults 91 92 723 --dt 10 --label "Johnson Valley" "Kickapoo" "Homestead Valley" --max_year 200000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_drops0-5.h5 --fault_time_series --use_faults 91 92 723 --dt 10 --label "Johnson Valley" "Kickapoo" "Homestead Valley" --max_year 200000 --full_time_range


# ------- Make a time series plot and save the time series for LA Basin faults for each taper type
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_drops0-5.h5 --fault_time_series --use_faults 152 108 185 226 236 240 122 109 113 --dt 10 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre" --max_year 200000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_drops0-5.h5 --fault_time_series --use_faults 152 108 185 226 236 240 122 109 113 --dt 10 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre" --max_year 200000 --full_time_range

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.h5 --model_file ~/VQModels/UCERF3/UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_drops0-5.h5 --fault_time_series --use_faults 152 108 185 226 236 240 122 109 113 --dt 10 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre" --max_year 200000 --full_time_range


## ========= Make fault group averaged time series
#python ../vq/pyvq/pyvq/pyvq.py --fault_group_time_series --group2_files fault_91_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_92_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_723_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --group1_files fault_109_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_113_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_122_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_240_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_108_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_152_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_185_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_226_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_236_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_renorm_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --label  "LA Basin faults" "Mojave faults"

#python ../vq/pyvq/pyvq/pyvq.py --fault_group_time_series --group2_files fault_91_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_92_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_723_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --group1_files fault_109_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_113_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_122_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_240_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_108_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_152_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_185_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_226_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_236_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_taper_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --label "LA Basin faults"  "Mojave faults"


#python ../vq/pyvq/pyvq/pyvq.py --fault_group_time_series --group2_files fault_91_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_92_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_723_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --group1_files fault_109_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_113_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_122_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_240_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_108_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_152_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_185_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_226_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle fault_236_timeseries_standardized_yearMin0_yearMax200000_combined_dt10.0yrs_UCERF3_EQSim_ReIndexed_LA_Basin_and_Mojave_AseismicCut_0-11_none_200kyr_dyn0-3_stressDrops0-5_DynDrops.pickle --label  "LA Basin faults" "Mojave faults"



## ------------ FULL UCERF3 SIM -------------------

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_ReIndexed_AseismicCut0-11_TaperRenorm_100kyr_dyn0-5_stressDrops0-7_DynDrops.h5 --model_file ~/Desktop/RUNNING/UCERF3_VQmeshed_from_EQSIM_ReIndexed_AseismicCut_0-11_taper_renorm_drops0-7.h5 --fault_time_series --max_year 80000 --use_faults 91 92 723 --dt 1.0 --label "Johnson Valley" "Kickapoo" "Homestead Valley"

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_ReIndexed_AseismicCut0-11_TaperRenorm_100kyr_dyn0-5_stressDrops0-7_DynDrops.h5 --model_file ~/Desktop/RUNNING/UCERF3_VQmeshed_from_EQSIM_ReIndexed_AseismicCut_0-11_taper_renorm_drops0-7.h5 --fault_time_series --max_year 80000 --use_faults 152 108 185 226 236 240 122 109 113 --dt 1.0 --label "Raymond" "Hollywood" "Santa Monica Bay" "Santa Monica" "Whittier" "Puente Hills" "Newport-Inglewood" "Palos Verdes" "Sierra Madre"
############@###########################################################




#python ../vq/pyvq/pyvq/pyvq.py --event_file events_single_strike_3km.txt --sweep_file sweeps_single_strike_3km.txt --model_file single_strike_3km.txt --slip_time_series --elements 0 1 2 3 4 5 6 --dt .2 --max_year 1000

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_single_strike_3km.txt --sweep_file sweeps_single_strike_3km.txt  --model_file single_strike_3km.txt --num_sweeps --event_mean_slip --event_shear_stress --event_normal_stress

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_single_strike_3km.txt  --sweep_file sweeps_single_strike_3km.txt --model_file single_strike_3km.txt --all_stat_plots --block_area_hist --field_plot --field_type insar --event_id 88

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_3km_5kyr_dyn1-3_VQstressDrops0-4_GreenLimits_doNormal_newDynamicDropsFrictionCoeff.h5   --summary 30 --min_area 3000 --min_magnitude 7.4  --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km.txt #--min_magnitude 5

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_3km_6kyr_dyn1-5_GreensLimits_VQstressDrops0-3_dynStressDrop.h5 --diagnostics #--min_slip 0  # --event_shear_stres --zoom

#python ../vq/pyvq/pyvq/pyvq.py --block_aseismic_hist --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km.txt #~/VQModels/UCERF3/UCERF3_fault_3000.txt  

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_5kyr_dyn2-0_stressDrops0-4_GreenLimits_largerSAFdrops0-6.h5  --plot_recurrence --use_trigger_sections 5 --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km.txt

# ================================================================================================
# ================================================================================================
#  TO COMPARE:   

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-5_stressDrops0-5_dynDrops_MagFix.h5  ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-1_stressDrops0-5_dynDrops_MagFix.h5  --label "$\eta = 0.5$" "$\eta = 0.1$"  --all_stat_plots --UCERF3 --min_magnitude 5 --min_slip -10 # --max_year 19000 #--min_num_elements 10

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/singleFaultFlat_fault_3km_1000yr_dyn0-2_stressDrops0-5_dynDrops.h5  ~/Desktop/RUNNING/singleFaultFlat_fault_3km_1000yr_dyn0-2_stressDrops0-5_dynDrops_BASSgen1.h5 --model_file singleFaultFlat_fault_3000mElements_drops0-5.txt  --model_file_type 'text' --min_slip -10 --all_stat_plots --label "standard" "with BASS aftershocks" --pdf #--min_year 0 --max_year 50 --spacetime --use_faults 0  #

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn0-5_GreensLimits_VQstressDrops0-3_dynDrops.h5  ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn0-3_GreensLimits_VQstressDrops0-4_dynDrops.h5  ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn1-0_stressDrops0-4_GreenLimits_dynDrops.h5   --all_stat_plots --min_num_elements 10 --max_year 10000 --min_magnitude 5.5 --UCERF2

## With and without vertical tapering, and adding horizontal tapering
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_TAPER_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5  ~/Desktop/RUNNING/UCERF3_VQmeshed_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-8_stressDrops0-7_GreenLimits_dynDrops.h5 --all_stat_plots --min_slip -10 --min_num_elements 0 --UCERF3 #--min_magnitude 6 

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_REfaulted_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-8_stressDrops0-7_GreenLimits_dynDrops.h5  ~/Desktop/RUNNING/UCERF3_VQmeshed_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-8_stressDrops0-7_GreenLimits_dynDrops.h5  ~/Desktop/RUNNING/UCERF3_VQmeshed_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5   --all_stat_plots --min_slip .1 --min_magnitude 5.5 --min_num_elements 10 --UCERF3

### No tapering UCERF3, varying fit parameters
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-7_stressDrops0-4_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn1-0_stressDrops0-4_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-4_stressDrops0-4_GreenLimits_dynDrops.h5  ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-7_stressDrops0-3_GreenLimits_dynDrops.h5 --all_stat_plots --min_num_elements 10 --min_slip .1 --UCERF3

#### Compare a few before the magnitude fix
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-9_DynDrops_dynTriggerFix.h5 ~/Desktop/RUNNING/UCERF3_REfaulted_ASEISMIC_CUT_0-11_TaperRenorm_20kyr_dyn0-5_stressDrops0-8_dynDrops_dynTriggerFix.h5 ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-7_dynDrops_dynTriggerFix.h5  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-6_DynDrops_dynTriggerFix.h5 ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-5_dynDrops_dynTriggerFix.h5 --all_stat_plots --min_slip -10 --min_magnitude 6 --UCERF3 --max_year 10000 --label "$\Delta M = 0.9$" "$\Delta M = 0.8$" "$\Delta M = 0.7$" "$\Delta M = 0.6$" "$\Delta M = 0.5$" --no_titles

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn1-5_stressDrops0-7_dynDrops_MagFix.h5 ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-5_stressDrops0-7_dynDrops_MagFix.h5 --all_stat_plots --min_slip -10 --min_magnitude 6 --UCERF3 --label "$\eta = 1.5$" "$\eta = 0.5$" --max_year 11000

######  NEWEST  ########   ######  NEWEST  ########    TUNING
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-9_DynDrops_MagFix.h5  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-8_DynDrops_MagFix.h5 ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-5_stressDrops0-7_dynDrops_MagFix.h5  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_10kyr_dyn0-5_stressDrops0-6_DynDrops_MagFix.h5 ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-5_stressDrops0-5_dynDrops_MagFix.h5 --all_stat_plots --min_slip -10 --min_magnitude 6 --UCERF3 --label "$\Delta M = 0.9$" "$\Delta M = 0.8$" "$\Delta M = 0.7$" "$\Delta M = 0.6$" "$\Delta M = 0.5$" --no_titles

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn1-5_stressDrops0-7_dynDrops_MagFix.h5  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_MagFix.h5  ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_11kyr_dyn0-1_stressDrops0-7_dynDrops_MagFix.h5  --all_stat_plots --min_slip -10 --min_magnitude 6 --UCERF3 --label "$\eta \geq 1.5$" "$\eta = 0.5$" "$\eta = 0.1$" --no_titles --max_year 10000 # ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_11kyr_dyn5-0_stressDrops0-7_dynDrops_MagFix.h5 "$\eta = 5.0$"

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_MagFix.h5 --plot_prob_vs_t --plot_prob_vs_t_fixed_dt --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 6.5


#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_50kyr_dyn0-1_stressDrops0-5_dynDrops_MagFix.h5    --max_year 10000  --all_stat_plots --min_slip -10 --UCERF3  --min_magnitude 5.0 --label "$\eta = 0.1$"  # ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-5_stressDrops0-5_dynDrops_MagFix.h5 ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_50kyr_dyn0-3_stressDrops0-5_dynDrops_MagFix.h5    "$\eta = 0.5$" "$\eta = 0.3$"
 
#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_drops0-5.txt --event_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-1_stressDrops0-5_dynDrops_MagFix.h5 --min_year 4000 --max_year 6000 --spacetime --use_faults 103

##########################   SPACETIME PLOTS   ########################
#python ../vq/pyvq/pyvq/pyvq.py --model_file  ~/VQModels/UCERF3/UCERF3_VQmeshed_from_EQSIM_current_taper_renorm_drops0-7.txt --event_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-1_stressDrops0-5_dynDrops_MagFix.h5  --use_faults 299   --min_year 8000 --max_year 8500 --spacetime --event_kml --event_id 5372 #--summary 30

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --use_faults 153 --min_year 21000 --max_year 23000 --spacetime --min_magnitude 4.8 --max_magnitude 7.2   --eps #--event_kml --event_id 10154

# --use_faults 1 --event_id 9585 --min_year 20000 --max_year 23000

#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_drops0-5.txt --event_file ~/Desktop/RUNNING/UCERF3_ReFaulted_AseismicCut0-11_taper_renorm_10kyr_dyn0-1_stressDrops0-5_dynDrops_MagFix.h5 --event_id 140 --event_kml


######  NEWEST  ########  ######  NEWEST  ########   TUNING

### Improvements to UCERF3 sims
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_VQmeshed_3km_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_TAPER_10kyr_dyn0-8_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_VQmeshed_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-8_stressDrops0-5_GreenLimits_NoDynDrops.h5  ~/Desktop/RUNNING/UCERF3_REfaulted_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-6_stressDrops0-5_GreenLimits_dynDrops.h5 ~/Desktop/RUNNING/UCERF3_REfaulted_VQmeshed_ASEISMIC_CUT_0-13_TaperRenorm_10kyr_dyn0-5_stressDrops0-4_dynDrops.h5 --label "standard UCERF3" "UCERF3 + vertical tapering" "UCERF3 + horiz/vert taper renorm + aseismic cut 0.13" "+ h/v taper renorm + aseismic cut 0.13 + combined faults + dyn=0.6 + s.d. 0.5" "+ h/v taper renorm + aseismic cut 0.13 + combined faults + dyn=0.5 + s.d. 0.4" --all_stat_plots --min_num_elements 10 --min_slip .1 --UCERF3

##  histograms and distribution
python ../vq/pyvq/pyvq/pyvq.py --model_file ~/VQModels/UCERF3/UCERF3_VQmeshed_from_EQSIM_ReIndexed_AseismicCut_0-11_April12_taper_renorm_drops0-5.txt --block_stress_drop_hist --reference 1e6

##------------------------------------------------------------------------
### Probability table
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_rightHanded.h5 --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 5

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_rightHanded.h5 --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 6

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_rightHanded.h5 --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 7
########
#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_AseismicCut0-11_TaperRenorm_50kyr_dyn0-5_stressDrops0-7_DynDrops_MagFix.h5 --probability_table --t0 1.0 1.4 5.8 --min_slip -10
##------------------------------------------------------------------------

#python ../vq/pyvq/pyvq/pyvq.py --event_file  ~/Desktop/RUNNING/UCERF3_REfaulted_ASEISMIC_CUT_0-11_TaperRenorm_10kyr_dyn0-3_stressDrops0-6_dynDrops.h5 --all_stat_plots --min_slip -10 --UCERF3    --min_magnitude 6 --max_year 10000 --label  "s.d. factor = 0.6, dyn trigger 0.3" --dpi 100

# ================================================================================================
# ================================================================================================


#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_3km_9kyr_dyn1-0_GreensLimits_VQstressDrops0-4_dynDrops_coeffFriction0-6.h5 ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn1-0_stressDrops0-4_GreenLimits_NOdynDrops_coeffFriction0-6.h5 --all_stat_plots --leonard --min_num_elements 10 --max_year 9000


#python ../vq/PyVQ/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_single_small_fault_3km_200yr_dyn0-381_VQstressDrops0-4_dynDrops.h5 --event_id 0 --model_file ~/Desktop/RUNNING/single_small_fault_3000m_none.txt --event_movie

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_single_small_fault_1km_10kyr_dyn1-0_VQstressDrops0-4.h5 --all_stat_plots --min_slip -10

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_100yr_dyn1-0_stressDrops0-4_GreenLimits.h5 --stress_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km_stress.txt --stress_index_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km_stress_index.txt --combine_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_100yr_dyn1-0_stressDrops0-4_GreenLimits_stressIN.h5 --event_mean_slip

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_subset_NorCal_3km_400yr_dyn2-0_stressDrops0-4_GreenLimits.h5 events_ALLCAL2_VQmeshed_subset_NorCal_3km_400yr_dyn2-0_stressDrops0-4_GreenLimits_stressIN.h5  --diagnostics

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_10kyr_dyn1-3_VQstressDrops0-3_GreenLimits_AllowNegSlip_RemoveZeroSlipRates.h5   --event_shear_stress --zoom

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_3km_25kyr_dyn1-3_GreensLimits_VQstressDrops0-3_AllowNegSlips.h5  --event_mean_slip --num_sweeps

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.txt --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_dyn1-3_newStressDrops_GreenLimits_stressDropFactor0-3.h5 --slip_time_series --max_year 2000 --elements 0 1 2 3 1512 1513 1514 1515 1516 1517 1518 1519 1520 1521 1522 1523 1524 1525 1526 1527 1528 1529 1530 1531 1532 1533 1534 1535 1536 1537 1538 1539 1540 1541 1542 1543 1544 1545 1546 1547 1548 1549 1622 1623 1624 1625 1626 1627 1628 1629 1630 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 2082 2083 2084 2085 2114 2115 2116 2117 2118 2494 2495 2496 2497 2498 2529 2530 2531 2532 2785 2786 2787 2788 2789 2790 2791 2792 3025 3026 3027 3028 3029 3030 3031 3032 3109 3110 3111 3112 3113 3114 3115 3116 3217 3218 3219 3220 3221 3222 3223 3224 3313 3314 3315 3316 3407 3408 3409 3410 3571 3572 3573 3574 3596 3597 3598 3599 3600 3711 3712 3713 3714 3715 3786 3787 3788 3789 3790 3791 3888 3889 3890 3891 3892 3893 3984 3985 3986 3987 4356 4357 4358 4359 4390 4391 4392 4393 4562 4563 4564 4565 4566 4567 4568 4569 4570 4726 4727 4728 4729 4730 4731 4732 4733 4734 4735 4796 4797 4798 4799 4800 4801 4802 4803 4804 4805 4866 4867 4868 4869 4870 4911 4912 4913 4914 4915 4916 4917 5044 5045 5046 5047 5048 5049 5050 5051 5052 5053 5054 5055 5116 5117 5118 5119 5120 5121 5122 5123 5124 5125 5126 5127 5128 5129 5328 5329 5330 5331 5332 5333 5334 5335 5336 5487 5488 5489 5490 5571 5572 5573 5574 5575 5576 5577 5578 5643 5644 5645 5646 5647 5648 5649 5650 5967 5968 5969 5970 5971 5972 5973 5974 6063 6064 6065 6066 6099 6100 6101 6102 6323 6324 6325 6326 6351 6352 6353 6354 6419 6420 6421 6422 6423 6424 6425 6426 6427 6508 6509 6510 6511 6512 6513 6514 6515 6516 6601 6602 6603 6604 6605 6606 6607 6608 6737 6738 6739 6740 6741 6742 6743 6744 6897 6898 6899 6900 6901 6902 6903 6904 7041 7042 7043 7044 7045 7046 7047 7048 7049 7150 7151 7152 7153 7154 7227 7228 7229 7230 7319 7320 7321 7322 7474 7475 7476 7477 7554 7555 7556 7557 7669 7670 7671 7672 7673 7764 7765 7766 7767 7768 7769 7770 7771 7772 7817 7818 7819 7820 8007 8008 8009 8010 8055 8056 8057 8058 8059 8060 8061 8062 8131 8132 8133 8134 8135 8136 8137 8138 8195 8196 8197 8198 8199 8200 8201 8202 8243 8244 8245 8246 8247 8248 8249 8250 8319 8320 8321 8322 8323 8324 8325 8326 8403 8404 8405 8406 8407 8408 8409 8410 8531 8532 8533 8534 8535 8536 8537 8538 8719 8720 8721 8722 8723 8724 8725 8726 8843 8844 8845 8846 8847 8848 8849 8850 8951 8952 8953 8954 8999 9000 9001 9002 9103 9104 9105 9106 9107 9108 9109 9110 9167 9168 9169 9170 9171 9172 9173 9174 9175 9176 9261 9262 9263 9264 9265 9266 9390 9391 9392 9393 9394 9455 9456 9457 9458 9459 9460 9461 9462 9463 9544 9545 9546 9547 9573 9574 9575 9576 9577 9633 9634 9635 9636 9637 9663 9664 9665 9666 9811 9812 9813 9814 9815 9816 9817 9818 9867 9868 9869 9870 10003 10004 10005 10006 10007 10068 10069 10070 10071 10072 10113 10114 10115 10116 10249 10250 10251 10252 10253 10254 10255 10256 10349 10350 10351 10352 10353 10354 10355 10539 10540 10541 10542 10543 10544 10545 10546 10672 10673 10674 10675 10676 10698 10699 10700 10701 10782 10783 10784 10785 10853 10854 10855 10856 10913 10914 10915 10916 10917 10918 10919 10959 10960 10961 10962 10963 10964 10965 10966 11247 11248 11249 11250 11251 11302 11303 11304 11305 11306 11377 11378 11379 11380 11381 11382 11383 11384 11385 11386 11457 11458 11459 11460 11461 11487 11488 11489 11490 11491 11492 11493 11613 11614 11615 11616 11617 11618 11619 11620 11621 11622 11623 11624 11625 11698 11699 11700 11701 11702 11703 11785 11786 11787 11788 11857 11858 11859 11860 11960 11961 11962 11963 12072 12073 12074 12075 12076 12077 12078 12079 12200 12201 12202 12203 12248 12249 12250 12251 12348 12349 12350 12351 12352 12353 12354 12355 12432 12433 12434 12435 12436 12437 12438 12439 12440 12441 12532 12533 12534 12535 12536 12537 12574 12575 12576 12577 12578 12579 12664 12665 12666 12667 12668 12669 12670 12671 12672 12673 12674 12675 12676 12677 12678 12796 12797 12798 12799 12800 12801 12802 12803 12804 12805 12806 12807 12808 12809 12810 12811 12812 13037 13038 13039 13040 13041 13042 13043 13044 13045 13046 13047 13048 13049 13050 13051 13052 13269 13270 13271 13272 13273 13274 13275 13276 13357 13358 13359 13360 13361 13362 13363 13364 13469 13470 13471 13472 13473 13474 13475 13476 13477 13478 13479 13480 13481 13482 13483 13484 13573 13574 13575 13576 13577 13578 13579 13580 13617 13618 13619 13656 13657 13658 13680 13681 13682 13683 13684 13760 13761 13762 13763 13764 13870 13871 13872 13909 13910 13911 13912 13913 13914 13948 13949 13950 13951 13952 13953 13987 13988 13989 14234 14235 14236 14237 14306 14307 14308 14309

#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km.txt --event_file events_ALLCAL2_VQmeshed_3km_5kyr_dyn1-2_GreensLimits_VQstressDrops0-5_dynStressDrop_doNormal.h5 --event_id 14004 --event_kml

#python ../vq/pyvq/pyvq/pyvq.py --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_3km.txt --event_file events_ALLCAL2_VQmeshed_3km_6kyr_dyn1-5_GreensLimits_VQstressDrops0-3_dynStressDrop.h5 --event_id 1 --event_movie

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Desktop/RUNNING/events_ALLCAL2_VQmeshed_3km_5kyr_simplerRupture_dyn0-5.h5 --model_file ~/Desktop/RUNNING/ALLCAL2_VQmeshed_subset_NorCal_3km.txt --wc94 --plot_mag_rupt_area

#-----------
#python ../vq/pyvq/pyvq/pyvq.py --event_file ../Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --event_id 2497 --lld_file ../TsunamiSquares/Channel_Islands.txt --field_eval

##python ../vq/pyvq/pyvq/pyvq.py --event_file ../Desktop/RUNNING/events_greensTrimmed_ALLCAL2_VQmeshed_3km_EQSim_StressDrops_4kyr_24June2015.h5 --event_id 1157 --field_plot --field_type displacement --colorbar_max 0.3 --levels  -.3 -.2 -.1 -.05 .05 .1 .2 .3  --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5

#-----------

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_ALLCAL2_VQmeshed_3km_5kyr_dyn1-2_GreensLimits_VQstressDrops0-5_dynStressDrop_doNormal.h5 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --summary 20 --min_area 1000 --max_area 2000 --max_magnitude 6.5 --min_magnitude 6.0 --max_slip 0.1

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_allcal_3km_noShocks_greensTrim_8June2015.h5   --max_year 4200 --diagnostics

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_May29_allcal5km_no_taper_NoShocks_20kyr_0-5dyn.h5 --plot_freq_mag 1 --use_sections 25 --model_file ../Desktop/RUNNING/UCERF2/ALLCAL2_VQmeshed_3km.h5 --max_year 2000

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_May29_allcal5km_no_taper_gen1shocks_10kyr_0-5dyn.h5   --all_stat_plots --wc94

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/single_vert_strikeslip_LeftLateral_fault_10000.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/single_vert_strikeslip_RightLateral_fault_10000.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_10x10km_fault_3333mElements.txt --field_plot --field_type "dilat_gravity" --uniform_slip 5 --colorbar_max 30 --levels -30 -20 -10 0 10 20 30 --small_model

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/vert_strikeslip_LeftLateral_strike270_fault_10km.txt --field_plot --field_type "gravity" --uniform_slip 5 --colorbar_max 50 --levels -50 -40 -30 -20 -10 0 10 20 30 40 50 --small_model

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_all_cal_fault_5km_20kyr_noShocks.h5   --field_plot --field_type "gravity" --colorbar_max 20 --levels -20 -10 -5 -2.5 -1 0 1 2.5 5 10 20 --event_id 440
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

##python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "geoid" --colorbar_max .01 --event_id 128 --levels -.01 -.005 -.0025 -.00125 0 .00125 .0025 .005 .01 

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --field_plot --field_type "insar" --event_id 128

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --all_stat_plots --wc94 --min_magnitude 4

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_norcal_fault_5km_5kyr_dyn0-5_BASSgen0.h5   --all_stat_plots --wc94

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --traces

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_norcal_fault_5km_5kyr_dyn0-5_BASSgen0.h5   --field_plot --field_type "gravity" --event_id 1414 --colorbar_max 20

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --event_file events_allcal_5km_250kyr.h5   --plot_cond_prob_vs_t --plot_waiting_times --min_magnitude 7.5 --use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#--use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_3000.h5 --traces --use_sections 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140

#--------------------------------------------- IRAN
#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --use_trigger_sections 1 --min_magnitude 6.5 --plot_waiting_times # --fit_weibull  --plot_prob_vs_t  --plot_cond_prob_vs_t --plot_recurrence   

#python ../vq/pyvq/pyvq/pyvq.py --event_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/event_East.h5 --model_file ~/Dropbox/UCD/RESEARCH/Iranian_Collab/Simulations/Iran_3000.txt --traces   #--probability_table --t0 0.0 5.0 5.1  #--plot_prob_vs_t  --plot_cond_prob_vs_t --plot_waiting_times  --fit_weibull --dpi 150  # --plot_recurrence  

#---------------------------------------------


#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_10x10km_fault_3333mElements.txt --field_plot --field_type "gravity" --uniform_slip 5 --colorbar_max 500 --levels -500 -400 -300 -200 -100 0 100 200 300 400 500 --small_model

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/allcal_fault_5000.h5 --traces

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/thrust_dip45_switch_500x300km_fault_50000mElements.txt --field_plot --field_type "geoid" --uniform_slip 10 --colorbar_max .05 --levels -.05 -.04 -.03 -.02 -.01 0 .01 .02 .03 .04 .05 --small_model

#python ../vq/pyvq/pyvq/pyvq.py --model_file ../VQModels/vert_strikeslip_LeftLateral_500x300km_fault_100kmElements.txt --field_plot --field_type "geoid" --uniform_slip 10 --colorbar_max .01 --levels -.01 -.0075 -.005 -.0025 0 .0025 .005 .0075 .01 --small_model

#python ../vq/pyvq/pyvq/pyvq.py --greens --field_type "gravity" --plot_name "strikeslip_dip90_LL" --uniform_slip 5 --colorbar_max 50 --levels -50 -40 -30 -20 -10 0 10 20 30 40 50 --rake 0 --dip 90 --DTTF 1000 --save_greens

#python ../vq/pyvq/pyvq/pyvq.py --greens --field_type dilat_gravity --plot_name strikeslip_dip90_LL --uniform_slip 5 --colorbar_max 15 --levels -15 -10 -5 0 5 10 15 --rake 0 --dip 90 --DTTF 1000

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_eqsim_ucerf2_no-creep_no_taper_noAftershocks_8kyr_0-5dyn_3km.h5   --plot_freq_mag 4

#python ../vq/pyvq/pyvq/pyvq.py --event_file events_small_ca_6fault_50kyr_dyn0-5_BASSgen0.h5   --plot_freq_mag 4


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

# Zero slip rate elements in AllCal 3km model
#0 1 2 3 1512 1513 1514 1515 1516 1517 1518 1519 1520 1521 1522 1523 1524 1525 1526 1527 1528 1529 1530 1531 1532 1533 1534 1535 1536 1537 1538 1539 1540 1541 1542 1543 1544 1545 1546 1547 1548 1549 1622 1623 1624 1625 1626 1627 1628 1629 1630 1945 1946 1947 1948 1949 1950 1951 1952 1953 1954 1955 2082 2083 2084 2085 2114 2115 2116 2117 2118 2494 2495 2496 2497 2498 2529 2530 2531 2532 2785 2786 2787 2788 2789 2790 2791 2792 3025 3026 3027 3028 3029 3030 3031 3032 3109 3110 3111 3112 3113 3114 3115 3116 3217 3218 3219 3220 3221 3222 3223 3224 3313 3314 3315 3316 3407 3408 3409 3410 3571 3572 3573 3574 3596 3597 3598 3599 3600 3711 3712 3713 3714 3715 3786 3787 3788 3789 3790 3791 3888 3889 3890 3891 3892 3893 3984 3985 3986 3987 4356 4357 4358 4359 4390 4391 4392 4393 4562 4563 4564 4565 4566 4567 4568 4569 4570 4726 4727 4728 4729 4730 4731 4732 4733 4734 4735 4796 4797 4798 4799 4800 4801 4802 4803 4804 4805 4866 4867 4868 4869 4870 4911 4912 4913 4914 4915 4916 4917 5044 5045 5046 5047 5048 5049 5050 5051 5052 5053 5054 5055 5116 5117 5118 5119 5120 5121 5122 5123 5124 5125 5126 5127 5128 5129 5328 5329 5330 5331 5332 5333 5334 5335 5336 5487 5488 5489 5490 5571 5572 5573 5574 5575 5576 5577 5578 5643 5644 5645 5646 5647 5648 5649 5650 5967 5968 5969 5970 5971 5972 5973 5974 6063 6064 6065 6066 6099 6100 6101 6102 6323 6324 6325 6326 6351 6352 6353 6354 6419 6420 6421 6422 6423 6424 6425 6426 6427 6508 6509 6510 6511 6512 6513 6514 6515 6516 6601 6602 6603 6604 6605 6606 6607 6608 6737 6738 6739 6740 6741 6742 6743 6744 6897 6898 6899 6900 6901 6902 6903 6904 7041 7042 7043 7044 7045 7046 7047 7048 7049 7150 7151 7152 7153 7154 7227 7228 7229 7230 7319 7320 7321 7322 7474 7475 7476 7477 7554 7555 7556 7557 7669 7670 7671 7672 7673 7764 7765 7766 7767 7768 7769 7770 7771 7772 7817 7818 7819 7820 8007 8008 8009 8010 8055 8056 8057 8058 8059 8060 8061 8062 8131 8132 8133 8134 8135 8136 8137 8138 8195 8196 8197 8198 8199 8200 8201 8202 8243 8244 8245 8246 8247 8248 8249 8250 8319 8320 8321 8322 8323 8324 8325 8326 8403 8404 8405 8406 8407 8408 8409 8410 8531 8532 8533 8534 8535 8536 8537 8538 8719 8720 8721 8722 8723 8724 8725 8726 8843 8844 8845 8846 8847 8848 8849 8850 8951 8952 8953 8954 8999 9000 9001 9002 9103 9104 9105 9106 9107 9108 9109 9110 9167 9168 9169 9170 9171 9172 9173 9174 9175 9176 9261 9262 9263 9264 9265 9266 9390 9391 9392 9393 9394 9455 9456 9457 9458 9459 9460 9461 9462 9463 9544 9545 9546 9547 9573 9574 9575 9576 9577 9633 9634 9635 9636 9637 9663 9664 9665 9666 9811 9812 9813 9814 9815 9816 9817 9818 9867 9868 9869 9870 10003 10004 10005 10006 10007 10068 10069 10070 10071 10072 10113 10114 10115 10116 10249 10250 10251 10252 10253 10254 10255 10256 10349 10350 10351 10352 10353 10354 10355 10539 10540 10541 10542 10543 10544 10545 10546 10672 10673 10674 10675 10676 10698 10699 10700 10701 10782 10783 10784 10785 10853 10854 10855 10856 10913 10914 10915 10916 10917 10918 10919 10959 10960 10961 10962 10963 10964 10965 10966 11247 11248 11249 11250 11251 11302 11303 11304 11305 11306 11377 11378 11379 11380 11381 11382 11383 11384 11385 11386 11457 11458 11459 11460 11461 11487 11488 11489 11490 11491 11492 11493 11613 11614 11615 11616 11617 11618 11619 11620 11621 11622 11623 11624 11625 11698 11699 11700 11701 11702 11703 11785 11786 11787 11788 11857 11858 11859 11860 11960 11961 11962 11963 12072 12073 12074 12075 12076 12077 12078 12079 12200 12201 12202 12203 12248 12249 12250 12251 12348 12349 12350 12351 12352 12353 12354 12355 12432 12433 12434 12435 12436 12437 12438 12439 12440 12441 12532 12533 12534 12535 12536 12537 12574 12575 12576 12577 12578 12579 12664 12665 12666 12667 12668 12669 12670 12671 12672 12673 12674 12675 12676 12677 12678 12796 12797 12798 12799 12800 12801 12802 12803 12804 12805 12806 12807 12808 12809 12810 12811 12812 13037 13038 13039 13040 13041 13042 13043 13044 13045 13046 13047 13048 13049 13050 13051 13052 13269 13270 13271 13272 13273 13274 13275 13276 13357 13358 13359 13360 13361 13362 13363 13364 13469 13470 13471 13472 13473 13474 13475 13476 13477 13478 13479 13480 13481 13482 13483 13484 13573 13574 13575 13576 13577 13578 13579 13580 13617 13618 13619 13656 13657 13658 13680 13681 13682 13683 13684 13760 13761 13762 13763 13764 13870 13871 13872 13909 13910 13911 13912 13913 13914 13948 13949 13950 13951 13952 13953 13987 13988 13989 14234 14235 14236 14237 14306 14307 14308 14309