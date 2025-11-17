# Create a Wideband Pulsed Measurement using the PNA-X

* * *

This Visual Basic COM example shows you how to configure the PNA-X internal
pulse generators and modulators to make wideband pulsed measurements in pulse
profile mode using the PNA-X.

[Visit the VNA
website](http://na.support.keysight.com/pna/apps/applications.htm) where you
can download a free Wideband Pulsed Application that performs this measurement
on the PNA-X.

[See all COM Pulsed examples](COM_Example_Intro.md#Pulsed)

'Create an VNA Application instance Dim pnaApp As New
AgilentPNA835x.Application 'Create a PathConfiguration instance Dim pathConf
As AgilentPNA835x.PathConfiguration 'Create an PulseGenerator instance Dim
pulseGen As AgilentPNA835x.PulseGenerator 'Create a Channel instance Dim
myChan As AgilentPNA835x.Channel 'Preset PNA-X pnaApp.Preset 'Assign current
active channel to myChan object Set myChan = pnaApp.ActiveChannel 'Let PNA-X
work in CW mode because of doing pulse profile measurement myChan.SweepType =
naCWTimeSweep 'Set CW Freq to 4 GHz myChan.CWFrequency = 4000000000# 'Set IF
Bandwidth to 5 MHz to get the best time resolution myChan.IFBandwidth =
5000000# 'Assign current active channel path configuration to pathConf object
Set pathConf = myChan.PathConfiguration 'Let PNA-X source work in ALC Open
Loop mode myChan.ALCLevelingMode(1) = naALCOpenLoop 'Make the Pulse1 as
modulation pulse to generate Pulsed-RF signal
pathConf.Element("PulseModDrive").Value = "Pulse1" 'Enable pulse modulation at
Source1Out1 path pathConf.Element("Src1Out1PulseModEnable").Value = "Enable"
'Assign current active channel pulse generator to pulseGen object Set pulseGen
= myChan.PulseGenerator 'Internal pulse generator has five channels, 'default
the channel 0 use as internal ADC trigger signal 'Enable channel 0 of internal
pulse generator as trigger signal pulseGen.State(0) = True 'Enable channel 1
of internal pulse generator as modulation signal pulseGen.State(1) = True 'Set
pulse period to 10 us pulseGen.Period = 0.00001 '10 us 'Set pulse width of
channel 0 to 1 us pulseGen.Width(0) = 0.000001 ' 1 us 'Set pulse width of
channel 1 to 5 us pulseGen.Width(1) = 0.000005 '5 us End Sub  
---  
  
* * *

