import numpy as np
import matplotlib.pyplot as plt
#=============================================================================
#Trying to replicate plot in Okubo '92
_C      = 1000.0   #meters
_DIP    = np.pi/2.0
_L      = 10000.0
_W      = 10000.0
_US     = 5.0
_UD     = 0.0
_UT     = 0.0
_LAMBDA = 1.0
_MU     = 1.0

_Xmin,_Xmax = -5000.0,15000.0
_Xstep      = 100.0
_Ymin,_Ymax = -10000.0,10000.0
_Ystep      = 100.0


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
def get_dz_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib
    
    okada   = quakelib.Okada() 
    X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)

    XX,YY   = np.meshgrid(X,Y)
    Z       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            loc     = quakelib.Vec3(XX[i][j],YY[i][j],0.0)
            Z[i][j] = okada.calc_displacement_vector(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)[2]
            #Z[i][j] = get_displacement(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)[2]
    
    return (XX,YY,Z)
#-----------------------------------------------------------------------------
def get_dh_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY   = np.meshgrid(X,Y)
    H       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            H[i][j] = okada.dH(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,H)
#-----------------------------------------------------------------------------
def get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY   = np.meshgrid(X,Y)
    DG      = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            DG[i][j] = okada.dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU) 
            #DG[i][j] = get_dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,DG)
#-----------------------------------------------------------------------------
def get_dg2_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib    
    
    okada   = quakelib.Okada()
    X,Y     = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY   = np.meshgrid(X,Y)
    DG2     = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            DG2[i][j] = okada.dg2(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU) 
            #DG[i][j] = get_dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,DG2)
#-----------------------------------------------------------------------------
def plot_dz(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    from scipy.interpolate import griddata
    import sys    

    #X,Y = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY,Z = get_dz_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)

    #V = [-.01,-.005,-.0025,0,.0025,.005,.01]
    #N=8

    DZplot = plt.imshow(Z, origin = 'lower', extent=[Xmin,Xmax,Ymin,Ymax])

    #plt.contourf(X,Y,Z,N,origin='lower',extent=(Xmin,Xmax,Ymin,Ymax))

    plt.colorbar()  
    filename = './test_dz_plot_'+str(_Xstep)+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def plot_dg(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):

    XX,YY,DG = get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
  
    #plt.contour(XX,YY,DG,LEVELS)

    UNIT = pow(10,-8)
    #FMT = {}
    #for level in LEVELS:
    #    FMT[level] = str(float(level)/float(UNIT))
    #DGplot = plt.contour(XX,YY,DG,LEVELS)

    plt.figure()
     
    DGplot = plt.imshow(DG, origin = 'lower', extent=[Xmin,Xmax,Ymin,Ymax])
    
    #For colormesh, XX,YY are bounds and DG is the value *inside* the bounds, to remove the last value of DG
    #DG          = DG[:-1,:-1]
    #plt.pcolor(XX,YY,DG)
    #plt.axis([XX.min(),XX.max(),YY.min(),YY.max()])
    
    
    #plt.clabel(DGplot, inline=1, fontsize=10,fmt=FMT)
    #plt.grid(True)

    plt.colorbar()
    filename = './test_dg_plot_'+str(_Xstep)+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def plot_dz_dh_diff(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import matplotlib
    
    my_cmap = matplotlib.cm.get_cmap('rainbow')
    my_cmap.set_under('w')
    
    XX,YY,DZ   = get_dz_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DH = get_dh_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    
    this_plot  = plt.imshow(DZ-DH,origin='lower',extent=[Xmin,Xmax,Ymin,Ymax], cmap=my_cmap,interpolation='none')
    
    plt.colorbar(this_plot,format='%.3f')
    filename = './test_dg_dz_diff_plot_'+str(_Xstep)+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------
def plot_dg_dg2_diff(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import matplotlib
    
    my_cmap = matplotlib.cm.get_cmap('rainbow')
    my_cmap.set_under('w')
    
    XX,YY,DG    = get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    dum,dum,DG2 = get_dg2_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    del(dum)
    
    this_plot  = plt.imshow(DG-DG2,origin='lower',extent=[Xmin,Xmax,Ymin,Ymax], cmap=my_cmap,interpolation='none')
    
    plt.colorbar(this_plot,format='%.3f')
    filename = './test_dg_dg2_diff_plot_'+str(_Xstep)+'m.png'
    plt.savefig(filename,dpi=200)
    plt.show()
#-----------------------------------------------------------------------------

#plot_dg(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
#plot_dz(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
plot_dz_dh_diff(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)
#plot_dg_dg2_diff(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)













