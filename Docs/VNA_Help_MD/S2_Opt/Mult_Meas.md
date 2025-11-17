# Switch Between Multiple Measurements

* * *

If you need to make multiple measurements to characterize a device, you can
use various methods to increase throughput. Experiment with these methods to
find what is best for your measurement application needs.

  * [Set Up Measurements for Increased Throughput](Mult_Meas.md#set)

  *     * [Arrange Measurements in Sets](Mult_Meas.md#arrange)

    * [Use Segment Sweep](Mult_Meas.md#use)

    * [Trigger Measurements Selectively](Mult_Meas.md#trigger)

  * [Automate Changes Between Measurements](Mult_Meas.md#auto)

  * [Recall Measurements Quickly](Mult_Meas.md#recall)

[Other topics about Optimizing Measurements](Optimize.md)

Set Up Measurements for Increased Throughput

To achieve optimum throughput of devices that require multiple measurements,
it is helpful to know the operation of the analyzer. This knowledge allows you
to set up the measurement scenarios that are best for your applications.

[Learn more about Traces, Channels, and
Windows](../S0_Start/Traces_Channels_and_Windows.htm)

Arrange Measurements in Sets

If you arrange measurements to keep the complete set of device measurements in
one instrument state, you can save them so that you can later recall a number
of measurements with one recall function.

See Pre-configured Measurement Setups for more information.

Use Segment Sweep

Segment sweep is helpful if you need to change the following settings to
characterize a device under test.

  * Frequency Range

  * Power Level

  * IF Bandwidth

  * Number of Points

  * Delay

  * Sweep Mode

  * LO Offset

The segment sweep allows you to define a set of frequency ranges that have
independent attributes. This allows you to use one measurement sweep to
measure a device that has varying characteristics.

See [Segment Sweep](../S1_Settings/Sweep.md#segment) for more information.

Trigger Measurements Selectively

You can use the measurement trigger to make measurements as follows:

  * Continuously update only the measurements that have rapidly changing data.

  * Occasionally update measurements that have infrequently changing data.

For example, if you had four channels set up as follows:

  * Two channels measuring the data that is used to tune a filter

  * Two channels measuring the data for the out-of-band responses of the filter

You would want to constantly monitor only the measurement data that you use
for tuning the filter. If you continuously update all of the channels, this
could slow the response of the analyzer so that you would not be able to tune
the filter as effectively.

Note: You must either trigger the infrequent measurement manually or with
remote interface commands.

To trigger measurements selectively:

This procedure shows you how to set up two different measurements with the
following behavior:

  * Channel 1 measurement will continuously update the data.

  * Channel 2 measurement will occasionally update the data.

  1. Press Setup > Quick Start.

  2. At the Quick Start dialog box, click Create in new channel.

  3. Frequency Sweep dialog box shows. Enter the preferred sweep setting.

### Set Up a Measurement Trigger for Continuous Updates

  1. Press Trigger > Trigger Source and select Internal.

  2. Press Trigger > Trigger....

  3. At the Trigger dialog box under Channel Trigger State, select Channel 1, and click Continuous.

### Set Up a Measurement Trigger for Occasional Updates

  1. At the Trigger dialog box under Channel Trigger State, select Channel 2, and click Single, OK.

  2. Press Trigger > Restart.

### Update the Measurement

  1. Click on the lower window to make Channel 2 the active channel.

  2. On the active entry toolbar, click the type of trigger you set up.

     * Click Single if you set up the analyzer for a single sweep per trigger.

     * Click Groups if you set up the multiple sweeps per trigger.

Note: A trace must be active for you to initiate a trigger for that
measurement.

Automate Changes Between Measurements

If there are slight differences between the various measurements that you need
to characterize a device, you may find that it is faster to change the
measurement settings using programming.

Recall Measurements Quickly

The most efficient way to recall measurements is to recall them as a set of
measurements (instrument state).

  * It only takes a short time longer to recall an instrument state that includes multiple measurements, than it does to recall an instrument state with only one measurement.

  * Each recall function has time associated with it. You can eliminate that time by setting up the measurements as a set so you can recall them as a set.

See [Save and Recall Files](../S5_Output/SaveRecall.md) for more information.

* * *

