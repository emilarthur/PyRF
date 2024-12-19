import numpy as np
import math

def binomial(N, Z0, ZL):
    """
    Calculate characteristic impedances for a binomial matching transformer with N sections.

    Parameters:
    - N: Number of sections
    - Z0: Source impedance
    - ZL: Load impedance

    Returns:
    - impedances: List of characteristic impedances for each section
    """    
   
    Z = []  # Start with source impedance
    c = []
    for n in range(1, N + 1):
        ci = math.factorial(N) / (math.factorial(N - n) * math.factorial(n))
        c.append(ci)
    c = np.flip(c)

    Z_new = Z0
    for i in range(1, N + 1):
        Z_old = Z_new
        Zi = np.exp(np.log(Z_old) + 2 ** (-N) * c[i-1] * np.log(ZL / Z0))
        Z_new = Zi
        Z.append(Z_new)

    # A = 2**(-N) * (ZL-Z0)/(ZL+Z0)

    return Z


