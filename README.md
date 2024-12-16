
# PyRF

This script can analyze and synthesize microstrip parameters based on Guillermo Gonzalez book "Microwave Transistor Amplifiers 2nd Edition" chapter 2.5.

Note that losses (α) are not accounted for.

```py
from microstrip import *
from microstrip.mlcalc import *
```

## Microstrip
Calculating characteristic impedance of a microstrip line

For $W/h\leq1$:

$$
Z_0=\frac{60}{\sqrt{\varepsilon_{r,eff}}}\ln\left(8\frac{h}{W}+0.25\frac{W}{h}\right)
$$
where
$$
\varepsilon_{r,eff}=\frac{\varepsilon_{r}+1}{2}+\frac{\varepsilon_{r}-1}{2}\left[\left(1+12\frac{h}{W}\right)^{-0.5}+0.04\left(1-\frac{W}{h}\right)^2\right]
$$

```py

ef width(Z0, er, h):
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
```