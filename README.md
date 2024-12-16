
# PyRF

This script can analyze and synthesize microstrip parameters based on Guillermo Gonzalez book "Microwave Transistor Amplifiers 2nd Edition" chapter 2.5.

Note that losses (α) are not accounted for.

```py
from microstrip import *
from microstrip.mlcalc import *
```
## Example
Instanciate a substrate
```py
RO6010 = Substrate(name="RO6010", h=0.635e-3, t=35e-6, er=10.2, tanD=0)
```
Calculate width and length
```py
W, L = synthesize(Z0=50,f=3e9, theta=90, substrate=RO6010,thicknesss=True, disp=True)
```
## Microstrip
Characteristic impedance of a microstrip line

For $W/h\leq1$:

$$
Z_0=\frac{60}{\sqrt{\varepsilon_{r,eff}}}\ln\left(8\frac{h}{W}+0.25\frac{W}{h}\right)
$$

where

$$
\varepsilon_{r,eff}=\frac{\varepsilon_{r}+1}{2}+\frac{\varepsilon_{r}-1}{2}\left[\left(1+12\frac{h}{W}\right)^{-0.5}+0.04\left(1-\frac{W}{h}\right)^2\right]
$$

for $W/h\geq1$:
$$
Z_0=\frac{120\pi/\sqrt{\varepsilon_r}}{W/h+1.393+0.667\ln(W/h+1.444)}
$$

where

$$
\varepsilon_{r,eff}=\frac{\varepsilon_{r}+1}{2}+\frac{\varepsilon_{r}-1}{2}\left(1+12\frac{h}{W}\right)^{-0.5}
$$

Waveength in the microstrip line

For $W/h\geq0.6$:

$$
\lambda=\frac{\lambda_0}{\sqrt{\varepsilon_r}}\left[\frac{\varepsilon_r}{1+0.63(\varepsilon_r-1)(W/h)^{0.1255}}\right]^{0.5}
$$

For $W/h\leq0.6$:
$$
\lambda=\frac{\lambda_0}{\sqrt{\varepsilon_r}}\left[\frac{\varepsilon_r}{1+0.6(\varepsilon_r-1)(W/h)^{0.0297}}\right]^{0.5}
$$


