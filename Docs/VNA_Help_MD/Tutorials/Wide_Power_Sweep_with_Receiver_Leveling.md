# Wide Power Sweep with Receiver Leveling

* * *

The following procedure illustrates how to use the [Receiver
Leveling](../S1_Settings/Receiver_Leveling.htm) feature to extend the power
sweep range of the VNA, sometimes to 60 dB. Your actual sweep range may vary
depending on the power offset setting and maximum available power at each
frequency.

With VNA internal leveling, the power sweep range is limited to the range of
the internal VNA source which is about 30 to 40 dB depending on the frequency
range. See [Power Sweep Range in the specs](../Specs/ManualChoice.md).

Note: You may not be able to achieve 60 dB of power sweep on your VNA. This is
NOT specified.

With the use of source attenuation, the low power setting can be adjusted down
to -95 dBm.

Without source attenuation, receiver leveling extends the low power setting to
about -60 dBm. This is done by measuring and adjusting the source power at
every data point. Because power levels are very low, noise must be reduced
using [IFBW](../S2_Opt/Trce_Noise.md#HowToIFBW) or
[Averaging](../S2_Opt/Trce_Noise.md#averaging).

  1. Press Sweep > Main > Sweep Setup....

  2. In the Sweep Setup dialog select Power Sweep.

  3. Set Start Power to -60 dBm.

  4. Set Stop Power to 0 dBm.

  5. Set CW Freq of the measurement. Click OK.

  6. Press Power > Main > Power and Attenuators....

  7. Click Leveling Mode then Receiver-R1.

  8. Click Receiver Leveling... button.

  9. Clear Enable source ALC hardware circuit checkbox.

  10. When the measured power level falls below some level, the message appears: Power set to min power level.

  11. Press Avg BW > Main > IF Bandwidth to reduce the amount of noise on the measurement.

  12. Adjust the scale.

For troubleshooting purposes, display R1 trace to view the power level at test
port 1.

* * *

