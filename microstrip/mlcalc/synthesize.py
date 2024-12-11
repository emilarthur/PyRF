from microstrip.utils import *
from microstrip.mlcalc.analyze import *

def synthesize(**kwargs):
    Z0 = kwargs.get("Z0")
    f = kwargs.get("f")
    substrate = kwargs.get("substrate")
    theta = kwargs.get("theta")
    thickness = kwargs.get("thcikness", True)
    disp = kwargs.get("disp", False)

    # Validate required parameters
    if Z0 is None or Z0 <= 0:
        raise ValueError("Characteristic impedance 'Z0' must be positive.")
        
    if f is None or f <= 0:
        raise ValueError("Frequency 'f' must be greater than 0.")
        
    if theta is None or theta < 0:
        raise ValueError("Electrical length 'theta' must be greater than 0.")

    er = substrate.getEr()
    h  = substrate.getH()
    t  = substrate.getT()


# Calculate constants
    lambda_0 = c / f  # Free space wavelength [m]

    # Synthesize Width and Length from closed-form equations
    w = width(Z0, er, h)
    lambda_s = microstripWavelength(lambda_0, er, w, h)
    L = msLength(theta, lambda_s)

    # Iteratively refine width to match Z0
    step = 0.01e-6
    while True:
        z0, _ = analyze(w=w, L=L, f=f, substrate=substrate)
        if abs(z0 - Z0) <= 0.001:
            break
        w += step if z0 > Z0 else -step

    # Iteratively refine length to match theta
    while True:
        _, theta_analyzed = analyze(w=w, L=L, f=f, substrate=substrate)
        if abs(theta_analyzed - theta) <= 0.001:
            break
        L += step if theta_analyzed < theta else -step

    # Display results if requested
    if disp:
        print(f"Width:.......................{w * 1e3:.3f} mm")
        print(f"Length:......................{L * 1e3:.3f} mm")

    return w, L
        