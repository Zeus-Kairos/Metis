# Set Up PNOP and PSAT Marker Search

* * *

This example program does the following:

  * Sets up measurement for either PNOP or PSAT marker search

  * Sets parameters for search

  * Reads a parameter for each

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SearchMkr.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See Other COM Example Programs](COM_Example_Intro.md)

Set app = CreateObject("AgilentPNA835X.Application") app.Preset set meas =
app.activemeasurement 'View Power Out vs Power In meas.ChangeParameter "B",1
'perform power sweep set chan = app.ActiveChannel chan.SweepType = 2
chan.StartPower = -5 chan.StopPower = 0 '\-------------------- 'Choose marker
search resp=Msgbox ("PNOP (yes) or PSAT (no)" , 4, "PNA Marker Search Demo")
if resp=6 then PNOP1() Else PSAT1() End If '\-------------------- 'PSAT marker
search Sub PSAT1() set psat = meas.PSaturation psat.PMaxBackOff = .3
psat.SearchPowerSaturation 'Read PSAT Parameter dim answer
answer=psat.GainSaturation wscript.echo("Gain Sat: "& answer) End Sub
'\-------------------- 'PNOP marker search Sub PNOP1() set pnop = meas.PNOP
pnop.BackOff = 2 pnop.PinOffset = 1 pnop.SearchPowerNormalOperatingPoint 'Read
PNOP Parameter dim answer answer=pnop.Gain wscript.echo("PNOP Gain: "& answer)
End Sub  
---  
  
* * *

