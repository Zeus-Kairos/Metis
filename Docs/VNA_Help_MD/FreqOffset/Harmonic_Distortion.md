# Harmonic Distortion

* * *

  * [What is Harmonic Distortion?](Harmonic_Distortion.md#harmonic_distortion_what_is)

  * [Why Measure Harmonic Distortion?](Harmonic_Distortion.md#harmonic_distortion_why_meas)

  * [How to Measure Harmonic Distortion](Harmonic_Distortion.md#harmonic_distortion_how_meas)

  * [Measurement and Accuracy Considerations](Harmonic_Distortion.md#harmonic_distortion_accuracy)

[See other Frequency Converting Device
Measurements](Frequency_Converting_Device_Measurements.htm)

What is Harmonic Distortion?

Harmonics are multiples of any signal appearing at the mixer input and also
multiples of the LO input. The distortion of the mixer's output
characteristics caused by these harmonics is referred to as harmonic
distortion. Harmonic distortion is caused by non-linearities in the device.

Harmonics are NOT signals created by two or more signals interacting (mixing);
these signals are known as intermodulation products, which result in
intermodulation distortion.

Why Measure Harmonic Distortion?

  * It can degrade the performance of devices connected to the output of the mixer.

  * The harmonics can also mix with other signals present in the mixer, adding to the intermodulation distortion of the mixer.

### How to measure Harmonic Distortion

The harmonics can be measured using the VNA with [Frequency
Offset](Frequency_Offset_Mode.htm) (option 80). The frequency of the LO to the
mixer is set to zero and multiplier of the RF input is used to set the IF
frequency (the harmonic). The equipment setup is shown below.

Since harmonics are specified in dBc, the fundamental RF and both the second
and third harmonics are measured and the differences calculated. Multiple
channels can be used to do this.

  1. Connect the equipment.

  2. Setup the measurement for calibration. See also [Measurement and Accuracy Considerations](Harmonic_Distortion.md#harmonic_distortion_accuracy).

Use three channels and [frequency offset mode](Frequency_Offset_Mode.md):

Channel 1 = F1 to F2

Channel 2 = F1 to 2F2 (frequency offset mode, multiplier = 1)

Channel 3 = F1 to 3F2 (frequency offset mode, multiplier = 1)

  * Perform a source power calibration and receiver power calibration over the entire frequency range. See [Measurement and Accuracy Considerations](Harmonic_Distortion.md#harmonic_distortion_accuracy).

  * Reduce the frequency span and increase the frequency offset multiplier on Channels 2 and 3:

Channel 2 = F1 to F2 (frequency offset mode, multiplier = 2)

Channel 3 = F1 to F2 (frequency offset mode, multiplier = 3)

Note: Because the frequency span has been changed from that used for
calibration, the source and receiver calibrations will be interpolated.

  * Connect the DUT, make the measurement, and calculate the harmonic response:

Set up markers on Channels 1, 2 and 3, and determine the difference between
the marker values to get the dBc value of each harmonic.

Channel 1 - Channel 2 = 2nd harmonic (dBc)

Channel 1 - Channel 3 = 3rd harmonic (dBc)

Note: Be sure to set the markers to the appropriate stimulus. Channel 2
markers should be set to twice the frequency of Channel 1 markers. Channel 3
markers should be set to three times the frequency of Channel 1 markers.

Measurement and Accuracy Considerations

### Equipment Setup Considerations

  * A filter must be used at the input of the mixer to remove the VNA source harmonics.

