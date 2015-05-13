#!/usr/bin/env python

from os import system

TYPE = "fundamental_greens"
# greens, fundamental_greens, single, Okubo, num_elements
PYVQ = "../vq/pyvq/pyvq/pyvq.py"


#  ---- Plotting Okubo Green's functions for single faults ----------------
if TYPE == "greens":
    plot       = "--greens"
    field_type = ["geoid","geoid","gravity","dilat_gravity","gravity","dilat_gravity"]
    plot_name  = ["strikeslip_dip90_LL_500x300km","thrust_dip45_500x300km",
                  "strikeslip_dip90_LL_10x10km","strikeslip_dip90_LL_10x10km",
                  "thrust_dip45_10x10km","thrust_dip45_10x10km"]
    slip       = [10,10,5,5,5,5]
    rake       = [0,90,0,0,90,90]
    dip        = [90,45,90,90,45,45]
    dttf       = [500,500,1000,1000,1000,1000]
    cbar_max   = [0.01,0.05,50,15,500,30]
    levels     = ["-.01 -.0075 -.005 -.0025 0 .0025 .005 .0075 .01",
                  "-.05 -.04 -.03 -.02 -.01 0 .01 .02 .03 .04 .05",
                  "-50 -40 -30 -20 -10 0 10 20 30 40 50",
                  "-15 -10 -5 0 5 10 15", 
                  "-500 -400 -300 -200 -100 0 100 200 300 400 500",
                  "-30 -20 -10 0 10 20 30"]
    Xmin       = [-500000, -500000, -5000, -5000, -5000, -5000]
    Xmax       = [1000000, 1000000, 15000, 15000, 15000, 15000]
    Ymin       = [-750000, -750000, -10000, -10000, -5000, -5000]
    Ymax       = [750000, 750000, 10000, 10000, 15000, 15000]
    L          = [500000, 500000, 10000, 10000, 10000, 10000]
    W          = [300000, 300000, 10000, 10000, 10000, 10000]

    for i in range(len(L)):
        return_value = system("python {} {} --field_type {} --plot_name {} --uniform_slip {} --colorbar_max {} --levels {} --rake {} --dip {} --DTTF {} --L {} --W {} --Xmin {} --Xmax {} --Ymin {} --Ymax {}".format(PYVQ, plot, field_type[i], plot_name[i], slip[i], cbar_max[i], levels[i], rake[i], dip[i], dttf[i], L[i], W[i], Xmin[i], Xmax[i], Ymin[i], Ymax[i]))
        
        
if TYPE == "fundamental_greens":
    plot       = "--greens"
    plot_name  = ["QUAL_strikeslip_dip90_LL_10x10km","QUAL_thrust_dip30_10x10km","QUAL_normal_dip60_10x10km"]
    field_type = "dilat_gravity"
    slip       = [5,5,5]
    rake       = [0,90,-90]
    dip        = [90,30,60]
    dttf       = 1000
    if field_type == "gravity":
        cbar_max   = [50,500,500]
        levels     = ["-50 -40 -30 -20 -10 0 10 20 30 40 50",
                      "-500 -400 -300 -200 -100 0 100 200 300 400 500",
                      "-500 -400 -300 -200 -100 0 100 200 300 400 500"]
    elif field_type == "displacement":
        cbar_max   = [.2,2,2]
        levels     = ["-.2 -.15 -.1 -.05 -.01 0 .01 .05 .1 .15 .2",
                      "-2 -1.5 -1 -.5 -.1 0 .1 .5 1 1.5 2",
                      "-2 -1.5 -1 -.5 -.1 0 .1 .5 1 1.5 2"]
    elif field_type == "dilat_gravity":
        cbar_max   = [20,20,20]
        levels     = ["-20 -16 -12 -8 -4 0 4 8 12 16 20",
                      "-20 -16 -12 -8 -4 0 4 8 12 16 20",
                      "-20 -16 -12 -8 -4 0 4 8 12 16 20"]
    L          = 10000
    W          = 10000
    Nx         = 2000
    Ny         = 2000
    # Okubo range
    #Xmin       = [-5000, -5000, -5000]
    #Xmax       = [15000, 15000, 15000]
    #Ymin       = [-10000, -5000, -5000]
    #Ymax       = [10000, 15000, 15000]
    # Better looking range
    Xmin       = [-10000, -10000, -10000]
    Xmax       = [20000, 20000, 20000]
    Ymin       = [-15000, -10000, -10000]
    Ymax       = [15000, 20000, 20000]

    for i in range(len(plot_name)):
        return_value = system("python {} {} --field_type {} --plot_name {} --uniform_slip {} --colorbar_max {} --levels {} --rake {} --dip {} --DTTF {} --L {} --W {} --Xmin {} --Xmax {} --Ymin {} --Ymax {} --Nx {} --Ny {}".format(PYVQ, plot, field_type, plot_name[i], slip[i], cbar_max[i], levels[i], rake[i], dip[i], dttf, L, W, Xmin[i], Xmax[i], Ymin[i], Ymax[i], Nx, Ny))
# --------------------------------------------------------------------------





# ---- Plotting the fields of faults with prescribed slip
if TYPE == "single":
    plot    = "--field_plot"
    #fields  = ["gravity", "dilat_gravity"]
    fields = ["dilat_gravity"]
    slip    = 5
    #models = ["single_normal_dip60_switch_fault_10000.txt","single_normal_dip60_fault_10000.txt","single_thrust_dip30_fault_10000.txt","single_vert_strikeslip_RightLateral_fault_10000.txt","single_normal_dip45_switch_fault_10000.txt","single_thrust_dip45_switch_fault_10000.txt"]
    models  = ["single_vert_strikeslip_LeftLateral_fault_10000.txt","single_normal_dip45_fault_10000.txt","single_thrust_dip45_fault_10000.txt"]
    for model in models:
        print(model)
        for field in fields:
            if field == "gravity":
                if "strikeslip" in model.split("_"):
                    cbar_max = 50
                    levels = "-50 -40 -30 -20 -10 0 10 20 30 40 50"
                else:
                    cbar_max = 500
                    levels = "-500 -400 -300 -200 -100 0 100 200 300 400 500"
            elif field == "dilat_gravity":
                    cbar_max = 20
                    levels = "-20 -16 -12 -8 -4 0 4 8 12 16 20"
                    
            return_value = system("python {} {} --model_file {} --field_type {} --uniform_slip {} --colorbar_max {} --levels {} --small_model".format(PYVQ, plot, model, field, slip, cbar_max, levels))
# --------------------------------------------------------------------------





# ---- Plotting the fields of faults with prescribed slip
if TYPE == "Okubo":
    plot    = "--field_plot"
    fields  = ["geoid","gravity", "dilat_gravity"]
    models  = ["~/VQModels/single_vert_strikeslip_LeftLateral_fault_10000.txt","~/VQModels/thrust_dip45_switch_500x300km_fault_100kmElements.txt","~/VQModels/vert_strikeslip_LeftLateral_500x300km_fault_100kmElements.txt","~/VQModels/thrust_dip45_switch_10x10km_fault_2000mElements.txt"]
    #"single_thrust_dip45_fault_10000.txt","thrust_dip45_10x10km_fault_2000mElements.txt","single_thrust_dip45_switch_10x10km_fault_10000.txt"
    for model in models:
        print(model)
        for field in fields:
            if field == "gravity":
                slip = 5
                extra = "--small_model"
                if "strikeslip" in model.split("_"):
                    cbar_max = 50
                    levels = "-50 -40 -30 -20 -10 0 10 20 30 40 50"
                else:
                    cbar_max = 500
                    levels = "-500 -400 -300 -200 -100 0 100 200 300 400 500"
            elif field == "dilat_gravity":
                slip = 5
                extra = "--small_model"
                if "strikeslip" in model.split("_"):
                    cbar_max = 15
                    levels = "-15 -10 -5 0 5 10 15"
                else:
                    cbar_max = 30
                    levels = "-30 -20 -10 0 10 20 30"
                
            
            elif field == "geoid":
                slip = 10
                extra = ""
                if "strikeslip" in model.split("_"):
                    cbar_max = 1
                    levels = "-1 -.75 -.5 -.25 0 .25 .5 .75 1"
                else:
                    cbar_max = 5
                    levels = "-5 -4 -3 -2 -1 0 1 2 3 4 5"
                
            if field == "geoid" and not "500x300km" in model.split("_"):
                print "skipped"
            else:
                return_value = system("python {} {} --model_file {} --field_type {} --uniform_slip {} --colorbar_max {} --levels {} {}".format(PYVQ, plot, model, field, slip, cbar_max, levels, extra))
# --------------------------------------------------------------------------



# ------ Seeing how the field changes when increasing the number of elements
if TYPE == "num_elements":
    plot    = "--field_plot"
    field   = "gravity"
    model_dir = "../VQModels/"
    models  = ["single_thrust_dip45_switch_10x10km_fault_10000.txt","thrust_dip45_switch_10x10km_fault_5000mElements.txt","thrust_dip45_switch_10x10km_fault_3333mElements.txt","thrust_dip45_switch_10x10km_fault_2500mElements.txt","thrust_dip45_switch_10x10km_fault_2000mElements.txt","thrust_dip45_switch_10x10km_fault_1kmElements.txt"]
    for model in models:
        model = model_dir+model
        print(model)
        if field == "gravity":
            slip = 5
            if "strikeslip" in model.split("_"):
                cbar_max = 50
                levels = "-50 -40 -30 -20 -10 0 10 20 30 40 50"
            else:
                cbar_max = 500
                levels = "-500 -400 -300 -200 -100 0 100 200 300 400 500"
        elif field == "dilat_gravity":
            slip = 5
            if "strikeslip" in model.split("_"):
                cbar_max = 15
                levels = "-15 -10 -5 0 5 10 15"
            else:
                cbar_max = 30
                levels = "-30 -20 -10 0 10 20 30"

        return_value = system("python {} {} --model_file {} --field_type {} --uniform_slip {} --colorbar_max {} --levels {} --small_model".format(PYVQ, plot, model, field, slip, cbar_max, levels))




