import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
window = np.hanning(51)
plt.plot(window)
plt.title("Hann window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()
plt.figure()

A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
freq = np.linspace(-0.5, 0.5, len(A))
with np.errstate(divide='ignore', invalid='ignore'):
    response = 20 * np.log10(mag)

response = np.clip(response, -100, 100)
plt.plot(freq, response)

plt.title("Frequency response of the Hann window")

plt.ylabel("Magnitude [dB]")

plt.xlabel("Normalized frequency [cycles per sample]")

plt.axis('tight')

plt.show()