# TI Nspire Electrical Engineering Tools

Convenient tools for Electrical Engineers to be used on TI-Nspire.
Down are the list of tools and their required parameters.

## DSP (Digital Signal Processing):
- [`aliasfreq(input frequency, phase, sampling frequency)`](#aliasfreq)
- [`convseq(seq1,seq2)`](#convseq)
- [`DFT(seq1)`](#dft)
- [`zeropole()`](#zeropole)
- [`zeropolefreqres()`](#zeropolefreqres)
- [`fouriercoef()`](#fouriercoef)
  - Currently usable but has bugs for piecewise functions. Sinusoids are not properly handled.

## E&M (Electrical and Magnetic) Interactions:
- [`gausslaw1()`](#gausslaw1)
- [`kinetice(mass, velocity)`](#kinetice)
- [`coulomblaw()`](#coulomblaw)

## RLC (Resistor Inductor Capacitor):
- [`capseries({c1, c2, c3, ..., cn})`](#capseries)
- [`capvoltage()`](#capvoltage)
- [`capcurrent()`](#capcurrent)
- [`resparallel({r1, r2, r3, ..., rn})`](#resparallel)
- [`indparallel({l1, l2, l3, ..., ln})`](#indparallel)
- [`indcurrent()`](#indcurrent)
- [`indvoltage()`](#indvoltage)
- [`indimpedance(freq, inductance)`](#indimpedance)
- [`capimpedance(freq, capacitance)`](#capimpedance)


## Power:
- [`rmsintegral()`](#rmsintegral)



# Function Descriptions and Usage
Here is a detailed explanation of what each function does, and how to get the most out of them!


## DSP (Digital Signal Processing):
- ### aliasfreq
  - #### Inputs
    - frequency (Hz)
    - phase (rad)
    - sampling frequency (Hz)
  - #### Outputs
    - aliased/folded frequency (Hz)
    - phase (rad)
- ### convseq
- ### DFT
- ### zeropole
- ### zeropolefreqres
- ### fouriercoef
  - Currently usable but has bugs for piecewise functions. Sinusoids are not properly handled.

## E&M (Electrical and Magnetic) Interactions:
- ### gausslaw1
- ### kinetice
- ### coulomblaw

## RLC (Resistor Inductor Capacitor):
- ### capseries
- ### capvoltage
- ### capcurrent
- ### resparallel
- ### indparallel
- ### indcurrent
- ### indvoltage
- ### indimpedance
- ### capimpedance

## Power
- ### rmsintegral
