import numpy as np
import matplotlib.pyplot as plt
#=============================================================================
#Trying to replicate plot in Okubo '92
_C      = 500   #meters
_DIP    = np.pi/2.0
_L      = 500000
_W      = 300000
_US     = 10
_UD     = 0
_UT     = 0
_LAMBDA = 1
_MU     = 1

_Xmin,_Xmax = -500000,1000000
_Xstep      = 1000
_Ymin,_Ymax = -750000,750000
_Ystep      = 1000


#-----------------------------------------------------------------------------
def get_dz(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib

    okada = quakelib.Okada()
    loc   = quakelib.Vec3(x,y,0.0)

    d,d,dz = okada.calc_displacement_vector(loc,c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return dz
#-----------------------------------------------------------------------------
def get_dg(x,y,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    import quakelib

    okada = quakelib.Okada()
    loc   = quakelib.Vec3(x,y,0.0)

    return okada.dg(x,y,c,L,W,US,UD,UT)
#-----------------------------------------------------------------------------
def get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep):
    X       = np.arange(Xmin,Xmax,Xstep,dtype=np.dtype('d'))
    Y       = np.arange(Ymin,Ymax,Ystep,dtype=np.dtype('d'))
    return X,Y
#-----------------------------------------------------------------------------
def get_dz_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):

    X,Y = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)

    XX,YY   = np.meshgrid(X,Y)
    Z       = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            Z[i][j] = get_dz(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,Z)
#-----------------------------------------------------------------------------
def get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):

    X,Y = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)

    XX,YY   = np.meshgrid(X,Y)
    DG      = np.zeros(XX.shape)

    for i in range(len(XX[0])):
        for j in range(len(XX[1])):
            DG[i][j] = get_dg(XX[i][j],YY[i][j],c,dip,L,W,US,UD,UT,LAMBDA,MU)
    
    return (XX,YY,DG)
#-----------------------------------------------------------------------------
def plot_dz(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):
    from scipy.interpolate import griddata
    import sys    

    X,Y = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY,Z = get_dz_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)

    #V = [-.01,-.005,-.0025,0,.0025,.005,.01]
    N=8

    plt.contourf(X,Y,Z,N,origin='lower',extent=(Xmin,Xmax,Ymin,Ymax))

    plt.colorbar()  
    plt.savefig('./test_dz_plot.png',dpi=100)
    plt.show()
    return 0
#-----------------------------------------------------------------------------
def plot_dg(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU):

    X,Y      = get_arrays(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep)
    XX,YY,DG = get_dg_matrix(Xmin,Xmax,Xstep,Ymin,Ymax,Ystep,c,dip,L,W,US,UD,UT,LAMBDA,MU)

    V = [-.00000050,-.00000040,-.00000030,-.00000020,-.0000001,0,.0000001,.0000002,.0000003,.0000004,.0000005]

    plt.contourf(X,Y,DG,V,origin='lower',extent=(Xmin,Xmax,Ymin,Ymax))

    plt.colorbar()
    plt.savefig('./test_dg_plot.png',dpi=100)
    plt.show()
    return 0
#-----------------------------------------------------------------------------

#plot_dz(_Xmin,_Xmax,_Xstep,_Ymin,_Ymax,_Ystep,_C,_DIP,_L,_W,_US,_UD,_UT,_LAMBDA,_MU)















