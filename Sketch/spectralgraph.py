import numpy as np
import matplotlib.pyplot as plt

def spectralgraph(A, f, phase):
    stem_frequencies = [f, -f]
    stem_amplitudes = [A / 2 * np.exp(1j * phase), A / 2 * np.exp(-1j * phase)]

    # Plot the spectral graph with stems
    plt.stem(stem_frequencies, np.abs(stem_amplitudes), linefmt='C0-', basefmt=" ", use_line_collection=True)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Spectral Graph')
    plt.show()

# Example usage
spectralgraph(2, 100, np.pi/2)
