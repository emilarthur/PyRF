from microstrip.utils import *

def analyze(**kwargs):
    f = kwargs.get("f")
    mlin = kwargs.get("mlin", None)
    thickness = kwargs.get("thickness", True)
    disp = kwargs.get("disp", False)


    if mlin != None:
        w   = mlin.getW()
        L   = mlin.getL()

        er  = mlin.substrate.getEr()
        h   = mlin.substrate.getH()
        t   = mlin.substrate.getT()
        
    else:
        w   = kwargs.get("w")
        L   = kwargs.get("L")
        substrate = kwargs.get("substrate")

        er  = substrate.getEr()
        h   = substrate.getH()
        t   = substrate.getT()
    

    # Calculate constants
    lambda_0 = c/f                           # Free space wavelength         [m]
    
    w_eff = effectiveWidth(w, h, t)

    # Calculate impedance
    if t/h > 0.005 and thickness == True:
        Z0 = impedance(er, w_eff, h)
        lambda_s = microstripWavelength(lambda_0, er, w_eff, h)
    else:
        Z0 = impedance(er, w, h)
        lambda_s = microstripWavelength(lambda_0, er, w, h)
    
    # Calculate Electrical Length
    theta = electricalLength(L, lambda_s)

    if disp == True:
        print(f"Impedance:...................{Z0:.2f} Ohm")
        print(f"Electrical Length:...........{theta:.2f} deg")


    return Z0, theta