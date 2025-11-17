# Antenna Measurements

* * *

This topic describes how to setup a Keysight Vector Network Analyzer (VNA) to
make S21 measurements on an array of antennas. Measurements can be made on up
to 100 antenna arrays (Ports) and up to 15 discrete frequencies

### Measurement Sequence

  1. The VNA is set to a start frequency.

  2. As the antenna moves, the VNA responds to each external trigger signal by measuring an antenna port.

  3. When all ports are measured, the VNA increments to the next frequency

  4. Again the VNA measures all ports, and so forth until all ports are measured at all frequencies in the forward direction.

  5. As the antenna begins moving in the opposite direction, the same sequence occurs, except the VNA decrements in frequency until all ports are measured at all frequencies and the VNA is set back to the original start frequency.

Once setup, only external trigger signals are sent to the VNA. After each
trigger, measurement data is stored in internal VNA memory.

### How to set up the VNA

  1. Press Preset

  2. Press Trigger > Main > Trigger Source > External

  3. Press Trigger > Main > Trigger

  4. In the Trigger dialog under Trigger Scope, select Channel

  5. Click OK

Forward Sweep

  1. Press Trace > Trace N > Trace N to add a new trace.

  2. Press Trace > Trace Setup > Measure....

  3. Select S21 then Channel Number 1

  4. Press Trigger > Main > Trigger

  5. In the Trigger dialog under Channel Trigger State, set the Trigger Mode to Point

  6. Click OK

  7. Press Sweep > Main > Sweep Type > Segment Sweep

  8. Click OK

  9. Press Sweep > Segment Table > Insert Segment

  10. Do this 15 times

  11. For each Segment in the Segment table:

     1. Click State:and select ON

     2. Click both START and STOP Frequency: (each new segment ascends in frequency)

     3. Click Points: type Number of Ports (elements)

Reverse sweep

Repeat the following steps for each frequency: (up to 15)

  * Increment the channel number (X) Starting with Channel 2

  * Decrement the frequency (F)

  1. Press Trace > Trace N > Trace N to add a new trace.

  2. Press Trace > Trace Setup > Measure....

  3. Click S21 then Channel Number X

  4. When a window contains four traces, press Trace > Trace Setup > Add Trace > New Trace + Window.

  5. Click OK

  6. Press Trigger > Main > Trigger

  7. In the Trigger dialog under Channel Trigger State, set the Trigger Mode to Point

  8. Click OK

  9. Press Sweep > Main > Sweep Type > Segment Sweep

  10. Click OK

  11. Press Sweep > Segment Table

  12. In the Segment table

     1. Click State:and select ON

     2. Click both START and STOP Frequency F

     3. Click Points: type Number of Ports (elements)

* * *

