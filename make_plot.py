import test_plot
reload(test_plot)
import numpy as np
#=============================================================================
#        DATA
DTTF        = [1000.0,1000.0,1000.0]   # depth to top of fault (Okubo's style)
_DIP        = [np.pi/2.0,np.pi/3.0,np.pi/6.0]
_L          = [10000.0,10000.0,10000.0]
_W          = [10000.0,10000.0,10000.0]
_C          = [DTTF[i] + _W[i]*np.sin(_DIP[i]) for i in range(len(_L))]   #meters
_US         = [5.0,0.0,0.0]
_UD         = [0.0,-5.0,5.0]
_UT         = [0.0,0.0,0.0]
_LAMBDA     = 1.0
_MU         = 1.0
#_Xmin,_Xmax = -0.5*_L,1.5*_L  ### Xrange and Yrange must be same
_Xmin,_Xmax = [-10000.0,-10000.0,-10000.0],[20000.0,20000.0,20000.0]
_Nx         = 100.0
#_Ymin,_Ymax = -_W,2*_W
_Ymin,_Ymax = [-15000.0,-10000.0,-10000.0],[15000.0,20000.0,20000.0]
_Ny         = 100.0

##        SWITCHES
#*******************
SAVE         = True
_DG          = True
_DG2         = False
_DZ          = False
_DH          = False
_DIFFG       = False
_DIFFZ       = False
_CLIMITS     = True
_suffix      = 'proposal'
_HIST        = True
#*******************
test_plot.plot_dg_vs_uz_simple(_Xmin[0],_Xmax[0],_Nx,_Ymin[0],_Ymax[0],_Ny,_C[0],_DIP[0],_L[0],_W[0],_US[0],_UD[0],_UT[0],_LAMBDA,_MU)


#=============================================================================
"""for k in range(len(_L)):
    test_plot.cbar_plot(_Xmin[k],_Xmax[k],_Nx,_Ymin[k],_Ymax[k],_Ny,_C[k],
                        _DIP[k],_L[k],_W[k],_US[k],_UD[k],_UT[k],
                        _LAMBDA,_MU,save=SAVE,DG2=_DG2,DG=_DG,DZ=_DZ,
                        DH=_DH,DIFFZ=_DIFFZ,DIFFG=_DIFFG,CLIMITS=_CLIMITS,
                        SUFFIX=_suffix,HIST=_HIST)
"""