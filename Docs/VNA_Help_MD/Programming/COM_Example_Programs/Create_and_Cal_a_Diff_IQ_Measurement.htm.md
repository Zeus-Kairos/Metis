# Create a Differential IQ Measurement

* * *

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as DIQ.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

### See Also

[DIQ Object](../COM_Reference/Objects/DIQ_Object.md)

[See other COM Examples](COM_Example_Intro.md)

Set app = CreateObject("AgilentPNA835x.Application")
app.CreateCustomMeasurementEx 2, "Differential I/Q", "IPwrF1" Set Diq =
app.ActiveChannel.CustomChannelConfiguration Diq.AddRange
Diq.RangeStartFrequency(1) = 1e9 Diq.RangeStopFrequency(1) = 2e9
Diq.RangeCoupleState(2) = 1 Diq.RangeCoupleId(2)=1 Diq.RangeMultiplier(2) = 2
Diq.RangeIFBW(2) = 1000 Diq.SourceRange("Port 1") = 1 Diq.SourceState("Port
1") = naPortON Diq.MatchState("Port 1") = 1 Diq.MatchFrequencyRange("Port 1")
= 1 Diq.MatchTestReceiver("Port 1") = "b3" Diq.MatchRefReceiver("Port 1") =
"a3" Diq.PowerSweepState("Port 1")=0 Diq.PortStartPower("Port 1")=-5
Diq.PortAttenuator("Port 1") = 5 Diq.AutoRangeState("Port 1") = 1  
---

