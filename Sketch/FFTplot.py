import numpy as np
import matplotlib.pyplot as plt

def plot_fft(N, sequence):
    dft_result = np.fft.fft(sequence, N)
    magnitude_spectrum = np.abs(dft_result)
    
    plt.stem(range(N), magnitude_spectrum)
    plt.xlabel('Frequency index')
    plt.ylabel('Magnitude')
    plt.title('Magnitude Spectrum (FFT)')
    plt.show()

# Example usage
N = 16
sequence = [1,1,1]

plot_fft(N, sequence)
