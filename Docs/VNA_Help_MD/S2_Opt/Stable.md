# Measurement Stability

* * *

There are several situations that can cause unstable measurements. To ensure
that you are making repeatable measurements, you can use various methods to
create a stable measurement environment.

  * [Frequency Drift](Stable.md#Fdrift)

  * [Temperature Drift](Stable.md#Tdrift)

  * [Inaccurate Measurement Calibrations](Stable.md#Data)

  * [Device Connections](Stable.md#Conn)

[Other topics about Optimizing Measurements](Optimize.md)

Frequency Drift

The analyzer frequency accuracy is based on an internal 10 MHz frequency
oscillator. See [Technical Specifications](../Specs/ManualChoice.md#RPanel)
for stability and aging specifications.

If your measurement application requires better frequency accuracy and
stability, you can override the internal frequency standard and provide your
own high-stability external frequency source through the 10 MHz Reference
[Input connector on the rear panel.](../Rear_Panel/XRtour.md#10M)

Temperature Drift

Thermal expansion and contraction changes the electrical characteristics of
the following components:

  * Devices within the analyzer

  * Calibration kit standards

  * Test devices

  * Cables

  * Adapters

To reduce the effects of temperature drift on your measurements, do the
following.

  * Switch on the analyzer 1/2 hour before performing a measurement calibration or making a device measurement.

  * One hour before you perform a measurement calibration, open the case of the calibration kit and take the standards out of the protective foam.

  * Use a temperature-controlled environment. All specifications and characteristics apply over a 25 °C ±5 °C range (unless otherwise stated).

  * Ensure the temperature stability of the calibration kit devices.

  * Avoid handling the calibration kit devices unnecessarily during the calibration procedure.

  * Ensure the ambient temperature is ±1°C of the measurement calibration temperature.

Inaccurate Measurement Calibrations

If a measurement calibration is inaccurate, you will not measure the true
response of a device under test. To ensure that your calibration is accurate,
you should consider the following practices:

  * Perform a measurement calibration at the points where you connect the device under test, that is, the reference plane.

  * If you insert any additional accessory (cable, adapter, attenuator) to the test setup after you have performed a measurement calibration, use the port extensions function to compensate for the added electrical length and delay.

  * Use calibration standards that match the definitions used in the calibration process.

  * Inspect, clean, and gage connectors. See [Connector Care](../Tutorials/Connector_Care.md).

See [Accurate Measurement Calibrations](../S3_Cals/Accurate.md) for more
detailed information.

Device Connections

Good connections are necessary for repeatable measurements. To help make good
connections, do the following:

  * Inspect and clean the connectors for all of the components in the measurement setup.

  * Use proper connection techniques.

  * Avoid moving the cables during a measurement.

* * *

