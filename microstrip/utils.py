import numpy as np

c = 299792458       # Speed of light            [m/s]
eta0 = 120*np.pi       # 

def width(Z0, er, h):
        # For W/h < 2
        A = Z0/60 * np.sqrt((er + 1)/2) + (er - 1)/(er + 1) * (0.23 + 0.11/er)
        W_A = (8*np.exp(A))/(np.exp(2*A) - 2) * h
        
        if W_A/h < 2:
            return W_A
        
        # For W/h > 2
        B = (eta0*np.pi) / (2*Z0*np.sqrt(er))
        W_B = 2/np.pi * (B - 1 - np.log(2*B - 1) + (er - 1)/(2*er) * (np.log(B - 1) + 0.39 - 0.61/er)) * h 
    
        if W_B/h > 2:
            return W_B
        

# Calculate effective width (W_eff = W + dW), due to copper thickness
def effectiveWidth(w, h, t):
    if t == 0:
        return w

    if t>h:
        raise ValueError("Violation of effective width, t>h")
    if t>w/2:
        raise ValueError("Violation of effective width, t>W/2")
        
    if w/h < 1/(2*np.pi):
        return (w/h + t/(np.pi*h) * (1 + np.log((4*np.pi*w)/t)))*h
    else:
        return (w/h + t/(np.pi*h) * (1 + np.log((2*h)/t)))*h
    

# Calculate effective permittivity
def effectivePermittivity(er, w, h) -> float:
    if w/h <= 1:
        return (er + 1)/2 + (er - 1)/2 * (np.power(1 + 12*h/w, -0.5) + 0.04*(1 - w/h)**2)
    else:
        return (er + 1)/2 + (er - 1)/2 *  np.power(1 + 12*h/w, -0.5)
    

# Calculate effective charataristic impedance (non-closed form)
def impedance(er, w, h):

    er_eff = effectivePermittivity(er,w,h)

    if w/h < 1:
        return 60/np.sqrt(er_eff) * np.log(8 * h/w + 0.25*w/h)
    else:
        return (eta0 / np.sqrt(er_eff)) / (w/h + 1.393 + 0.667*np.log(w/h + 1.444))


# Calculate wavelength in substrate (Gonzalez 2.5.9 & 2.5.8)
def microstripWavelength(lambda_0, er, w, h):
    if w/h < 0.6:
        return lambda_0/np.sqrt(er) * np.power(er/(1+0.6*(er-1)*(w/h)**0.0297),0.5)
    else:
        return lambda_0/np.sqrt(er) * np.power(er/(1+0.63*(er-1)*(w/h)**0.1255),0.5)

def msLength(theta, lambda_s):
    return theta/360 * lambda_s

def electricalLength(L, lambda_s):
        if L == 0:
            return 0
        else:
            return (360*np.abs(L)) / lambda_s


    
def mitred(W, h):
# https://www.everythingrf.com/rf-calculators/microstrip-mitred-bend-calculator

    D = W * np.sqrt(2)
    X = W*np.sqrt(2)*(0.52+0.65*np.exp(-1.35*W/h))

    M = X/D                         # Constant for ADS

    A = X*np.sqrt(2) - W    

    a = (W+A)/2
    diagonal = np.sqrt(2*a**2)      # Added path length
    return M, diagonal


# Simulate

# def Zin(MLIN, ZL, f):
#     w = MLIN.getW()    
#     L = MLIN.getL()
#     sub = MLIN.getSubstrate()

#     Zin_values = []  # Initialize a list to store Zin for each frequency
    
#     if isinstance(f, list):
#         for i in range(len(f)):
#             Z0, theta = analyze(f[i], w, L, sub, True, False)
#             t = np.tan(np.radians(theta))
#             Zin = Z0 * (ZL + 1j * Z0 * t) / (Z0 + 1j * ZL * t)
            
#             Zin_values.append(Zin)  # Store the result for each frequency

#             return Zin_values
#     else:
#         Z0, theta = analyze(f, w, L, sub, True, False)
#         t = np.tan(np.radians(theta))
#         Zin = Z0 * (ZL + 1j * Z0 * t) / (Z0 + 1j * ZL * t)
        
#         return Zin
