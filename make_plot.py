import test_plot
reload(test_plot)
import numpy as np
#=============================================================================
#        DATA
DTTF        = 1000.0   # depth to top of fault (Okubo's style)
_DIP        = np.pi/2.0
_L          = 10000.0
_W          = 10000.0
_C          = DTTF + _W*np.sin(_DIP)   #meters
_US         = 5.0
_UD         = 0.0
_UT         = 0.0
_LAMBDA     = 1.0
_MU         = 1.0
_Xmin,_Xmax = -5000.0,15000.0  ### Xrange and Yrange must be same
_Nx         = 500.0
_Ymin,_Ymax = -10000.0,10000.0
_Ny         = 500.0

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
#*******************
#=============================================================================

test_plot.cbar_plot(_Xmin,_Xmax,_Nx,_Ymin,_Ymax,_Ny,_C,_DIP,_L,_W,_US,_UD,_UT,
               _LAMBDA,_MU,save=SAVE,DG2=_DG2,DG=_DG,DZ=_DZ,
               DH=_DH,DIFFZ=_DIFFZ,DIFFG=_DIFFG,CLIMITS=_CLIMITS)