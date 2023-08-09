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
  - #### Example Usage
    - Calculating how a 100Hz signal with pi/2 phase will appear when sampled at 75Hz
    - `aliasfreq(100, pi/2, 75)`
    - Output: `[25, -pi/2]`
  
- ### convseq
  - #### Inputs
    - sequence 1 (as a list with curly braces)
    - sequence 2 (as a list with curly braces)
  - #### Outputs
    - convolution of the two sequences (as a list with curly braces, starts at t = 0)
  - #### Example Usage
    - Calculating the convolution of the sequences {1, 2, 3} and {4, 5, 6}
    - `convseq({1, 2, 3}, {4, 5, 6})`
    - Output: `{4, 13, 28, 27, 18}`
    #### Notes
    - In order to use the step function, entering a very long list of 1s will suffice. 

- ### DFT
  - #### Inputs
    - sequence 1 (as a list with curly braces)
  - #### Outputs
    - DFT of the sequence (as a list with curly braces)
  - #### Example Usage
    - Calculating the DFT of the sequence {1, 2, 3}
    - `DFT({1, 2, 3})`
    - Output: `{6, -1.5 + 0.8660254038i, -1.5 - 0.8660254038i}`

- ### zeropole
  - #### Inputs
    - Doesn't take any inputs, but prompts 2 inputs:
    - Numerator of the transfer function (uses variable z and has strictly positive powers of z)
    - Denominator of the transfer function (uses variable z and has strictly positive powers of z)
  - #### Outputs
    - zeros (shown as o's)
    - poles (shown as x's)
    - exact locations of the zeros and poles (shown in the calculator page)
  - #### Example Usage
    - Calculating the zeros and poles of the transfer function (z^2 + 1)/(z^4 + 1)
    - `zeropole()`
    - Output: shown on the graph/ calculator page zeros = {i, -i}, poles = {i, -i, 1, -1}
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
