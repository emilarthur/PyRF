from microstrip import *
from microstrip.mlcalc import *

freq = 3e9

sub = Substrate(name="sub", h=0.635e-3, t=35e-6, er=10.2, tanD=0)
W, L = synthesize(Z0=50,f=freq, theta=90, substrate=sub,thicknesss=True, disp=True)