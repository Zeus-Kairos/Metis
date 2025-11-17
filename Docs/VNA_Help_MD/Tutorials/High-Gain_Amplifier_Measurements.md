# High-Gain Amplifier Measurements

* * *

When measuring High-Gain Amplifiers, errors in measuring any of the
S-parameters during calibration can result in error in the S21 measurement.
This is because all the S-parameters are used in the error correction math.

A particular problem occurs with high gain amplifiers because the source power
is set very low. Thus, when making reverse measurements (S22, S12) the signal-
to-noise is poor and the raw measurements can be dominated by noise. This
noise in the raw measurements will result in a noisy trace appearing for
corrected S21 or S11.

If you are using a large attenuator on port 2 (which improves output match),
perform an Enhanced Response Calibration as follows. This corrects for the
same errors as the full 2-port correction EXCEPT the interaction between the
raw load match and the DUT output match.

  1. There is NO need to Uncouple the port powers.

  2. Set port powers to an acceptable level. Do NOT overpower the test port.

  3. Perform Enhanced Response Cal. [Learn how.](../S3_Cals/Select_Cal.md#Enhanced) (Does not measure or correct for S12 or S22 port match).

If you want to do a full correction (for example, when your amplifier output
match is poor so the Enhanced Response Cal above is not adequate), then...

  1. Uncouple the port powers. [Learn how](../S1_Settings/Power_Level.md#Advanced).

  2. Set input (port 1) power to approximately the output power of the amplifier up to 0 dBm

  3. Set reverse (port 2) power to the same power (for measuring isolation and S22) 

  4. Perform a Full 2-port Cal.

  5. Re-set the input power (port 1) to a lower power level appropriate for driving the amplifier.

Additional Error due to Mismatch of DUT Output Match and Raw Load Match  
---  
![](../assets/images/hiGainAmpError.gif)  
  
* * *

