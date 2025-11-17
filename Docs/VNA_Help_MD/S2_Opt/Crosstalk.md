# Crosstalk

* * *

Crosstalk is energy leakage between analyzer signal paths. This can be a
problem with high-loss transmission measurements. Although the [crosstalk
specification](../Specs/ManualChoice.htm#uncorPerf) of the analyzer is
exceptional, you can reduce the effects of crosstalk by doing the following:

  * [Set the Sweep to Alternate](Crosstalk.md#Swp)

  * [Perform an Isolation Calibration](Crosstalk.md#Cal)

[Other topics about Optimizing Measurements](Optimize.md)

### Set the Sweep to Alternate

This selection is no longer available from the user interface. [Learn
more.](../S1_Settings/Sweep.htm#Alternate)

### Perform an Isolation Calibration

For transmission measurements, a response and isolation measurement
calibration helps reduce crosstalk because the analyzer measures and then
subtracts the leakage signal during the measurement calibration. The
calibration improves isolation so that it is limited only by the noise floor.

Note: Isolation is never performed on a Smart (Guided) Calibration. [Learn
more.](../S3_Cals/Accurate.htm#iso)

Generally, the isolation error falls below the noise floor. So when you are
performing an isolation calibration you should use a noise reduction technique
such as sweep averages or reducing the IF bandwidth.

* * *

