import math

def rc_cutoff_frequency(resistor, capacitor):
    """
    Calculates the cut-off frequency for a first-order RC filter.
    
    Args:
        resistor (float): Resistance value in ohms.
        capacitor (float): Capacitance value in farads.
    
    Returns:
        float: Cut-off frequency in hertz.
    """
    return 1 / (2 * math.pi * resistor * capacitor)

# Example usage
resistor_value = 1000  # 1 kilohm
capacitor_value = 1e-6  # 1 microfarad

cutoff_frequency = rc_cutoff_frequency(resistor_value, capacitor_value)
print("Cut-off frequency: {:.2f} Hz".format(cutoff_frequency))
