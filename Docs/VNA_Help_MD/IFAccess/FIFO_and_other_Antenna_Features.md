# Fast CW Mode (Opt S93118A/B) and other Antenna Features

* * *

The following features, used with the PNA-X models and the N5264B, were
designed specifically for Antenna applications.

  * ### [Fast CW Mode Features (Opt S93118A/B)](FIFO_and_other_Antenna_Features.md#FastSweep)

  *     * [FIFO Buffer](FIFO_and_other_Antenna_Features.md#FIFO) and [Fast CW](FIFO_and_other_Antenna_Features.md#FastCW)

    * [FIFO Buffer and Fast Groups](FIFO_and_other_Antenna_Features.md#FastGroups)

    * [FIFO Buffer and Fast Segments](FIFO_and_other_Antenna_Features.md#FastSegments)

  * ### [Other Useful Antenna Features](FIFO_and_other_Antenna_Features.md#Other)

  *     * [Point Averaging](FIFO_and_other_Antenna_Features.md#PointAveraging)

    * [Point Sweep](FIFO_and_other_Antenna_Features.md#PointMode)

    * [Trace Triggering](FIFO_and_other_Antenna_Features.md#Trace)

  * ### See Also

  *     * [N5264B](N5264A.md)

    * Pulsed Measurements

    * [Frequency (Security) Blanking](../System/Frequency_Blanking.md)

    * [External Triggering](../S1_Settings/External_Triggering.md)

* * *

## Fast CW Mode Features (Opt S93118A/B)

The following Fast Sweep features allow you to very quickly measure and
download data to a remote computer.

  * [Fast CW](FIFO_and_other_Antenna_Features.md#FastCW), [Fast Groups](FIFO_and_other_Antenna_Features.md#FastGroups), and [Fast CW Segments](FIFO_and_other_Antenna_Features.md#FastSegments) all work ONLY with the FIFO Data Buffer.

  * These features can be used ONLY with [SCPI or COM commands](../Programming/DataTopic.md#FIFO). COM is faster than SCPI when using [DataInCompactForm](../Programming/COM_Reference/Properties/DataInCompactForm_Property.md). Otherwise, SCPI is faster than COM.

### The FIFO Data Buffer

The FIFO (First-IN, First-OUT) data buffer is a circular buffer that allows
very fast Read-Write access.

  * 5 GB FIFO buffer file on the E:\ drive. If the "not enough disk space" error message is displayed, clear all unnecessary files on the E:\ drive.

  * You can write to, and simultaneously read from, the FIFO buffer.

  * A maximum of 1 million data points can be read for each query.

  * REAL / IMAGINARY pairs is the ONLY supported format for the FIFO buffer.

  * A preset or instrument state recall will turn off the FIFO buffer collection.

  * When more than one measurement is present, data from each measurement is stored in the FIFO buffer in the following order. These measurements are separated into lines for easier reading.

PNA-X, 4-port models

R, A, B, C, D,

R/R, A/R, B/R, C/R, D/R,

R/A, A/A, B/A, C/A, D/A,

R/B, A/B, B/B, C/B, D/B,

R/C, A/C, B/C, C/C, D/C,

R/D, A/D, B/D, C/D, D/D

PNA-X, 2-port models

R1, R2, A, B,

R1/R1, R2/R1, A/R1, B/R1

R1/R2, R2/R2, A/R2,B/R2

R1/A, R2/A, A/A, B/A

R1/B, R2/B, A/B, B/B

S-parameters are pre-defined, ratioed-receiver measurements. [Learn
more](../S1_Settings/Measurement_Parameters.htm#Receiver). S-parameters are
placed in the FIFO in order based on their underlying receivers. For example,
S21 is placed into the FIFO in the same manner as B/R1.

### Fast CW

In Fast CW mode the VNA display is not updated. There is no background
computation or other 'interference' from the VNA computer. Therefore, data is
acquired real-time.

The following requirements must be met before sending the Fast CW command.

  * FIFO is ON

  * A single channel is being measured. Other channels can be in Hold.

  * All measurements are acquired in a single sweep.

  * The channel must be in CW mode (start frequency = stop frequency or sweep type = CW Time).

IMPORTANT - Fast CW and IF Bandwidth setting

  * IF Bandwidth of 10 kHz and lower \- Data is transferred immediately to the FIFO after every acquisition.
  * IF Bandwidths greater than 10 kHz \- Data is transferred to the FIFO in groups. A triggered acquisition is NOT placed into the FIFO buffer until either the total number of points is completed, or an intermediate group of points is finished. The number of points within a group differs for each IF Bandwidth setting.

  
---  
  
Notes:

  * See example programs in [SCPI](../Programming/GPIB_Example_Programs/Setup_FastCW_and_FIFO.md) and [COM](../Programming/COM_Example_Programs/Setup_FastCW_and_FIFO.md).

  * Fast CW sets the number of data points, overwriting the standard channel setting.

  * 400,000 points/second applies to 600 KHz at a CW frequency with no point triggering. For narrower bandwidths the speed is slower.

  * Frequency switching time will reduce the speed. The frequency switching can be anywhere from 50 uS to 1 mS depending on the frequencies. The CW segment itself can go at 400,000 points per second.

  * All 5 receivers can do 400,000 point/second at the same time. So the data comes out at 5 times that rate, i.e. 2 Mp/s.

  * When exiting Fast CW, the FIFO data buffer is cleared.

  * External measurement trigger signals are allowed only on Meas Trigger.

  * The Aux 1 and Aux 2 triggers cannot be used per point in FastCW mode.

  * Aux 1 and Aux 2 triggers can still be used for external source hardware triggering, but the external sources must be in CW mode.

  * An error message appears if triggering is sent to the VNA faster than it can respond.

### Fast Groups with FIFO Data Buffer

With this speed optimization feature, interaction with Windows or other VNA
'overhead' calls are suspended, allowing very fast and predictable measurement
timing.

Fast Groups is automatically enabled when the following requirements are met:

  * FIFO is ON

  * A single channel is being measured. Other channels can be in Hold.

  * All measurements are acquired in a single sweep.

  * [Group trigger is enabled](../S1_Settings/Trigger.md#channel_state) with count > 1.

Notes:

  * Fast CW can NOT be used with Fast Groups.

  * Fast Groups and Fast CW Segments were designed to be used together, but not required.

  * The [FIFO Tester](../Programming/GPIB_Example_Programs/Setup_FastCW_and_FIFO.md) example program demonstrates this feature.

### Fast CW Segments with FIFO Buffer

In this optimization feature, each CW segment (where the start and stop
frequency is identical) within a channel is measured at speeds as fast as the
Fast CW mode sweep.

Fast CW Segments is automatically enabled when the following requirements are
met:

  * FIFO is ON

  * Start and stop frequency of a segment is identical.

  * External measurement trigger signals are allowed only on Meas Trigger.

  * The Aux 1 and Aux 2 triggers cannot be used per point in Fast CW Segment.

  * Aux 1 and Aux 2 triggers can be used for external source hardware triggering.

Notes:

  * Fast CW can NOT be used with Fast CW Segments.

  * The sweep can include non-CW segments, but these are not acquired in Fast mode.

  * Fast Groups and Fast CW Segments were designed to be used together, but not required.

  * The [FIFO Tester](../Programming/GPIB_Example_Programs/Setup_FastCW_and_FIFO.md) example program demonstrates this feature.

  * In Fast CW Segments, when data is not being acquired in real-time, the following message appears: Caution: Sweep time jitter. Try reducing the number of segments. To avoid this error, reduce the number of segments in the channel.

## Other Antenna Features

### Point Averaging

This feature is selected on the [Average](../S2_Opt/Trce_Noise.md#averaging)
dialog.

When selected, each data point is measured the specified number of averages
before stepping to the next data point. When [point
trigger](../S1_Settings/Trigger.htm#state_point) is selected, only one trigger
is required for each data point regardless of the number of averages.

### Point Sweep

This feature is selected on the [Sweep
Setup](../S1_Settings/Sweep.htm#SweepSetup) dialog.

In Point Sweep mode, the VNA measures both the forward and reverse parameters
at each frequency point before stepping to the next frequency. The display
trace is updated as each data point is measured. Point sweep is the same as
stepped sweep mode of the 8510 and 8530.

### Trace Triggering

This feature is selected under [Trigger
Mode](../S1_Settings/Trigger.htm#TriggerMode) on the Trigger dialog.

Available ONLY when [Point Sweep](../S1_Settings/Sweep.md#SweepSetupDiag) is
selected. Each trigger signal causes two identical measurements to be
triggered separately - one trigger signal is required for each measurement.
Other trigger mode settings cause two identical parameters to be measured
simultaneously.

Trace triggering is NOT permitted when a channel is using a 2 port (or more)
S-Parameter calibration.

### See Also

  * Pulsed Measurements

  * [Frequency (Security) Blanking](../System/Frequency_Blanking.md)

  * [External Triggering](../S1_Settings/External_Triggering.md)

* * *

