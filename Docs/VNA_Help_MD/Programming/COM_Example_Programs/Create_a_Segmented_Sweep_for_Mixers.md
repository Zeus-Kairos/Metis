# Create a Segmented Sweep for Mixers

* * *

This example program shows how to setup a segment sweep in FCA.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as Seg.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

### See Also

[Converter Object](../COM_Reference/Objects/Converter_Object.md)

[See Other COM Example Programs](COM_Example_Intro.md)

option explicit Dim app,chan,conv Set app =
CreateObject("AgilentPNA835x.Application") Set chan = app.ActiveChannel Set
conv = chan.GetConverter app.Reset ' Create FCA Scalar Mixer/Converter channel
with an SC21 measurement: app.CreateCustomMeasurementEx 1, "Scalar
Mixer/Converter", "SC21", 1 ' Delete all existing segments, and create three
new ones conv.DeleteAllSegments() conv.AddSegment 1,3 ' Turn on segment 1
conv.SegmentState(1)=True ' Set segment sweep ' The sweeptype command discards
the changes made to the scratch mixer ' Therefore, precede with Apply ' Also,
always do this before setting the LO port conv.Apply chan.SweepType = 4
'segment sweep ' Setup segment #1 ' Input is swept from 1.1GHz to 1.39GHz
conv.SegmentStartFrequency(1,0)=1.1e9 conv.SegmentStopFrequency(1,0)=1.39e9
'Swept input conv.SegmentRangeMode(1,0)=0 ' Input power is -10 dBm
conv.SegmentFixedPower(1,0)=-10.0 ' LO1 is fixed: 2.2 GHz
conv.SegmentFixedFrequency(1,2)=2.2e9 ' LO1 power is 10.0 dBm
conv.SegmentFixedPower(1,2)=10.0 ' Number of points is 21
conv.SegmentPoints(1)=21 ' Output is swept conv.SegmentRangeMode(1,1)=0 '
Output is low-side conv.SegmentMixingMode(1,1)=0 ' Output is calculated from
input and lo1 conv.SegmentCalculate 1,2 ' Turn on segment 1
conv.SegmentState(1)=True ' Setup segment #2 from 1.40 to 1.49 GHz ' All else
the same conv.SegmentStartFrequency(2,0)=1.4e9
conv.SegmentStopFrequency(2,0)=1.49e9 conv.SegmentRangeMode(2,0)=0
conv.SegmentFixedPower(2,0)=-10.0 conv.SegmentFixedFrequency(2,2)=2.2e9
conv.SegmentFixedPower(2,2)=10.0 conv.SegmentPoints(2)=21
conv.SegmentRangeMode(2,1)=0 conv.SegmentMixingMode(2,1)=0
conv.SegmentCalculate 2,2 conv.SegmentState(2)=True ' Setup segment #3 from
1.50 to 1.59 GHz ' All else the same conv.SegmentStartFrequency(3,0)=1.5e9
conv.SegmentStopFrequency(3,0)=1.59e9 conv.SegmentRangeMode(3,0)=0
conv.SegmentFixedPower(3,0)=-10.0 conv.SegmentFixedFrequency(3,2)=2.2e9
conv.SegmentFixedPower(3,2)=10.0 conv.SegmentPoints(3)=21
conv.SegmentRangeMode(3,1)=0 conv.SegmentMixingMode(3,1)=0
conv.SegmentCalculate 3,2 conv.SegmentState(3)=True ' Mixer Input to be port 1
' Mixer output to Port 2 ' Mixer LO to Port 3 conv.LOName(1)="Port 3" ' Apply
the scratch mixer conv.Apply  
---  
  
* * *

