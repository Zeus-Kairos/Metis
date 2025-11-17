# Comparing the VNA "Delay" Functions

* * *

The VNA has three Delay functions which are similar but are used in different
ways.

1\. [Group Delay format](../S1_Settings/Data_Format.md#Group_Delay) is used
to display the Group Delay of a network. Group Delay is defined as:

-d(phi)/d(omega) \-- where phi is radian angle, and omega is radian frequency. 

Since it is defined by a derivative, the value must be determined from an
analytic function. However, the VNA makes discrete measurements, so we
approximate the group delay by taking the finite difference:

-(1/360)*delta(phi)/delta(f) \-- where phi is degree angle and f is frequency in Hz. The 1/360 does the proper conversion of degrees to radians and Hz frequency to radian frequency. 

From this we can see that, if the phase response of a network varies with
frequency, then the Group Delay must vary as well. In fact, many filters are
specified by the variation of their Group Delay.

If we measure the phase response of a lossless cable, it should be a straight
line. But, of course, nothing is perfect. The phase response will have a small
amount of noise. This is due to trace noise of the VNA, and the loss with real
cables or transmission lines, which causes a small amount of non-linear phase
change with frequency. So, if we look at the Group Delay of a cable, we will
see a small amount of variation. Also, if the frequency spacing is small
enough when you make the measurement, the delta(f) in the denominator becomes
very small, so the delay can have wide swings with just a little noise.

To overcome this issue, we sometimes add smoothing to a phase trace, which
widens the effective delta(f), called the aperture, and provides a less noisy
Group Delay response. The Group Delay of a device is only valid for a given
frequency aperture. [Learn more about Group Delay.](Group_Delay6_5.md)

2\. [Electrical Delay](../S2_Opt/Phase_Accy.md#ElectricalDiag) function. On
many filters, the passband response is specified for a maximum value of
"Deviation from Linear Phase". When looking at the passband of a multi-pole
filter, one sees the phase changing very rapidly. This makes it difficult to
determine the linearity of the phase response. The Electrical Delay function
subtracts out a "LINEAR PHASE" equivalent to the delay time value computed as
above. When you use this function, you dial in the Linear Delay such that a
CONSTANT PHASE SLOPE is removed from the phase trace, until the phase trace is
mostly flat. The remaining variation is the deviation from linear phase.

To make this task a little less tedious, the VNA has a marker function called
[Marker =>> Delay](../S4_Collect/Markers.md#functions). This function
computes the Group Delay value at the marker position, using a 20% smoothing
aperture, then changes the Electrical Delay value to this value. Obviously, if
the phase trace is not perfectly linear, moving the marker and recomputing the
delay will result in different values. The phase slope added by the electrical
delay function applies only to the current measurement. That is, each
measurement (S11, S22, S12, S21) can have its own value of electrical delay.
[Learn more about Deviation from Linear Phase](Phase_Devi.md).

3\. [Port Extension](../S3_Cals/Port_Extensions.md) is a function that is
similar to calibration. It applies to all the traces in a given channel. It
compensates for the phase response change that occurs when the calibration
reference plane is not the same as the measurement plane of the device.

Let's look at an example of a DUT that is mounted on a PCB fixture with SMA
connectors. We can easily calibrate at the SMA connectors. But if we add the
fixture to measure the board-mounted device, the apparent phase of the DUT is
changed by the phase of the PCB fixture. We use port extensions to add a
LINEAR PHASE (constant delay) to the calibration routines to shift the phase
reference plane to that of the DUT. This is ONLY valid if the fixture consists
of a transmission line with linear phase response, and this limitation is
usually met in practice. The main reason that it is NOT met is that there is
mismatch at the SMA-to-PCB interface. This mismatch was not removed with the
error correction because it occurs AFTER the SMA connector. Ripple can be seen
on the display as signals bounce back and forth between the mismatch and the
DUT. If the DUT is well matched, the ripple effect is very small. However,
when we use Automatic Port Extension (APE), and we leave the fixture open (the
DUT removed), the reflection is large and we see larger ripples. That is why
APE uses a curve fitting process to remove the effects of the ripple. For best
effect, the wider the IF Bandwidth, the better we can "smooth-out" the ripples
with curve fitting. Still, we are fitting a LINEAR PHASE SLOPE to the phase
response, and thus we use only a single Port Extension Delay value to
represent the phase slope.

The method used by older VNAs to get this same functionality was to add a
mechanical line stretcher to the reference channel, which removed a fixed
delay amount from the port. Port extensions give 1x the delay for transmission
at each port, and 2x the delay for reflection, so it differs somewhat from
Electrical Delay above, in that the math function depends upon the measurement
being made. The signal passes twice through the fixture for reflection (out
and back), but only once for each port on transmission. For S21, the phase
slope added is the sum of the port 1 and port 2 Port Extension Delay values.

The "User Range" APE function is used in cases where a fixture has limited
bandwidth, perhaps due to tuning elements or bias elements. In this case, the
model of constant delay for the fixture over the whole bandwidth is not valid,
so a narrower "User Range" of frequencies can be selected to compute the
delay. Since the aperture is smaller, there is more uncertainty in the delay
computation for port extension. Also, for those who had been using the [Marker
=>> Delay](../S4_Collect/Markers.htm#functions) function to estimate the
delay, we added the "Active Marker" selection to APE, which works exactly the
same as Marker->Delay. [Learn more about Automatic Port
Extensions.](../S3_Cals/Port_Extensions.htm#AutoPortExtensions)

