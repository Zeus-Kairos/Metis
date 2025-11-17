# Front-Panel Jumpers

* * *

There are many reasons to configure the front-panel jumpers on the VNA.

  * [High-power measurements using the VNA - App Note 1408-10](http://literature.cdn.Keysight.com/litweb/pdf/5989-1349EN.pdf)

  * [Using a Booster Amp for SMC Measurements](../FreqOffset/SMC_with_a_Booster_Amp.md)

  * [Improving Dynamic Range](../S2_Opt/Dyn_Rge.md)

Note: Phase-locking and the Reference Receivers The R1 and R2 reference
receivers are used for phase-locking between the RF source and receiver LO.
The phase-locking requirement imposes the following restrictions on the
reference signal:

  * PNA-X and N522x power level: limited by the noise floor
  * All models require a clean signal without spurious content

In [Frequency Offset Mode](../FreqOffset/Frequency_Offset_Mode.md) (FOM) Opt
S93080A, the R1 receiver is NOT used for phase locking. Independent internal
circuitry is used to phase lock the source and receivers. When FOM is
available, turn FOM ON simply to take advantage of the independent phase
locking mechanism. If NOT measuring at different source and receiver
frequencies, set the offset to zero, so that the source and receiver
frequencies are the same.  
---  
  
### Topics

  * [High-power measurements](../Tutorials/High_Power_PNA-X.md)

### See Also

  * [Arbitrary Ratio](../S1_Settings/Measurement_Parameters.md#arb_ratio)

  * [Block diagrams and Specifications](../Specs/ManualChoice.md)

  * [VNA Options and Configurations](../Support/Configurations.md)

* * *

