# Set Up an Embedded LO Measurement

* * *

This VBScript example creates a Noise Figure Converter measurement for a
converter with an Embedded LO.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Noise.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

option explicit dim app dim chan dim host set app =
CreateObject("Agilentpna835x.application") app.reset ' create NFX traces
app.CreateCustomMeasurementEx 1, "Noise Figure Converters", "NF", 1
app.CreateCustomMeasurementEx 1, "Noise Figure Converters", "SC21", 1 'set
channel and application objects set chan = app.ActiveChannel dim nfx set nfx =
chan.CustomChannelConfiguration dim converter set converter =
chan.GetConverter() dim calMgr set calMgr = app.GetCalManager dim nfxCal set
nfxCal = CalMgr.CreateCustomCalEx(1) dim nfxCalExt set nfxCalExt =
nfxCal.CustomCalConfiguration dim ELO set ELO = converter.ConverterEmbeddedLO
' Set embedded LO properties ELO.NormalizePoint = 101 ELO.TuningMode = 0 '
Broadband and precise ELO. TuningIFBW = 3.0e4 ELO.MaxPreciseTuningIterations =
5 ELO.PreciseTuningTolerance = 1 ELO.TuningSweepInterval = 1 ELO.IsOn = true
'The following single sweep performs the same 'function as "Find Now" on the
ELO dialog chan.Single 1  
---  
  
* * *

