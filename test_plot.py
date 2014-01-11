import sys
sys.path.append("/home/kasey/PyVC/")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import quakelib
import math
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.font_manager as mfont

if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
    os.remove('/home/kasey/.matplotlib/fontList.cache')

#=============================================================================
def bin_2d(x,y,bmin=None,bmax=None,all_vals=False) :

    if np.shape(x) != np.shape(y):
        raise NameError('Array shape mismatch, insert coin(s) to continue.')

    num_bins = math.floor(len(x)/100.0)
    
    if num_bins <= 20:
        num_bins = 20
    elif num_bins >= 100:
        num_bins = 100
    
    
    x       = np.array(x)
    y       = np.array(y)
    
    if bmin==None and bmax==None:
        bmin = math.floor(np.min(x))
        bmax = math.ceil(np.max(x))
        
    bins    = np.linspace(bmin,bmax,num=num_bins) 
    inds    = np.digitize(x, bins)
    x_ave   = []
    y_ave   = []
    binned_data = {}

    for n, iBin in enumerate(inds):
        try:
            binned_data[iBin].append(y[n])
        except KeyError:
            binned_data[iBin] = [y[n]]

    KEYS = binned_data.keys()

    if all_vals:
        if 0 in KEYS:
            x_ave.append(bmin)
            y_ave.append(sum(binned_data[0])/float(len(binned_data[0])))  

    """for k in sorted(KEYS):
        if k != 0:
            if k==len(bins):
                #Catch the bins that are excluded to the right of the last bin
                k=len(bins)-1
                x_ave.append(0.5*(bins[k-1]+bins[k]))
                y_ave.append(sum(binned_data[k])/float(len(binned_data[k])))
            else:
                x_ave.append(0.5*(bins[k-1]+bins[k]))
                y_ave.append(sum(binned_data[k])/float(len(binned_data[k])))    
    """
    for k in sorted(KEYS):
        if k>0 and k < len(bins):
                x_ave.append(0.5*(bins[k-1]+bins[k]))
                y_ave.append(sum(binned_data[k])/float(len(binned_data[k])))
            

    if all_vals:            
        if len(bins) in KEYS:
            x_ave.append(bmax)
            y_ave.append(sum(binned_data[len(bins)])/float(len(binned_data[len(bins)])))
                

    return np.array(x_ave), np.array(y_ave)
#-----------------------------------------------------------------------------

def hist_1d(x,bmin=None,bmax=None,norm=False,num_bins=100):
    x       = np.array(x)

    if bmin==None and bmax==None:
        bmin = math.floor(np.min(x))
        bmax = math.ceil(np.max(x)) 
        
    bins    = np.linspace(bmin,bmax,num=num_bins) 
    inds    = np.digitize(x, bins)
    x_ave   = []
    count   = []
    binned_data = {}

    for n, iBin in enumerate(inds):
        try:
            binned_data[iBin].append(x[n])
        except KeyError:
            binned_data[iBin] = [x[n]]


    KEYS    = binned_data.keys()
    # Put values below minimum bin into first bin
    if 0 in KEYS:
        x_ave.append(bmin)
        count.append(len(binned_data[0]))  
    
    for k in sorted(KEYS):
        if k!=0:
            if k<len(bins):
                x_ave.append(0.5*(bins[k-1]+bins[k]))            
                count.append(len(binned_data[k]))
                
    # Put values above maximum bin into last bin             
    if len(bins) in KEYS:
        x_ave.append(bmax)
        count.append(float(len(binned_data[len(bins)])))
                           
    x_ave = np.array(x_ave)
    count = np.array(count)
    
    if norm:
        count /= float(len(x)) 
           
    return x_ave,count

#-----------------------------------------------------------------------------
def get_slope_intercept(x,y):
    from scipy import stats
  
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    return slope,intercept

#-----------------------------------------------------------------------------
def get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny):
    x   = np.linspace(Xmin,Xmax,num=Nx)
    y   = np.linspace(Ymin,Ymax,num=Ny)
    return x,y

#-----------------------------------------------------------------------------
def get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,
               DG=False,DH=False,DZ=False,DG2=False,DV=False):
    
    okada   = quakelib.Okada() 
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    MAT     = np.zeros(XX.shape)

    if DG:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec2(XX[i][j],YY[i][j])
                MAT[i][j] = okada.calc_dg(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    elif DV:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec3(XX[i][j],YY[i][j],0.0)
                MAT[i][j] = okada.calc_dV(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
                
    elif DG2:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec2(XX[i][j],YY[i][j])
                MAT[i][j] = okada.calc_dg2(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)    
    elif DZ:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec3(XX[i][j],YY[i][j],0.0)         
                MAT[i][j] = okada.calc_displacement_vector(loc,c,dip,L,W,US,
                                                           UD,UT,LAMBDA,MU)[2]
    elif DH:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec2(XX[i][j],YY[i][j])
                MAT[i][j] = okada.calc_dh(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    else:
        raise IOError('You must choose one of: DG,DH,DG2,DZ')
    
    
    return (XX,YY,MAT)

#-----------------------------------------------------------------------------

def get_filename(c,dip,L,W,US,UD,UT,folder,pre='none',suff='none'):
    
    dip_deg = round(180.0*dip/np.pi)
    
    fault_type = ""
    if US!=0.0:
        slip = US
        fault_type = "strikeslip"
    if UD!=0.0:
        slip = UD
        if UD>0:
            fault_type = "thrust"
        else:
            fault_type = "normal"
    if UT!=0.0:
        slip = UT
        fault_type = "tensile"
    
    if pre=='none':
        f0 = folder.split('_')[0]
    else:
        f0 = pre
        
    f1 = '_'+fault_type+str(int(abs(slip)))+'_dip'+str(int(round(dip_deg)))
    f2 = '_L'+str(int(round(L/1000.0)))+'k_'+'W'+str(int(round(W/1000.0)))+'k'
    f3 = '_c'+str(int(round(c/1000.0)))+'k'
    
    if suff != 'none':
        f3 = f3+'_'+suff+'.png'
    else:
        f3 = f3+'.png'
    
    filename = folder+'/'+f0+f1+f2+f3
    return filename,fault_type
    

#-----------------------------------------------------------------------------
def cbar_plot(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,
              save=False,DG2=False,DG=True,DZ=False,DH=False,
              DIFFZ=False,DIFFG=False,CLIMITS=False,SUFFIX='none',
              HIST=False,SHOW=False,DV=False):
    
    # Need to remove a cached file for Arial fonts to be used
    if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
    
    ticklabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=9)
    framelabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=10)
    
    """
    Immutable constants: (hard coded in quakelib/src/QuakeLibOkada.cpp) all MKS
        Free-air gravity gradient (Okubo '92):   Beta = 0.00000309 1/s^2
                                                      = 309 microgal/m
        Constant crustal density:                Rho  = 2670.0 kg/m^3
        Gravitational constant:                  G    = 0.000000000066738
    
    Vertical displacement calculations:::
        DH: Method outlined in Okubo '92
        DZ: Method previously implemented, from Okada
        
    Gravity change calculations:::
        DG2: Complete implementation of Okubo '92 method
        DG:  Okubo '92 formulas for gravity change functionals,
                but using in-place version of Okada's half-space 
                deformation equations    
    """ 
    #--------  Choose the data to plot     vvvvvv  -----------
    if DIFFG:
        #        Plot difference between DG and DG2 calculations.
        filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'diff_plots',
                                           pre='dg-dg2',suff=SUFFIX)

        XX,YY,DG    = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DG=True)
        XX,YY,DG2   = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=True)
        Data        = DG - DG2   
        FMT         = '%.2f'    
        UNIT        = pow(10,-8)  #micro gals
        CLABEL      = r'Gravity change $[\mu gal]$'
    elif DIFFZ:
        #        Plot difference between Okubo (DH) and Okada (DZ) vertical displacements
        filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'diff_plots',
                                              pre='dz-dh',suff=SUFFIX)
        
        XX,YY,H     = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,
                                    UT,LAMBDA,MU,DH=True)
        XX,YY,Z     = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,
                                    UT,LAMBDA,MU,DZ=True)
        Data        = Z - H
        FMT         = '%.1f'
        UNIT        = pow(10,-2)  # centimeters  
        CLABEL      = r'$\Delta z \ [cm]$'
    elif DV:
        XX,YY,dv    = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DV=True)
        UNIT        = 1.0 #pow(10,-4)  #GUESS?!?!?!
        CLABEL      = r'Gravitational potential change $[units??]$'
        FMT         = '%i'   
        Data        = dv
        filename    = 'test_dV.png'
        
        
    elif not DZ and not DH:
        #        Plot either DG or DG2
        pre                 = ('dg2' if DG2 else 'dg')
        filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'dg_plots',
                                              pre=pre,suff=SUFFIX)
                
        XX,YY,Data  = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=DG2,DG=DG)
        FMT         = '%i'
        UNIT        = pow(10,-8)  #micro gals
        
        if fault_type == 'strikeslip':
            CMIN,CMAX   = -50,50
            #plot_lab    = "Strike-slip"
        elif fault_type == 'thrust':
            CMIN,CMAX   = -500,500
            #plot_lab    = "Thrust"
        elif fault_type == 'normal':
            CMIN,CMAX   = -500,500
            #plot_lab    = "Normal"
        else:
            CMIN,CMAX   = -400,400
            #plot_lab    = "Tensile"
            
        CLABEL      = r'gravity changes $[\mu gal]$'
    else:
         #        Plot either DZ or DH
        pre                 = ('dh' if DH else 'dz')
        filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'dz_plots',
                                           pre=pre,suff=SUFFIX)        
        XX,YY,Data  = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DH=DH,DZ=DZ)
        FMT         = '%.2f'
        UNIT        = pow(10,-2)  # centimeters  
        CLABEL      = r'$\Delta z \ [cm]$'         
    #---------------------------------------------------------
    
    if HIST:
        savename = filename.split('.')[0]+'_hist.png'
        DG_flat  = Data.flatten()/UNIT        
        plot_dg_hist(DG_flat,savename)
    
    
    
    # Make the figure   
    this_fig    = plt.figure()
    fig_axes    = plt.subplot(111)
    this_img    = plt.imshow(Data/UNIT, origin = 'lower',interpolation='nearest',
                         extent=[Xmin/1000.0,Xmax/1000.0,Ymin/1000.0,
                                 Ymax/1000.0],cmap=plt.get_cmap('seismic'))
    
    # Tighten up the axis labels
    img_ax        = this_fig.gca()
    img_ax.set_xlabel(r'along fault [$km$]',labelpad=-1, fontproperties=framelabelfont)
    img_ax.set_ylabel(r'[$km$]',labelpad=-5, fontproperties=framelabelfont)
    
    if CLIMITS:
        forced_ticks  = [int(num) for num in np.linspace(CMIN,CMAX,11)]
    else:
        Data          = np.array(Data)
        forced_ticks  = [num for num in np.linspace(Data.min(),Data.max(),11)]
    
    # Make color bar and put its label below its x-axis
    divider       = make_axes_locatable(fig_axes)
    cbar_ax       = divider.append_axes("top", size="5%",pad=0.02)                       
    cbar          = plt.colorbar(this_img,format=FMT,
                               orientation='horizontal',cax=cbar_ax,
                               ticks=forced_ticks)
    if CLIMITS:
        plt.clim(CMIN,CMAX)
    
    # Make and position colorbar label
    cbar_ax.set_xlabel(CLABEL,labelpad=-40, fontproperties=framelabelfont)
    cbar_ax.tick_params(axis='x',labelbottom='off',labeltop='on',
                        bottom='off',top='off',right='off',left='off',pad=-0.5)
    
    
    # Want to change outermost tick labels on colorbar
    #   from 'VALUE','-VALUE' to '>VALUE' and '<-VALUE'  
    if not DV:  
        cb_tick_labs = [str(num) for num in forced_ticks]
        cb_tick_labs[0] = '<'+cb_tick_labs[0]
        cb_tick_labs[-1] = '>'+cb_tick_labs[-1]
        cbar.ax.set_xticklabels(cb_tick_labs)
      
    for label in img_ax.xaxis.get_ticklabels()+img_ax.yaxis.get_ticklabels():
        label.set_fontproperties(framelabelfont)  
        
    for label in cbar_ax.xaxis.get_ticklabels()+cbar_ax.yaxis.get_ticklabels():
        label.set_fontproperties(ticklabelfont)        
      
      
      
    # Draw a projection of the fault
    W_proj      = W*np.cos(dip)  #projected width of fault due to dip angle
    fault_proj  = mpl.patches.Rectangle((0.0,0.0),L/1000.0,W_proj/1000.0,
                                        ec='k',fc='none',fill=False,
                                        ls='solid',lw=4.0)
    fig_axes.add_patch(fault_proj)
    
    # Save the plot
    if save:
        plt.savefig(filename,dpi=300)
        print '>>> plot saved: '+filename
        
    if SHOW:
        plt.show()
        
    plt.clf()
#-----------------------------------------------------------------------------

def plot_for_cutoff(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,
              save=False,SHOW=False,_CLIMS=False):
    
    TRIG_TOLERANCE = 0.0001
    NUM_BINS       = 50
    NUM_TICKS      = 5
    
    ticklabelfont = mfont.FontProperties(family='Serif', style='normal', variant='normal', size=8)
    framelabelfont = mfont.FontProperties(family='Serif', style='normal', variant='normal', size=8)
        
    XX,YY,dv    = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DV=True)
    UNIT        = 1.0 #pow(10,-4)  #GUESS?!?!?!
    CLABEL      = r'Gravitational potential change $[units??]$'
    FMT         = '%.4f'   
    Data        = dv
    filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'finding_cutoff_plots',
                                           pre='potential')
    R           = []
    
    def sin_o(dip):
        if abs(np.sin(dip)) < TRIG_TOLERANCE :
            return 0.0
        else:
            return np.sin(dip)
        
    def cos_o(dip):
        if abs(np.cos(dip)) < TRIG_TOLERANCE :
            return 0.0
        else:
            return np.cos(dip)
        
    cos_o_dip = cos_o(dip)
    sin_o_dip = sin_o(dip)
        
    #Centroid of fault segment
    x_c         = -0.5*W*cos_o_dip
    y_c         = 0.5*L
    z_c         = 0.5*W*sin_o_dip - c
    
    
    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            x = XX[i][j]
            y = YY[i][j]
            
            dist_numerator   = (x - x_c)**2 + (y-y_c)**2 + z_c**2 
            dist_denominator = float(L*W)
            
            dist = np.sqrt(dist_numerator/dist_denominator)
            R.append(dist)
    
            
    R_bin_vals,counts = hist_1d(R,bmin=min(R),bmax=max(R),norm=True,num_bins=NUM_BINS) 
    this_fig    = plt.figure()
    fig_axes    = plt.subplot(121)
    plt.plot(R_bin_vals,counts,c='k')        

    # Make the figure   
    fig_axes    = plt.subplot(122)
    this_img    = plt.imshow(Data/UNIT, origin = 'lower',interpolation='nearest',
                         extent=[Xmin/1000.0,Xmax/1000.0,Ymin/1000.0,
                                 Ymax/1000.0],cmap=plt.get_cmap('seismic'))
    
    # Tighten up the axis labels
    img_ax        = this_fig.gca()
    img_ax.set_xlabel(r'along fault [$km$]',labelpad=-1, fontproperties=framelabelfont)
    img_ax.set_ylabel(r'[$km$]',labelpad=-5, fontproperties=framelabelfont)
    
    
    if _CLIMS:
        LIM = 0.001
    else:
        max_val       = abs(Data.max())
        min_val       = abs(Data.min())
        LIM           = max([max_val,min_val])
        
        
    forced_ticks  = [num for num in np.linspace(-LIM,LIM,NUM_TICKS)]
    
    # Make color bar and put its label below its x-axis
    divider       = make_axes_locatable(fig_axes)
    cbar_ax       = divider.append_axes("top", size="5%",pad=0.02)                       
    cbar          = plt.colorbar(this_img,format=FMT,
                               orientation='horizontal',cax=cbar_ax,
                               ticks=forced_ticks)
    
    plt.clim(-LIM,LIM)
    
    # Make and position colorbar label
    cbar_ax.set_xlabel(CLABEL,labelpad=-40, fontproperties=framelabelfont)
    cbar_ax.tick_params(axis='x',labelbottom='off',labeltop='on',
                        bottom='off',top='off',right='off',left='off',pad=-0.5)

    # Draw a projection of the fault
    W_proj      = W*np.cos(dip)  #projected width of fault due to dip angle
    fault_proj  = mpl.patches.Rectangle((0.0,0.0),L/1000.0,W_proj/1000.0,
                                        ec='c',fc='none',fill=False,
                                        ls='solid')
    fig_axes.add_patch(fault_proj)
    
    
    for label in img_ax.xaxis.get_ticklabels()+img_ax.yaxis.get_ticklabels():
        label.set_fontproperties(framelabelfont)  
        
    for label in cbar_ax.xaxis.get_ticklabels()+cbar_ax.yaxis.get_ticklabels():
        label.set_fontproperties(ticklabelfont)  
    
    plt.clim(-LIM,LIM)
    
    # Save the plot
    if save:
        plt.savefig(filename,dpi=300)
        print '>>> plot saved: '+filename
        
    if SHOW:
        plt.show()
        
    plt.clf()
#-----------------------------------------------------------------------------


def plot_dg_vs_uz_simple(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,
                         LABELS=False,SUFFIX='none'):
    from pyvc import vcutils
    import os
    
    ticklabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=9)
    framelabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=10)
    legendfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=10)
    titlefont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=12)
    
    
    # Need to remove a cached file for Arial fonts to be used
    if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
        
    UNIT       = float(pow(10,-8))  # 1 microgal in mks units is 10^(-8) m/s^2
    
    dum,dum,DG  = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DG=True)
    dum,dum,DZ  = get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DZ=True)
    
    del(dum)
    
                    ## In units of microgals
    DG_flat = DG.flatten()/UNIT
    DZ_flat = DZ.flatten()
    
    del(DG)
    del(DZ)
       
    if US>0.0:
        fault_type = "strikeslip"
        plot_lab   = "Strike-slip"
    if UD>0.0:
        if UD>0:
            fault_type = "thrust"
            plot_lab   = "Thrust"
        if UD<0:
            fault_type = "normal"
            plot_lab   = "Normal"
    if UT>0.0:
        fault_type = "tensile"
        plot_lab   = "Tensile"
        
    dip_deg     = int(round(dip*180.0/np.pi))
    
    CC = int(round(c/1000.0))
    LL = int(round(L/1000.0))
    WW = int(round(W/1000.0))

    if SUFFIX is not 'none':
        output_file = "/home/kasey/Okubo-test/dg_vs_uz/dg_dz_{}_c{}km_L{}km_W{}km_dip{}_{}.png".format(fault_type,CC,LL,WW,dip_deg,SUFFIX)
    else:
        output_file = "/home/kasey/Okubo-test/dg_vs_uz/dg_dz_{}_c{}km_L{}km_W{}km_dip{}.png".format(fault_type,CC,LL,WW,dip_deg)

    #Before plotting, clear the current axis and figure
    plt.clf()
    
    x_ave,y_ave     = bin_2d(DZ_flat,DG_flat)
    
    slope,intercept = get_slope_intercept(x_ave,y_ave)
    y_fit           = slope*x_ave + intercept   

    fit_label       = 'slope = {:.3f}'.format(slope)

    plt.plot(DZ_flat,DG_flat,'.',c='k')
    plt.plot(x_ave,y_fit,c='grey',label=fit_label,lw=2)
    this_ax = plt.gca()
    
    this_ax.set_title(plot_lab, fontproperties=titlefont)
    
    for label in this_ax.xaxis.get_ticklabels()+this_ax.yaxis.get_ticklabels():
        label.set_fontproperties(ticklabelfont)
    
    if LABELS:    
        XLABEL  = r'vertical displacement $[m]$'
        YLABEL  = r'gravity change $[\mu gal]$'
        this_ax.set_xlabel(XLABEL, fontproperties=framelabelfont)
        this_ax.set_ylabel(YLABEL, fontproperties=framelabelfont)
    
    this_ax.legend(loc=1,frameon=False,prop=legendfont)
    plt.savefig(output_file,dpi=200)

    """vcutils.standard_plot(output_file,DZ_flat,DG_flat,
        axis_format='plot',
        add_lines=[{'label':'binned average', 'x':x_ave, 'y':y_ave}],
        axis_labels = {'x':'vertical displacement [m]', 'y':r'gravity change [$\mu$gal]'},
        plot_label=Plot_Label
    )      
    """
    
#----------------------------------------------------------------------------- 
def plot_dg_vs_uz_event(evnum,sim_file):
    from pyvc import vcutils
    import os
    
    ticklabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=9)
    framelabelfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=10)
    legendfont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=10)
    titlefont = mfont.FontProperties(family='Arial', style='normal', variant='normal', size=12)
        
    # Need to remove a cached file for Arial fonts to be used
    if os.path.isfile('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
    
    # get the gravity field of the event
    UNIT     = pow(10,-8) #microgals
    dg_field,mag,slip,num_elem = get_field(evnum,sim_file,
                                                    field_type='gravity',
                                                    mag=True,avg_slip=True,
                                                    num_elem=True)
    dg       = dg_field.dG.flatten()/UNIT
    
    # get the vertical displacement field of the event
    dz_field = get_field(evnum,sim_file,field_type='displacement')       
    dz       = dz_field.dZ.flatten()
       
    #Before plotting, clear the current axis and figure
    plt.clf()
    
    # binning and fitting
    x_ave,y_ave     = bin_2d(dz,dg)
    slope,intercept = get_slope_intercept(x_ave,y_ave)
    y_fit           = slope*x_ave + intercept   
    fit_label       = 'slope = {:.3f}'.format(slope)

    # plot the raw and binned & fitted data
    plt.plot(dz,dg,'.',c='k')
    plt.plot(x_ave,y_fit,c='grey',label=fit_label,lw=2)
    this_ax = plt.gca()
    
        
    # font and labels
    PLOT_LABEL  = 'Magnitude {:.2f} event, {} fault elements, avg. slip = {:.2f}m'.format(mag,slip,num_elem)
    XLABEL      = r'height change $[m]$'
    YLABEL      = r'gravity change $[\mu gal]$'  
    
    this_ax.set_title(PLOT_LABEL, fontproperties=titlefont)
    
    for label in this_ax.xaxis.get_ticklabels()+this_ax.yaxis.get_ticklabels():
        label.set_fontproperties(ticklabelfont)
    
    this_ax.set_xlabel(XLABEL, fontproperties=framelabelfont)
    this_ax.set_ylabel(YLABEL, fontproperties=framelabelfont)
    
    this_ax.legend(loc=1,frameon=False,prop=legendfont)
    
    # Saving
    output_file = "/home/kasey/Okubo-test/dg_vs_uz/dg_dz_{}.png".format(evnum)
    plt.savefig(output_file,dpi=200)   
#-----------------------------------------------------------------------------


def get_field(evnum,sim_file,field_type='gravity',mag=False,avg_slip=False,
              num_secs=False,num_elem=False):
    from pyvc import *
    from operator import itemgetter
    from pyvc import vcplots
    import sys
    
    output_directory        = 'animation_test_g/'
    field_values_directory  = '{}field_values/'.format(output_directory)
    
    padding   = 0.01
    cutoff    = None

    with VCSimData() as sim_data:
        sim_data.open_file(sim_file)    
        events              = VCEvents(sim_data)
        geometry            = VCGeometry(sim_data)
        min_lat             = geometry.min_lat
        max_lat             = geometry.max_lat
        min_lon             = geometry.min_lon
        max_lon             = geometry.max_lon
        base_lat            = geometry.base_lat
        base_lon            = geometry.base_lon
        event_data          = events[evnum]
        event_element_slips = events.get_event_element_slips(evnum)
        event_sections      = geometry.sections_with_elements(event_element_slips.keys())
                
        if field_type=='gravity':
            EF = vcplots.VCGravityField(min_lat, max_lat, min_lon, max_lon, base_lat, base_lon, padding=padding)
        else:
            EF = vcplots.VCDisplacementField(min_lat, max_lat, min_lon, max_lon, base_lat, base_lon, padding=padding)
                
        field_values_loaded = EF.load_field_values('{}{}_'.format(field_values_directory, evnum))
        
    
        if field_values_loaded:
            sys.stdout.write('loaded'.format(evnum))
            # If they havent been saved then we need to calculate them
        elif not field_values_loaded:
            sys.stdout.write('processing '.format(evnum))
            sys.stdout.flush()
                        
            ele_getter = itemgetter(*event_element_slips.keys())
            event_element_data = ele_getter(geometry)
            if len(event_element_slips) == 1:
                event_element_data = [event_element_data]
                        
            sys.stdout.write('{} elements :: '.format(len(event_element_slips)))
            sys.stdout.flush()
                        
            EF.calculate_field_values(
                                      event_element_data,
                                      event_element_slips,
                                      cutoff=cutoff,
                                      save_file_prefix='{}{}_'.format(field_values_directory, evnum)
                                      )
    
    '{} elements in {} sections : '.format(len(event_element_slips), len(event_sections))
    
    
    if mag or avg_slip or num_secs or num_elem:
        returning = []
        returning.append(EF)
        if mag:
            returning.append(event_data[3])
        if avg_slip:
            returning.append(event_data[13])
        if num_secs:
            returning.append(len(event_element_slips))
        if num_elem:
            returning.append(len(event_sections))
        
        return returning
    else:
        return EF
#-----------------------------------------------------------------------------

def plot_dg_hist(evnum,sim_file,bin_min=-30.0,bin_max=-30.0,NUM_BINS=100,NORM=False):
    from matplotlib import pyplot as plt
    
    UNIT        = pow(10,-8) #microgals
    event_field = get_field(evnum,sim_file,field_type='gravity')
    dg          = event_field.dG.flatten()/UNIT
    
    dg_bin_vals,counts = hist_1d(dg,bmin=bin_min,bmax=bin_max,norm=NORM,num_bins=NUM_BINS) 
       
    LABEL =    'M = '+str(round(mag,2))
    plt.plot(dg_bin_vals,counts,label=LABEL,color='k')
    plt.tick_params(axis='y',bottom='off',top='off',left='off',right='off',
                labelbottom='off',labeltop='off',labelleft='off',labelright='off')
    plt.tick_params(axis='x',top='off',bottom='off')
    plt.legend(loc=2)
    img_ax        = plt.gca()
    img_ax.set_xlabel(r'Gravity change $[\mu gal]$',labelpad=-1)
    
    #plt.savefig('local/dg_hist_ev'+str(evnum)+'.png',dpi=200)
    #plt.clf()
    plt.show()
#-----------------------------------------------------------------------------
    
def plot_dg_hist_inset(evnum,sim_file,DG_MIN=-30.0,DG_MAX=30.0,NUM_BINS=100):
    from pyvc import vcplots
    from matplotlib import pyplot as plt
    #******************************************
    #evnum = 109382
    #sim_file = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
    #*******************************************
    out_file      = 'local/dg_field_{}_hist_inset.png'.format(evnum)
    
    # For this vvv to work you must go to vcplots and make this method return the figure
    this_fig      = vcplots.plot_event_field(sim_file,evnum,output_file=out_file,
                        save_file_prefix='animation_test_g/field_values/'+str(evnum)+'_',
                        field_type='gravity')
    
    UNIT                = pow(10,-8) #microgals
    
    # Width and height are fixed
    ph = 768.0
    pw = 1024.0
    width_frac = 200.0/pw
    height_frac = 150.0/ph
    left_frac = 130.0/pw
    bottom_frac = 100.0/ph    
    
    event_field,mag     = get_dg_field(evnum,sim_file)
    dg                  = event_field.dG.flatten()/UNIT
    dg_binned,counts    = hist_1d(dg,bmin=DG_MIN,bmax=DG_MAX,num_bins=NUM_BINS,norm=True)
    
    LABEL   = r'$M={}$'.format(str(round(mag,1)))
    
    hist_inset = this_fig.add_axes((left_frac,bottom_frac,width_frac,height_frac))
    
    hist_inset.plot(dg_binned,counts,color='k')
    hist_inset.tick_params(axis='y',bottom='off',top='off',left='off',right='off',
                labelbottom='off',labeltop='off',labelleft='off',labelright='off')
    hist_inset.tick_params(axis='x', labelsize='small')
    #hist_inset.tick_params(axis='x',top='off',bottom='off')
    
    #  Make first and last ticks be <MIN and >MAX
    #tick_labels = [item.get_text() for item in hist_inset.get_xticklabels()]
    #tick_labels[0] = '<'+tick_labels[0]
    #tick_labels[-1] = '>'+tick_labels[-1]
    #hist_inset.set_xticklabels(tick_labels)
        
    #hist_inset.legend(loc=2,frameon=False,numpoints=1,handlelength=0,handletextpad=0)
    hist_inset.patch.set_alpha(0.0)
    
    this_fig.savefig(out_file,dpi=200)
    plt.clf()

def plot_number_area_data(sim_file, output_file=None, event_range=None):
    from pyvc import *
    from pyvc import vcplotutils
    
    #Can't handle plot label if no event_range given
    
    with VCSimData() as sim_data:
        # open the simulation data file
        sim_data.open_file(sim_file)
        
        # instantiate the vc events class passing in an instance of the
        # VCSimData class
        events = VCEvents(sim_data)
        
        # get the data
        event_data = events.get_event_data(['event_number','event_area'], event_range=event_range)
        
   
    start,end = event_range['filter']
    duration  = round(end-start)
    
    #---------------------------------------------------------------------------
    # Prepare the plot and do it.
    #---------------------------------------------------------------------------  
    # initilize a dict to store the event counts and get the total number
    # of events.
    cum_num = {}
    total_events   = len(event_data['event_number']) 
        
    for num in range(total_events):
        area = float(sorted(event_data['event_area'])[num])*float(pow(10,-6))
        cum_num[area] = total_events - (num + 1)

    sys.stdout.write("\nnumber of events  : {}\n".format(total_events))
    
    # dump the counts into x and y arrays for plotting. also, divide the count
    # by the number of years so we get count per year.
    x = []
    y = []
    for area in sorted(iter(cum_num)):
        x.append(float(area))
        y.append(float(cum_num[area]))
        
    # create the line for b = 1
    x_b1 = np.linspace(min(x),max(x),num=1000)
    y_b1 = y[0]*x_b1[0]*(np.array(x_b1)**-1)
    #sys.stdout.write(str(y_b1))
       
    plt.title('Duration: {} years    Total events: {}'.format(duration,total_events))
       
    plt.plot(x_b1,y_b1,label='b=1',ls='-',lw=2,c='r')  
    plt.plot(x,y,'.',c='k')
    plt.legend(loc='upper right')  
    plt.ylabel(r'$N (\geq A_r)$')
    plt.xlabel(r'$A_r [km^2]$')
    plt.xlim(-500,5500)
    plt.ylim(-20,750)
    plt.savefig(output_file,dpi=200)
       
    # do the standard plot
    """vcplotutils.standard_plot(output_file, x, y,
        axis_format='plot',
        add_lines=[{'label':'b=1', 'x':x_b1, 'y':y_b1}],
        axis_labels = {'y':'N', 'x':'rupture area [km^2]'},
        connect_points=True,
        legend_loc='upper right',
        plot_label = '      Duration: {} years   Total events: {}'.format(duration,total_events),
    )
    """

def make_frequency_area_plot(sim_file,center_evnum,duration,output_file=None):

    event_range = {'type':'year','filter':(500,700)}

    plot_number_area_data(sim_file, output_file=output_file, event_range=event_range)    

def plot_global_freq_mag(output_file="../Desktop/Dropbox/UCD/Stat_Mech_219B/global_freq_mag.png"):
	from scipy import optimize
	
	plt.clf()
    
    #Can't handle plot label if no event_range given
    
	anss_cat 		= '../Desktop/Dropbox/UCD/Stat_Mech_219B/ANSS_global_1990_2010.txt'
	cum_num 	= {}
	mags = []

	with open(anss_cat) as f:
		for numline,line in enumerate(f):
			if numline > 8:
				mags.append(float(line.split()[5]))

	total_events = len(mags)

	for num,mag in enumerate(sorted(mags)):
		cum_num[mag] = total_events - (num + 1)

	#sys.stdout.write("\nnumber of events  : {}\n".format(total_events))
    
    # dump the counts into x and y arrays for plotting. also, divide the count
    # by the number of years so we get count per year.
	x = []
	y = []
	for mag in sorted(iter(cum_num)):
		x.append(float(mag))
		y.append(float(cum_num[mag]))
        
	x_av,y_av = bin_2d(x,y,bmin=5.5,bmax=7.5)

	#Fitting to gutenberg richter
	fitfunc = lambda p, m: p[0] - p[1]*m # Target function
	errfunc = lambda p, m, y: fitfunc(p,m) - y # Distance to the target function
	p0 = [9.6, 1.0] # Initial guess for the parameters
	p1, success = optimize.leastsq(errfunc, p0[:], args=(x_av,np.log10( y_av)))

	a_fit, b_fit = p1[0],p1[1]

    # create the best fit line
	x_fit = np.linspace(min(x),max(x),num=10)
	y_fit = 10**(a_fit)*10**(-b_fit*x_fit)
       
	plt.title('     1990-2010')
       
	fit_label = 'a = %.3f, b=-%.3f'%(a_fit,b_fit)

	plt.plot(x_fit,y_fit,label=fit_label,ls='-',lw=3,c='grey')  
	plt.semilogy(x,y,'.',c='k')
	plt.xlabel('magnitude, m')
	plt.ylabel(r'N ($\geq$ m)')
	plt.legend(loc='upper right') 
	#plt.autoscale(tight=False)
	plt.savefig(output_file,dpi=200)
	
	
def plot_freq_mag(sim_file='ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'):
	from pyvc import vcsimdata,vcevents
	from scipy import optimize
	
	outfile = '../Dropbox/UCD/Stat_Mech_219B/vc_gr_ensemble.png'
	
	plt.clf()

    # for the UCERF2 error bars
	x_UCERF = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5]
	y_UCERF = [4.73, 2.15, 0.71, 0.24, 0.074, 0.020]
	y_error_UCERF = [[1.2, 0.37, 0.22, 0.09, 0.04, 0.016],[1.50, 0.43, 0.28, 0.11, 0.06, 0.035]]
	
	years = [(0,200),(3100,3300),(6200,6400),(8500,8700),(11500,11700),
				(15600,15800),(17700,17900),(20800,21000),(22700,22900),
				(24800,25000),(27000,27200),(29000,29200),(31000,31200),
				(33000,33200),(37000,37200),(40000,40200),(42000,42200),
				(43500,43700),(46300,46500),(48800,49000)]
	
	with vcsimdata.VCSimData() as sim_data:
        # open the simulation data file
		sim_data.open_file(sim_file)
        
        # instantiate the vc events class passing in an instance of the
        # VCSimData class
		events = vcevents.VCEvents(sim_data)
		all_mags = []
		total_duration = 0.0
        
		for year_pair in years:
			start,end = year_pair
        	
			event_range={'type':'year','filter':(start,end)}
        
        	# get the data
			event_data     = events.get_event_data(['event_magnitude', 'event_range_duration'], event_range=event_range)
			these_mags     = event_data['event_magnitude']
			total_duration+= event_data['event_range_duration']
        	
			for mag in these_mags:
				all_mags.append(mag)
    
    
    # initilize a dict to store the event counts and get the total number
    # of events.
	cum_freq = {}
	total_events = len(all_mags)
    
    # count the number of events bigger than each magnitude
	for num, magnitude in enumerate(sorted(all_mags)):
		cum_freq[magnitude] = total_events - (num + 1)
    
    # dump the counts into x and y arrays for plotting. also, divide the total duration 
    # to get an ensemble average of EQs per year
	x = []
	y = []
	for magnitude in sorted(cum_freq.iterkeys()):
		x.append(magnitude)
		y.append(float(cum_freq[magnitude])/total_duration)

	# Fit data to GR relation
	x_av,y_av = bin_2d(x,y,bmin=4.5,bmax=7.5)

	#Fitting to gutenberg richter
	fitfunc = lambda p, m: p[0] - p[1]*m # Target function
	errfunc = lambda p, m, y: fitfunc(p,m) - y # Distance to the target function
	p0 = [y_UCERF[0]*1.5, 1.0] # Initial guess for the parameters
	p1, success = optimize.leastsq(errfunc, p0[:], args=(x_av,np.log10( y_av)))

	a_fit, b_fit = p1[0],p1[1]

    # create the best fit line
	x_fit = np.linspace(min(x),max(x),num=10)
	y_fit = 10**(a_fit)*10**(-b_fit*x_fit)
    
	fit_label = 'a = %.3f, b=-%.3f'%(a_fit,b_fit)
    
	plt.semilogy(x,y,c='k',ls='dotted')
	plt.errorbar(x_UCERF,y_UCERF,yerr=y_error_UCERF,c='r',ls='--',label="UCERF2")
	plt.semilogy(x_fit,y_fit,label=fit_label)
    
	plt.legend(loc='upper right')
	plt.xlabel('magnitude, m')
	plt.ylabel(r'N ($\geq$ m)')
	
	plt.savefig(outfile,dpi=200)


"""
evnum    = 109382
duration = 100
sim_file = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
make_frequency_area_plot(sim_file,evnum,duration,output_file='test_number_area.png')
"""


#=============================================================================
#evnum = 109382
#sim_file = 'ALLCAL2_1-7-11_no-creep_dyn-05_st-20.h5'
#DG_MIN,DG_MAX = -30.0,30.0
#NBIN          = 100
#binner = np.linspace(DG_MIN,DG_MAX,NBIN)
#plot_dg_hist(evnum,sim_file,BINS=binner)
#=============================================================================
#--DEPRECATED OR OLD----------------------------------------------------------
"""def plot_dg_hist(dg_flat,savename,Nbins=100):
    import numpy as np
    from matplotlib import pyplot as plt
    
    dg_hist,bin_edges     = np.histogram(dg_flat, bins=Nbins, density=True, normed=True)
    
    x = np.linspace(bin_edges[0],bin_edges[-1],len(dg_hist))
    plt.clf()
    plt.figure()
    
    plt.plot(x,dg_hist,color='g')
    
    plt.savefig(savename,dpi=200)
    plt.clf()
"""      
#=============================================================================
"""
def plot_dg(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
            c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=False,save=False,DIFF=False):
    
    
    if DIFF:
        filename    = get_filename(c,dip,L,W,US,UD,UT,'diff_plots',pre='dg-dg2')
        XX,YY,DG    = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU)
        XX,YY,DG2   = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=True)
        DG          = DG - DG2   
        FMT         = '%.2f'    
    else:
        CLIM,CMAX   = -400,400
        FMT         = '%i'
        if DG2:
            filename = get_filename(c,dip,L,W,US,UD,UT,'dg2_plots')
            XX,YY,DG = get_dg2_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU)
        else:       
            filename = get_filename(c,dip,L,W,US,UD,UT,'dg_plots')
            XX,YY,DG = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU)
   

    # Put gravity change in micro-gals
    UNIT = pow(10,-8)
    DG /= float(UNIT)

    # Make the figure    
    this_fig    = plt.figure()
    these_axes  = plt.subplot(111)
    
    # Plot stuff   
    BlueRed = plt.get_cmap('RdBu_r')    
    DGplot  = plt.imshow(DG, origin = 'lower',interpolation='nearest',
                         extent=[Xmin/1000.0,Xmax/1000.0,Ymin/1000.0,
                                 Ymax/1000.0],cmap=BlueRed)

    dg_ax   = this_fig.gca()
    dg_ax.set_xlabel('X [km]',labelpad=-2)
    dg_ax.set_ylabel('Y [km]',labelpad=-5)        
    
    # Put color bar below x-axis
    divider     = make_axes_locatable(these_axes)
    cbar_axis   = divider.append_axes("top", size="5%",pad=0.02)                       
    cbar        = plt.colorbar(DGplot,format=FMT,
                               orientation='horizontal',cax=cbar_axis)
    if not DIFF:
        plt.clim(CLIM,CMAX)
    
    cbar_ax     = this_fig.gca()
    
    cbar_ax.set_xlabel(r'$\Delta$g [$\mu$gal]',labelpad=-42)
    cbar_ax.tick_params(axis='x',labelbottom='off',labeltop='on',
                        bottom='off',top='off',right='off',left='off',
                        labelsize='small',pad=-1)

    # Draw a projection of the fault
    W_proj      = W*np.cos(dip)
    fault_proj  = mpl.patches.Rectangle((0.0,0.0),L/1000.0,W_proj/1000.0,
                                        ec='k',fc='none',fill=False,
                                        ls='solid',lw=5.0)
    dg_ax.add_patch(fault_proj)
    
    # Save the plot
    if save:
        plt.savefig(filename,dpi=200)
        print '>>> plot saved: '+filename
    plt.show()
"""
#--DEPRECATED--------------------------------------------------------------
"""
def plot_dz(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DH=False,
            DIFF=False,save=False):
    UNIT        = pow(10,-2)

    BlueRed     = plt.get_cmap('RdBu_r')
    # Make the figure    
    this_fig    = plt.figure()
    these_axes  = plt.subplot(111)
    
    # Plotting difference between vert. displacement calculations
    if DIFF:
        XX,YY,H = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,
                                    UT,LAMBDA,MU,DH=True)
        XX,YY,Z = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,
                                    UT,LAMBDA,MU)
        Z       = Z-H
        filename= get_filename(c,dip,L,W,US,UD,UT,'diff_plots',pre='dz-dh')
        FMT     = '%.1f'
    else:
        FMT     = '%.1f'

        folder  = 'dz_plots'
        if DH:
            pre ='dh'
        else:
            pre ='dz'
        XX,YY,Z     = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,
                                    UT,LAMBDA,MU,DH=DH)
        filename    = get_filename(c,dip,L,W,US,UD,UT,'dz_plots',pre=pre)


    this_plot   = plt.imshow(Z/UNIT, origin = 'lower', extent=[Xmin,Xmax,Ymin,Ymax],
                             cmap=BlueRed)

    # Adjust plot axis labels
    dz_ax   = this_fig.gca()
    dz_ax.set_xlabel('X [km]',labelpad=-2)
    dz_ax.set_ylabel('Y [km]',labelpad=-5)        
    
    # Put color bar below x-axis
    divider     = make_axes_locatable(dz_ax)
    cbar_axis   = divider.append_axes("top", size="5%",pad=0.02)                      
    cbar        = plt.colorbar(this_plot,format=FMT,
                               orientation='horizontal',cax=cbar_axis)
    cbar_ax     = this_fig.gca()

    # Colorbar labeling    
    cbar_ax.set_xlabel(r'$\Delta$z [$cm$]',labelpad=-42)
    cbar_ax.tick_params(axis='x',labelbottom='off',labeltop='on',
                        bottom='off',top='off',right='off',left='off',
                        labelsize='small',pad=-1)
    
    # Draw a projection of the fault
    W_proj      = W*np.cos(dip)
    fault_proj  = mpl.patches.Rectangle((0.0,0.0),L/1000.0,W_proj/1000.0,
                                        ec='k',fc='none',fill=False,
                                        ls='solid',lw=5.0)
    these_axes.add_patch(fault_proj)
    
    # Save the beautiful plot
    if save:
        plt.savefig(filename,dpi=200)
        print '>>> plot saved: '+filename
    plt.show()
"""
#--DEPRECATED--------------------------------------------------------------
"""def get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep):
    X       = np.arange(Xmin,Xmax,Xstep,dtype=np.dtype('d'))
    Y       = np.arange(Ymin,Ymax,Ystep,dtype=np.dtype('d'))
    return X,Y
"""
#--DEPRECATED--------------------------------------------------------------
"""def plot_dz_dh_diff(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    
    my_cmap = mpl.cm.get_cmap('rainbow')
    my_cmap.set_under('w')
    
    XX,YY,DZ   = get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DH = get_dh_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    
    this_plot  = plt.imshow(DZ-DH,origin='lower',extent=[Xmin,Xmax,Ymin,Ymax], cmap=my_cmap,interpolation='none')
    
    res = round((Xmax-Xmin)/float(Nx))
    
    plt.colorbar(this_plot,format='%.3f')
    filename = './test_dg_dz_diff_plot_'+str(int(res))+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
"""
#--DEPRECATED--------------------------------------------------------------
"""
def plot_dg_dg2_diff(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    
    my_cmap = mpl.cm.get_cmap('rainbow')
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
"""
#--DEPRECATED--------------------------------------------------------------
"""
def get_dz_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DH=False):
    
    okada   = quakelib.Okada() 
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    Z       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            loc     = quakelib.Vec3(XX[i][j],YY[i][j],0.0)
            if DH:
                Z[i][j] = okada.calc_dH(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
            else:
                Z[i][j] = okada.calc_displacement_vector(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)[2]
            del loc
    
    return (XX,YY,Z)
"""
#--DEPRECATED--------------------------------------------------------------
"""
#-----------------------------------------------------------------------------

def get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=False):
    
    okada   = quakelib.Okada()
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    DG      = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            loc   = quakelib.Vec2(XX[i][j],YY[i][j])
            if DG2:
                DG[i][j] = okada.calc_dg2(loc,dip,c,L,W,US,UD,UT,LAMBDA,MU)
            else:
                DG[i][j] = okada.calc_dg(loc,dip,c,L,W,US,UD,UT,LAMBDA,MU)
            del loc 
    
    return (XX,YY,DG)
"""












