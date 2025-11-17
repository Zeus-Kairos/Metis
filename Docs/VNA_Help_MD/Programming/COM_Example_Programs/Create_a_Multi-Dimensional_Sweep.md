# Create a Multi-Dimensional Sweep

* * *

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as <filename>.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[MultiDimensionalSweep
Object](../COM_Reference/Objects/MultiDimensionalSweep_Object.htm)

[See other COM Examples](COM_Example_Intro.md)

'Demonstration of multi-dimensional sweep setup.  
set pna = CreateObject("AgilentPNA835x.Application","A-N5242A-10096")  
CreateSAMeasurement  
SetupMultiSweep Sub CreateSAMeasurement  
' Create a B measurement on channel 1  
pna.Channels.RemoveChannelNumber(1)  
call pna.CreateCustomMeasurementEx(1,"Spectrum Analyzer","B")  
set chan = pna.ActiveChannel  
chan.Hold  
End Sub Sub SetupMultiSweep  
set chan = pna.ActiveChannel  
set mdsweep = chan.MultiDimensionalSweep  
set pc = chan.PhaseControl  
set dc = chan.DCStimulus 'Turn Port 1 ON  
chan.SourcePortMode(1) = naSourcePortOn  
'Configure Port 1 frequency start/stop range  
chan.SourcePortStartFrequency(1) = 2e9  
chan.SourcePortStopFrequency(1) = 4e9  
'Set Port 1 frequency domain's order to 3  
mdsweep.SourcePortFrequencyOrder(1) = 3  
'Enable Port 1 frequency domain in multi-dimensional sweep  
mdsweep.SourcePortFrequencyState(1) = 3  
'Configure Port 1 power start/stop range  
chan.StartPowerEx(1) = -5  
chan.StopPowerEx(1) = 5  
'Set Port 1 power domain's order to 5  
mdsweep.SourcePortPowerOrder(1) = 5  
'Enable Port 1 power domain in multi-dimensional sweep  
mdsweep.SourcePortPowerState(1) = 1  
'Configure Port 1 phase start/stop range  
pc.StartPhase(1) = 0  
pc.StopPhase(1) = 270  
'Set Port 1 phase domain's order to 4  
mdsweep.SourcePortPhaseOrder(1) = 4  
'Enable Port 1 phase domian in multi-dimensional sweep  
mdsweep.SourcePortPhaseState(1) = 1 'Turn Port 3 ON  
chan.SourcePortMode(3) = naSourcePortOn  
'Configure Port 3 frequency start/stop range  
chan.SourcePortStartFrequency(3) = 2e9  
chan.SourcePortStopFrequency(3) = 4e9  
'Set Port 3 frequency domain's order to 3  
mdsweep.SourcePortFrequencyOrder(3) = 3  
'Enable Port 3 frequency domain in multi-dimensional sweep  
mdsweep.SourcePortFrequencyState(3) = 3  
'Configure Port 3 power start/stop range  
chan.StartPowerEx(3) = -5  
chan.StopPowerEx(3) = 5  
'Set Port 3 power domain's order to 5  
mdsweep.SourcePortPowerOrder(3) = 5  
'Enable Port 3 power domain in multi-dimensional sweep  
mdsweep.SourcePortPowerState(3) = 1  
'Configure Port 3 phase start/stop range  
pc.StartPhase(3) = 0  
pc.StopPhase(3) = 270  
'Set Port 3 phase domain's order to 4  
mdsweep.SourcePortPhaseOrder(3) = 4  
'Enable Port 3 phase domain in multi-dimensional sweep  
mdsweep.SourcePortPhaseState(3) = 1 'Turn AO1 ON  
dc.State("AO1") = 1  
'Configure AO1 start/stop range  
dc.Start("AO1") = 0  
dc.Stop("AO1") = 2  
'Set AO1's order to 2  
mdsweep.DCOrder("AO1") = 2  
'Enable AO1 in multi-dimensional sweep  
mdsweep.DCState("AO1") = 1 'Set dimension order 3's point count to 3  
mdsweep.DimensionPointCount(3) = 3  
'Set dimension order 3's repeat count to 1  
mdsweep.DimensionRepeatCount(3) = 1  
'Set dimension order 4's point count to 4  
mdsweep.DimensionPointCount(4) = 4  
'Set dimension order 4's repeat count to 1  
mdsweep.DimensionRepeatCount(4) = 1  
'Set dimension order 5's point count to 5  
mdsweep.DimensionPointCount(5) = 5  
'set dimension order 5's repeat count to 1  
mdsweep.DimensionRepeatCount(5) = 1 End Sub  
---

