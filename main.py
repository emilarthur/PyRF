# from microstrip import *
# from microstrip.mlcalc import *

# from matching.transformers import binomial

# freq = 3e9

# sub = Substrate(name="sub", h=0.635e-3, t=35e-6, er=10.2, tanD=0)
# W, L = synthesize(Z0=50,f=freq, theta=90, substrate=sub,thickness=True, disp=True)

# print(f"W: {W*1e6:.2f} um")
# print(f"L: {L*1e6:.2f} um")

# print()
# # Binomal Transformer
# N = 3   # Number of sections
# Z0 = 100  # Source impedance
# ZL = 50  # Load impedance

# Zx = binomial(N, Z0, ZL)

# for i in range(1,N+1):
#     print(f"{Zx[i-1]:.2f}")



import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

# Define signal parameters
duration = 10e-6  # Duration of the signal in seconds (10 microseconds)
center_freq = 9.4e9  # Center frequency in Hz (9.4 GHz)
span = 100e6         # Frequency span in Hz (100 MHz)
f_start = center_freq - span / 2  # Start frequency
f_end = center_freq + span / 2    # End frequency
f_max = f_end  # Maximum frequency of the signal

# Dynamically set the number of samples based on Nyquist theorem
sampling_rate = 2 * f_max  # Minimum sampling rate (Nyquist theorem)
N = int(sampling_rate * duration)  # Total number of samples
T = 1 / sampling_rate  # Sampling interval (time step)
t = np.linspace(0, duration, N)  # Time vector with N points from 0 to duration

# Generate Linear Frequency Modulation (LFM) signal
x_lin = chirp(t, f0=f_start, f1=f_end, t1=duration, method='linear')

# Compute FFT
fft_x = np.fft.fft(x_lin)
fft_x = np.abs(fft_x)  # Magnitude of FFT
freq = np.fft.fftfreq(N, T)  # Frequency axis

# Convert FFT frequency to positive only and adjust units to GHz
positive_freq = freq[:N // 2] / 1e9  # Convert to GHz
positive_fft = fft_x[:N // 2]

# Plot the LFM signal, its FFT, and the spectrogram
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Plot the LFM signal (Amplitude vs. Time)
axs[0].plot(t * 1e6, x_lin, color='b', linestyle='-', label="Linear Frequency Modulation")
axs[0].set_xlim(t[0] * 1e6, t[-1] * 1e6)  # Convert time axis to microseconds
axs[0].set_title("Linear Frequency Modulation Signal")
axs[0].set_xlabel("Time (µs)")
axs[0].set_ylabel("Amplitude")
axs[0].grid(True)
axs[0].legend(loc="upper right")

# Plot the FFT (Magnitude vs. Frequency)
axs[1].plot(positive_freq, positive_fft, color='r', linestyle='-', label="FFT of LFM Signal")
axs[1].set_xlim(9.2, 9.6)  # Set frequency range to show the span
axs[1].set_title("FFT of Linear Frequency Modulation Signal")
axs[1].set_xlabel("Frequency (GHz)")
axs[1].set_ylabel("Magnitude")
axs[1].grid(True)
axs[1].legend(loc="upper right")

# Plot the spectrogram
f_spect, t_spect, Sxx = spectrogram(x_lin, fs=sampling_rate, nperseg=2**16, noverlap=512, scaling='density')
axs[2].pcolormesh(t_spect * 1e6, f_spect / 1e9, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
axs[2].set_title("Spectrogram of Linear Frequency Modulation Signal")
axs[2].set_xlabel("Time (µs)")
axs[2].set_ylabel("Frequency (GHz)")
axs[2].set_xlim(t[0] * 1e6, t[-1] * 1e6)
axs[2].set_ylim(f_start / 1e9, f_end / 1e9)
plt.colorbar(axs[2].collections[0], ax=axs[2], label="Power Spectral Density (dB)")

# Apply tight layout
plt.tight_layout()

# Show the plot
plt.show()





