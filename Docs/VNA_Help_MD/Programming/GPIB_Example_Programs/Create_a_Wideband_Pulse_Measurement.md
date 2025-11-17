# Create a Wideband Pulsed Measurement using the PNA-X

* * *

This Visual Basic example shows you how to configure the PNA-X internal pulse
generators and modulators to make wideband pulsed measurements in pulse
profile mode using the PNA-X.

[Visit the VNA
website](http://na.support.keysight.com/pna/apps/applications.htm) where you
can download a free Wideband Pulsed Application that performs this measurement
on the PNA-X.

[See all SCPI Pulsed examples](SCPI_Example_Programs.md)

Private Sub Form_Load() Dim app Dim scpi ' Create / Get the VNA application.
Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser 'Preset the analyzer scpi.Execute ("*RST") 'Set BW to 5
MHz scpi.Execute ("[SENS:BWID](../GP-
IB_Command_Finder/Sense/Sense_Bandwidth.htm#res) 5MHZ") 'Set sweep type to CW
mode scpi.Execute ("[SENS:SWE:TYPE](../GP-
IB_Command_Finder/Sense/Sweep_SCPI.htm#ssty) CW") 'Delete S11 trace
scpi.Execute ("[DISP:WIND:TRAC1:DEL](../GP-
IB_Command_Finder/Display.htm#tdel)") 'Create S21 trace scpi.Execute
("[CALC:PAR:DEF:EXT](../GP-
IB_Command_Finder/Calculate/Parameter.htm#DefineExtend) 'MyMeas',S21")
scpi.Execute ("[DISP:WIND:TRAC1:FEED](../GP-
IB_Command_Finder/Display.htm#dwtf) 'MyMeas'") 'Set modulation source to
Pulse1 scpi.Execute
("[sens:path:conf:elem](../../IFAccess/IF_Path_Configuration.md#elements)
'PulseModDrive','Pulse1'") 'Set power leveling mode to Openloop scpi.Execute
("[sour:pow1:alc:mode](../GP-IB_Command_Finder/source.md#ALCMode) open")
'Enable pulse modulator 1 scpi.Execute ("sens:path:conf:elem
'Src1Out1PulseModEnable','Enable'") 'Set clock of internal pulse generator to
internal scpi.Execute ("sens:path:conf:elem 'PulseTrigInput','Internal'")
'Turn on Pulse0 scpi.Execute ("[SENS:PULS0:STAT](../GP-
IB_Command_Finder/Sense/Pulse.htm#state) 1") 'Turn on Pulse1 scpi.Execute
("SENS:PULS1:STAT 1") 'Set pulse period to 1 ms scpi.Execute
("[sens:puls:per](../GP-IB_Command_Finder/Sense/Pulse.md#period) .001") 'Set
Pulse1 width to 10 us scpi.Execute ("[sens:puls1:width](../GP-
IB_Command_Finder/Sense/Pulse.htm#width) 0.00001") 'Set Pulse1 delay to 8 us
scpi.Execute ("[sens:puls1:delay](../GP-
IB_Command_Finder/Sense/Pulse.htm#delay) 0.000008") 'Set Pulse0 width to 1 us
scpi.Execute ("sens:puls0:width 0.000001") 'Set Pulse0 delay to 400 ns
scpi.Execute ("sens:puls0:delay 0.0000004") 'Set trigger scope to Channel
scpi.Execute ("[TRIG:SCOP](../GP-IB_Command_Finder/Trigger_SCPI.md#tssc)
CURRENT") End Sub  
---

