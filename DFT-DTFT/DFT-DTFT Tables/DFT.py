import numpy as np

def calculate_dft(sequence):
    N = len(sequence)
    dft_result = []
    
    for k in range(N):
        dft_value = 0
        for n in range(N):
            exponent = -2j * np.pi * k * n / N
            dft_value += sequence[n] * np.exp(exponent)
        dft_result.append(dft_value)
    
    return dft_result

sequence = [1, 2, 3, 4, 5]

dft_result = calculate_dft(sequence)
print("DFT Result:")
for index, value in enumerate(dft_result):
    print(f"DFT[{index}]: {value}")
