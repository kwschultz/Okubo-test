import sys
sys.path.append("/home/kasey/PyVC/")

import numpy as np
import matplotlib.pyplot as plt
#=============================================================================
#Trying to replicate plot in Okubo '92
_C      = 11000.0   #meters
_DIP    = np.pi/3.0
_L      = 10000.0
_W      = 10000.0
_US     = 0.0
_UD     = -5.0
_UT     = 0.0
_LAMBDA = 1.0
_MU     = 1.0

_Xmin,_Xmax = -5000.0,15000.0
_Nx         = 500.0
_Ymin,_Ymax = -10000.0,10000.0
_Ny         = 500.0


#-----------------------------------------------------------------------------
def get_displacements(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib

    okada = quakelib.Okada()
    loc   = quakelib.Vec3(x,y,0.0)

    dx,dy,dz = okada.calc_displacement_vector(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (dx,dy,dz)
#-----------------------------------------------------------------------------
def get_dh(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib
    okada = quakelib.Okada()
    
    return okada.dH(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU)
#-----------------------------------------------------------------------------
def get_dg(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib

    okada = quakelib.Okada()
    loc   = quakelib.Vec3(x,y,0.0)

    return okada.dg(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU)
#-----------------------------------------------------------------------------
def get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep):
    X       = np.arange(Xmin,Xmax,Xstep,dtype=np.dtype('d'))
    Y       = np.arange(Ymin,Ymax,Ystep,dtype=np.dtype('d'))
    return X,Y
#-----------------------------------------------------------------------------
def get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny):
    x   = np.linspace(Xmin,Xmax,num=Nx)
    y   = np.linspace(Ymin,Ymax,num=Ny)
    return x,y
#-----------------------------------------------------------------------------
def get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib
    
    okada   = quakelib.Okada() 
    #X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    Z       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            loc     = quakelib.Vec3(XX[i][j],YY[i][j],0.0)
            Z[i][j] = okada.calc_displacement_vector(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)[2]
            #Z[i][j] = get_displacement(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)[2]
    
    return (XX,YY,Z)
#-----------------------------------------------------------------------------
def get_dh_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    #X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    H       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            H[i][j] = okada.dH(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,H)
#-----------------------------------------------------------------------------
def get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    #X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    DG      = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            DG[i][j] = okada.dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU) 
            #DG[i][j] = get_dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,DG)
#-----------------------------------------------------------------------------
def get_dg2_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    #X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    DG2     = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            DG2[i][j] = okada.dg2(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU) 
            #DG[i][j] = get_dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,DG2)
#-----------------------------------------------------------------------------
def plot_dz(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    from scipy.interpolate import griddata
    import sys    

    #X,Y = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY,Z = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)

    #V = [-.01,-.005,-.0025,0,.0025,.005,.01]
    #N=8

    DZplot = plt.imshow(Z, origin = 'lower', extent=[Xmin,Xmax,Ymin,Ymax])

    #plt.contourf(X,Y,Z,N,origin='lower',extent=(Xmin,Xmax,Ymin,Ymax))

    res = (Xmax-Xmin)/float(Nx)

    plt.colorbar()  
    filename = './test_dz_plot_'+str(int(res))+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def plot_dg(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import matplotlib as mpl

    #if mode==1:
    #    XX,YY,DG = get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    #if mode==2:
    
    XX,YY,DG = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    #dum,dum,DG2 = get_dg2_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)


    UNIT = pow(10,-8)

    MYcmap = mpl.colors.ListedColormap(['#0000CC','#0066FF','#66FFFF','#99CCFF','#FFFFFF','#FFFF00','#FF9933','#FF0000','#800000'])
    #bounds = [-3000*UNIT,-1500*UNIT,-1000*UNIT,-500*UNIT,-100*UNIT,100*UNIT,500*UNIT,1000*UNIT,1500*UNIT,3000*UNIT]
    bounds = [-50*UNIT  ,-40*UNIT  ,-30*UNIT  ,-20*UNIT ,-5*UNIT  ,5*UNIT  ,20*UNIT ,30*UNIT ,40*UNIT  ,50*UNIT]
    MYnorm = mpl.colors.BoundaryNorm(bounds,MYcmap.N)
    
    plt.figure()
    DGplot = plt.imshow(DG, origin = 'lower',interpolation='nearest',extent=[Xmin/1000.0,Xmax/1000.0,Ymin/1000.0,Ymax/1000.0],cmap=MYcmap,norm=MYnorm) 

    plt.colorbar(DGplot, cmap=MYcmap, norm=MYnorm, boundaries=bounds, format='%.1e')
    dip_deg = 180.0*dip/np.pi
    
    zero_index = np.where((XX==0)&(YY==0))
    L_index    = np.where((XX==L)&(YY==0))
    
    #plt.autoscale(False)
    #plt.axhline(y=0,xmin=0,xmax=L/1000.0,linewidth=4,color='k')
    
    title = 'Strike Slip Okubo gravity change [m/s^2]\nc=%.1fkm, L=%.1fkm, W=%.1fkm, dip=%.1fdeg, slip=%.1fm\n'%(c/1000.0,L/1000.0,W/1000.0,dip_deg,US)
    plt.title(title)
    #filename = './dg_plot_'+'c'+str(int(c/1000.0))+'km_'+str(int(_Xstep))+'m_res_OkadaUZ.png'
    filename = './dg_plot_difference_OkadaUZ_OkuboDH.png'
    plt.xlabel('X [km]')
    plt.ylabel('Y [km]')
    plt.savefig(filename,dpi=200)
    print '>>> plot saved: '+filename
    plt.show()
#-----------------------------------------------------------------------------
def plot_dz_dh_diff(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import matplotlib
    
    my_cmap = matplotlib.cm.get_cmap('rainbow')
    my_cmap.set_under('w')
    
    XX,YY,DZ   = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DH = get_dh_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    
    this_plot  = plt.imshow(DZ-DH,origin='lower',extent=[Xmin,Xmax,Ymin,Ymax], cmap=my_cmap,interpolation='none')
    
    res = (Xmax-Xmin)/float(Nx)
    
    plt.colorbar(this_plot,format='%.3f')
    filename = './test_dg_dz_diff_plot_'+str(int(res))+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def plot_dg_dg2_diff(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import matplotlib
    
    my_cmap = matplotlib.cm.get_cmap('rainbow')
    my_cmap.set_under('w')
    
    XX,YY,DG    = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DG2 = get_dg2_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    
    this_plot  = plt.imshow(DG-DG2,origin='lower',extent=[Xmin,Xmax,Ymin,Ymax], cmap=my_cmap,interpolation='none')
    
    res = (Xmax-Xmin)/float(Nx)
    
    plt.colorbar(this_plot,format='%.3f')
    filename = './test_dg_dg2_diff_plot_'+str(int(res))+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def bin_2d(x,y) :
    import math

    if np.shape(x) != np.shape(y):
        raise NameError('Array shape mismatch, insert coin(s) to continue.')

    num_bins = math.floor(len(x)/100.0)
    
    if num_bins <= 20:
        num_bins = 20
    elif num_bins >= 100:
        num_bins = 100
    
    x = np.array(x)
    y = np.array(y)
    
    bin_min = math.floor(np.min(x))
    bin_max = math.ceil(np.max(x))
    
    bins = np.linspace(bin_min,bin_max,num=num_bins)
       
    inds = np.digitize(x, bins)
    
    binned_data = {}

    for n, iBin in enumerate(inds):
        try:
            binned_data[iBin].append(y[n])
        except KeyError:
            binned_data[iBin] = [y[n]]

        
    x_ave = []
    y_ave = []
    for k in sorted(binned_data.keys()):
        if k != 0:
            if k==len(bins):
                #Catch the bins that are excluded to the right of the last bin
                k=len(bins)-1
                x_ave.append(0.5*(bins[k-1]+bins[k]))
                y_ave.append(sum(binned_data[k])/float(len(binned_data[k])))
            else:
                x_ave.append(0.5*(bins[k-1]+bins[k]))
                y_ave.append(sum(binned_data[k])/float(len(binned_data[k])))
        
    return x_ave, y_ave
    
#-----------------------------------------------------------------------------
def plot_dg_vs_uz(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,returns=False):
    from pyvc import vcplots
    import os
    
    # Need to remove a cached file for Arial fonts to be used
    if os.path.exists('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
        
    UNIT        = float(pow(10,-8))  # 1 microgal in mks units is 10^(-8) m/s^2
    
    XX,YY,DG    = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DZ  = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    del(XX)
    del(YY)
    
                    ## In units of microgals
    DG_flat = DG.flatten()/UNIT
    DZ_flat = DZ.flatten()
    
    del(DG)
    del(DZ)
    
    #DG      = np.array([okada.dg(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU) for x,y in zip(X,Y)])/UNIT
    #UZ      = np.array([okada.calc_displacement_vector(quakelib.Vec3(x,y,0.0),c,dip,L,W,US,UD,UT,LAMBDA,MU)[2] for x,y in zip(X,Y)])

    #x_ave,y_ave = vcutils.calculate_averages(UZ,DG)
    x_ave,y_ave = bin_2d(DZ_flat,DG_flat)
    
    
    fault_type = ""
    if US!=0.0:
        fault_type = "strikeslip"
        plot_lab   = "Strike Slip"
    if UD!=0.0:
        if UD>0:
            fault_type = "thrust"
            plot_lab   = "Thrust"
        if UD<0:
            fault_type = "normal"
            plot_lab   = "Normal"
    if UT!=0.0:
        fault_type = "tensile"
        plot_lab   = "Tensile"
        
    dip_deg     = dip*180.0/np.pi

    res = (Xmax-Xmin)/float(Nx)

    output_file = "/home/kasey/Okubo-test/dg_vs_uz_"+fault_type+"_c%ikm_L%ikm_W%ikm_dip%i_%im.png"%(c/1000.0,L/1000.0,W/1000.0,dip_deg,res)
    Plot_Label  = r"$\Delta$g vs. height change: "+plot_lab+" c=%ikm L=%ikm W=%ikm dip=%i$^\circ$"%(c/1000.0,L/1000.0,W/1000.0,dip_deg)

    #Before plotting, clear the current axis and figure
    plt.cla()
    plt.clf()

    vcplots.standard_plot(output_file,DZ_flat,DG_flat,
        axis_format='plot',
        add_lines=[{'label':'binned average', 'x':x_ave, 'y':y_ave}],
        axis_labels = {'x':'vertical displacement [m]', 'y':r'gravity change [$\mu$gal]'},
        plot_label=Plot_Label
    )       
    if returns:
        return DZ_flat,DG_flat,x_ave,y_ave
#-----------------------------------------------------------------------------    
#def dg_vs_uz_multi_plot(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,LAMBDA,MU):
    

    
    


#plot_dg(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
#plot_dz(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
#plot_dz_dh_diff(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
#plot_dg_dg2_diff(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)

plot_dg_vs_uz(_Xmin,_Xmax,_Nx,_Ymin,_Ymax,_Ny,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)












