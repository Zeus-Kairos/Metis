# Calibration Overview

* * *

The following is discussed in this topic:

  * [What Is Measurement Calibration?](Measurement_Calibration.md#what)

  * [Why Is Calibration Necessary?](Measurement_Calibration.md#why)

  * [Conditions Where Calibration Is Suggested](Measurement_Calibration.md#conditions)

  * [What Is ECal?](Measurement_Calibration.md#ecal)

[See other Calibration Topics](Calibration.md)

What Is Measurement Calibration?

Calibration removes one or more of the systematic errors using an equation
called an error model. Measurement of high quality standards (for example, a
short, open, load, and thru) allows the analyzer to solve for the error terms
in the error model. See [Measurement Errors](Errors.md).

You can choose from different calibration types, depending on the measurement
you are making and the level of accuracy you need for the measurement. See
[Select a Calibration Type](Select_Cal.md).

The accuracy of the calibrated measurements is dependent on the quality of the
standards in the calibration kit and how accurately the standards are modeled
(defined) in the calibration kit definition file. The calibration-kit
definition file is stored in the analyzer. In order to make accurate
measurements, the calibration-kit definition must match the actual calibration
kit used. To learn more, see [Accurate Calibrations](Accurate.md).

Calibration Wizard provides the different calibration methods used in the VNA.
See [Calibration Wizard](Calibration_Wizard.md).

There are quick checks you can do to ensure your measurement calibration is
accurate. To learn more see [Validity of a Measurement
Calibration](Quest_Cal.htm)

If you make your own custom-built calibration standards (for example, during
in-fixture measurements), then you must characterize the calibration standards
and enter the definitions into a user modified calibration-kit file. For more
information on modifying calibration kit files, see [Calibration
Standards](ModifyCalKits.htm).

Note: [Instrument Calibration](../Support/Instrument_Calibration.md) is
ensuring the analyzer hardware is performing as specified. This is not the
same as measurement calibration.

Why Is Calibration Necessary?

It is impossible to make perfect hardware that would not need any form of
error correction. Even making the hardware good enough to eliminate the need
for error correction for most devices would be extremely expensive.

The accuracy of network analysis is greatly influenced by factors external to
the network analyzer. Components of the measurement setup, such as
interconnecting cables and adapters, introduce variations in magnitude and
phase that can mask the actual response of the device under test.

The best balance is to make the hardware as good as practically possible,
balancing performance and cost. Calibration is then a very useful tool to
improve measurement accuracy.

Conditions Where Calibration Is Suggested

Generally, you should calibrate for making a measurement under the following
circumstances:

  * You want the best accuracy possible.

  * You are adapting to a different connector type or impedance.

  * You are connecting a cable between the test device and an analyzer test port.

  * You are measuring across a wide frequency span or an electrically long device.

  * You are connecting an attenuator or other such device on the input or output of the test device.

If your test setup meets any of the conditions above, the following system
characteristics may be affected:

  * Amplitude at device input

  * Frequency response accuracy

  * Directivity

  * Crosstalk (isolation)

  * Source match

  * Load match

What Is ECAL

ECal is a complete solid-state calibration solution. It makes one port
(Reflection), full two and three-port calibrations fast and easy. See [Using
ECal](Using_ECal.htm).

  * It is less prone to operator error.

  * The various standards (located inside the calibration module) never wear out because they are switched with PIN-diode or FET switches.

  * The calibration modules are characterized using a TRL-calibrated network analyzer.

  * ECal is not as accurate as a good TRL calibration.

For information about ordering ECal modules, see [Analyzer
Accessories](../Support/Analyzer_Accessories.htm) or contact your [Keysight
Support Representative](../Support/Tech_Supp.htm)

* * *

