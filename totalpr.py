def TotalPR(*resistances):
    total_inverse_resistance = sum(1 / resistance for resistance in resistances)
    return 1 / total_inverse_resistance

# Example usage
resistances = [10, 20, 30, 40]  # Resistances in parallel: 10Ω, 20Ω, 30Ω, 40Ω

rp = TotalPR(*resistances)

print("Parallel Resistance:", rp, "Ω")
