import sys
sys.path.append("/home/kasey/PyVC/")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import quakelib
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable

#=============================================================================
def bin_2d(x,y) :

    if np.shape(x) != np.shape(y):
        raise NameError('Array shape mismatch, insert coin(s) to continue.')

    num_bins = math.floor(len(x)/100.0)
    
    if num_bins <= 20:
        num_bins = 20
    elif num_bins >= 100:
        num_bins = 100
    
    
    x       = np.array(x)
    y       = np.array(y)
    bin_min = math.floor(np.min(x))
    bin_max = math.ceil(np.max(x))
    bins    = np.linspace(bin_min,bin_max,num=num_bins) 
    inds    = np.digitize(x, bins)
    x_ave   = []
    y_ave   = []
    binned_data = {}

    for n, iBin in enumerate(inds):
        try:
            binned_data[iBin].append(y[n])
        except KeyError:
            binned_data[iBin] = [y[n]]

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
def get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny):
    x   = np.linspace(Xmin,Xmax,num=Nx)
    y   = np.linspace(Ymin,Ymax,num=Ny)
    return x,y

#-----------------------------------------------------------------------------
def get_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,
               DG=False,DH=False,DZ=False,DG2=False):
    
    okada   = quakelib.Okada() 
    X,Y     = get_linspaces(Xmin,Xmax,Nx,Ymin,Ymax,Ny)
    XX,YY   = np.meshgrid(X,Y)
    MAT     = np.zeros(XX.shape)

    if DG:
        for i in range(len(XX[0])):
            for j in range(len(XX[1])):
                loc       = quakelib.Vec2(XX[i][j],YY[i][j])
                MAT[i][j] = okada.calc_dg(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
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
              HIST=False):
    """
    Immutable constants: (hard coded in quakelib/src/QuakeLibOkada.cpp) all MKS
        Free-air gravity gradient (Okubo '92):   Beta = 0.00000309 1/s^2
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
            CLIM,CMAX   = -60,60
        else:
            CLIM,CMAX   = -300,300
            
        #CLABEL      = r'gravity changes $[\mu gal]$'
    else:
         #        Plot either DZ or DH
        pre                 = ('dh' if DH else 'dz')
        filename,fault_type = get_filename(c,dip,L,W,US,UD,UT,'dz_plots',
                                           pre=pre,suff=SUFFIX)        
        XX,YY,Data  = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,
                                 c,dip,L,W,US,UD,UT,LAMBDA,MU,DH=DH)
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
    img_ax.set_xlabel(r'along fault [$km$]',labelpad=-1)
    img_ax.set_ylabel(r'[$km$]',labelpad=-5)
    
    forced_ticks  = [int(num) for num in np.linspace(CLIM,CMAX,11)]
    
    # Make color bar and put its label below its x-axis
    divider       = make_axes_locatable(fig_axes)
    cbar_ax       = divider.append_axes("top", size="5%",pad=0.02)                       
    cbar          = plt.colorbar(this_img,format=FMT,
                               orientation='horizontal',cax=cbar_ax,
                               ticks=forced_ticks)
    if CLIMITS:
        plt.clim(CLIM,CMAX)
    
    # Make and position colorbar label
    #cbar_ax.set_xlabel(CLABEL,labelpad=-46)
    cbar_ax.tick_params(axis='x',labelbottom='off',labeltop='on',
                        bottom='off',top='off',right='off',left='off',
                        pad=-1)
    
    
    # Want to change outermost tick labels on colorbar
    #   from 'VALUE','-VALUE' to '>VALUE' and '<-VALUE'    
    cb_tick_labs = [str(num) for num in forced_ticks]
    cb_tick_labs[0] = '<'+cb_tick_labs[0]
    cb_tick_labs[-1] = '>'+cb_tick_labs[-1]
    cbar.ax.set_xticklabels(cb_tick_labs)
      
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
        
    plt.clf()
#----------------------------------------------------------------------------- 
    

def plot_dg_hist(dg_flat,savename,Nbins=100):
    import numpy as np
    from matplotlib import pyplot as plt
    
    dg_hist,bin_edges     = np.histogram(dg_flat, bins=Nbins, density=True, normed=True)
    
    x = np.linspace(bin_edges[0],bin_edges[-1],len(dg_hist))
    plt.clf()
    plt.figure()
    
    plt.plot(x,dg_hist,color='g')
    
    plt.savefig(savename,dpi=200)
    plt.clf()
            
#-----------------------------------------------------------------------------
def plot_dg_vs_uz(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,returns=False):
    from pyvc import vcplots
    import os
    
    # Need to remove a cached file for Arial fonts to be used
    if os.path.exists('/home/kasey/.matplotlib/fontList.cache'):
        os.remove('/home/kasey/.matplotlib/fontList.cache')
        
    UNIT        = float(pow(10,-8))  # 1 microgal in mks units is 10^(-8) m/s^2
    
    XX,YY,DG    = get_dg_matrix(Xmin,Xmax,Nx,Ymin,Ymax,Ny,c,dip,L,W,US,UD,UT,LAMBDA,MU,DG2=True)
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
        
    dip_deg     = round(dip*180.0/np.pi)

    res = (Xmax-Xmin)/float(Nx)

    output_file = "/home/kasey/Okubo-test/dg2_vs_uz_"+fault_type+"_c%ikm_L%ikm_W%ikm_dip%i_%im.png"%(c/1000.0,L/1000.0,W/1000.0,dip_deg,res)
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


#=============================================================================
#=============================================================================
#--DEPRECATED OR OLD----------------------------------------------------------
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












