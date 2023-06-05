import numpy as np


def calculate_aliased_frequency(sampling_rate, input_frequency, phase):
    nyquist_frequency = sampling_rate / 2
    normalized_frequency = input_frequency / nyquist_frequency
    folded_frequency = normalized_frequency - np.floor(normalized_frequency)
    aliased_frequency = folded_frequency * nyquist_frequency

    aliased_frequency = round(aliased_frequency, 2)  # Limit to 2 decimal places

    if folded_frequency >= 0.5:
        aliased_frequency = nyquist_frequency - aliased_frequency
        phase = -phase 
    else:
        phase = phase

    return aliased_frequency, phase

# Example usage
sampling_rate = 1000  # Hz
input_frequency = 800  # Hz
input_phase = np.pi / 3  # radians

aliased_freq, phase = calculate_aliased_frequency(sampling_rate, input_frequency, input_phase)

print(f"Aliased Frequency: {aliased_freq:.2f} Hz")
print(f"Phase: {phase:.2f} radians")
