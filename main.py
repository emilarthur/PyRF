from microstrip import *
from microstrip.mlcalc import *

from matching.transformers import binomial

freq = 3e9

sub = Substrate(name="sub", h=0.635e-3, t=35e-6, er=10.2, tanD=0)
W, L = synthesize(Z0=50,f=freq, theta=90, substrate=sub,thickness=True, disp=True)

print(f"W: {W*1e6:.2f} um")
print(f"L: {L*1e6:.2f} um")

print()
# Binomal Transformer
N = 3   # Number of sections
Z0 = 100  # Source impedance
ZL = 50  # Load impedance

Zx = binomial(N, Z0, ZL)

for i in range(1,N+1):
    print(f"{Zx[i-1]:.2f}")




