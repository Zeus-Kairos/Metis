# Achieve Fastest Sweep

* * *

You can achieve the fastest measurement sweep by adjusting the following:

  * [Sweep Settings](Fast_Swp.md#sweep)

  * [Noise Reduction Settings](Fast_Swp.md#noise)

  * [Measurement Calibration Choice](Fast_Swp.md#cal)

  * [Unnecessary Functions](Fast_Swp.md#func)

[Other topics about Optimizing Measurements](Optimize.md)

Sweep Settings

Consider changing each of the following settings as suggested.

  * [Frequency Span](../S1_Settings/Frequency_Range.md#How to) - Measure only the frequencies that are necessary for your device.

  * [Segment Sweep](../S1_Settings/Sweep.md#segment) - Use segments to focus test data only where you need it.

  * [Switch Off Stepped Sweep](../S1_Settings/Sweep.md#Stepped) - Use linear swept mode to minimize sweep time when possible.

  * [Auto Sweep Time](../S1_Settings/Sweep.md#SettingSweepSpeed) - Use this default to sweep as quickly as possible for the current settings.

  * [Number of Points](../S1_Settings/DPoints.md) - Use the minimum number of points required for the measurement.

For more information on how number of points and other settings affect sweep
cycle time, see [Technical Specifications](../Specs/ManualChoice.md#Speed).

Noise Reduction Settings

Using a combination of these settings, you can decrease the sweep time while
still achieving an acceptable measurement.

  * [IF Bandwidth](Trce_Noise.md#HowToIFBW). Use the widest IF bandwidth that will produce acceptable trace noise and [dynamic range](Dyn_Rge.md).

  * [Average](Trce_Noise.md#HowToAver). Reduce the average factor, or switch Average off.

Measurement Calibration Choice

Choose the appropriate type of calibration for the required level of accuracy.

When full 2-port error correction is applied, the analyzer takes both forward
and reverse sweeps to gather all 12 error correction terms. This occurs even
with a single S11 measurement displayed. All displayed measurements are
updated as the second sweep is performed. Both sweeps are performed using the
specified sweep time.

When calibrating greater than 2 ports, the following formula is used to
determine the number of sweeps required:

  * N * (N-1) where N = the number of ports.

When full 3-port calibration is applied, 6 sweeps are required; forward and
reverse for each port pair. With full 4-port correction, 12 sweeps are
required, and so forth.

To limit the measurement time, perform ONLY the level of calibration that your
measurements require. For example, if making only an S11 measurement, perform
a 1-port calibration on that port.

Sweep speed is about the same for uncorrected measurements and measurements
done using a response calibration, or one-port calibration. For more
information see [Select a Calibration](../S3_Cals/Select_Cal.md).

Unnecessary Functions

The analyzer must update information for all active functions. To achieve an
additional increase in sweep speed, switch off all of the analyzer functions
that are not necessary for your measurement application.

  * [Delete Unwanted Traces](../S0_Start/Traces_Channels_and_Windows.md#DeleteTrace)

  * [Switch Off Unwanted Markers](../S4_Collect/Markers.md#HowMarkerDiag)

  * [Switch Off Smoothing](Trce_Noise.md#HowToSmooth)

  * [Switch Off Limit Testing](../S4_Collect/Use_Limits_to_Test_Devices.md#limit_testing)

  * [Switch Off Math Functions](../S4_Collect/Math_Operations.md#MathMemorydialogbox)

Analyzer sweep speed is dependent on various measurement settings. Experiment
with the settings to get the fastest sweep and the measurement results that
you need.

* * *

