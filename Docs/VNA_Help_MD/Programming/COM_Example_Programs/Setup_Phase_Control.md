# Set Up Phase Control

* * *

The following VB Script example exercises the COM commands used to setup and
display Phase Sweep measurements.

### See Also

[About Phase Control](../../S1_Settings/Phase_Control.md)

[PhaseControl Object](../COM_Reference/Objects/PhaseControl_Object.md)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as RxLevel.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

'Assume port 1 is connected to port 3 Set pna =
CreateObject("AgilentPNA835x.Application") pna.Preset Set chan =
pna.ActiveChannel chanNum = chan.ChannelNumber 'Create 3 traces: S33,
R3/C(amp),R3/C(phase) pna.CreateMeasurement 1,"S33",3 Set meas1 =
pna.ActiveMeasurement meas1.Format = 4 'Smithchart format
pna.CreateMeasurement 1,"R3/C",3 'Log format Set meas2 = pna.ActiveMeasurement
meas2.Format = 1 'Phase format pna.CreateMeasurement 1,"R3/C",3 Set meas =
pna.ActiveMeasurement meas.Format = 2 'Phase format 'turn on 3 and 1
chan.SourcePortMode(1) = 1 chan.SourcePortMode(3) = 1 chan.SweepType = 5
'Phase sweep Set phase = chan.PhaseControl 'set port3's control parameter to
R3/C phase.PhaseParameter(3) = "R3/C" 'notice the reference port should not
included in the parameter phase.PhaseReferencePort(3) = 1 'Set port3 to PAR
mode phase.PhaseControlMode(3) = 1 'PhaseControlParamter mode
phase.FixedRatioedPower(3) = 3 phase.StartPhase(3) = 0 phase.StopPhase(3) =
180  
---  
  
* * *

