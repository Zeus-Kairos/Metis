# Setup an FCA Segment Sweep

* * *

This example program shows how to setup a segment sweep in FCA.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as FCASeg.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

option explicit dim App, scpi set App =
CreateObject("Agilentpna835x.application") App.Reset ' Create FCA Scalar
Mixer/Converter channel with an SC21 measurement:
App.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter", "SC21", 1 ' Access
the COM SCPI string parser set scpi = App.ScpiStringParser ' Delete all
existing segments, and create three new ones
scpi.Parse("sens:mix:segm:del:all") scpi.Parse("sens:mix:segm:add 3") ' Turn
#1 ON scpi.Parse("sens:mix:segm1:stat on") ' Set segment sweep ' The following
'type:segm' command discards the changes made to the scratch mixer '
Therefore, precede with Apply ' Also, always do this before setting the LO
port scpi.Parse ("sens:mix:apply") scpi.Parse("sens:swe:type segm") ' Setup
segment #1 ' Input is swept: [1.1GHz, 1.39GHz] ' LO1 is fixed: 2.2 GHz '
Output is low-side mixing swept and calculated ' from input and LO1. ' Number
of points is 21 ' Input power is -10 dBm ' LO1 power is 10.0 dBm
scpi.Parse("sens:mix:segm1:inp:freq:star 1.10E9")
scpi.Parse("sens:mix:segm1:inp:freq:stop 1.39E9")
scpi.Parse("sens:mix:segm1:inp:freq:mode swept")
scpi.Parse("sens:mix:segm1:inp:pow -10.0")
scpi.Parse("sens:mix:segm1:lo1:freq:fix 2.2E9")
scpi.Parse("sens:mix:segm1:lo1:freq:mode fixed")
scpi.Parse("sens:mix:segm1:lo1:pow 10.0") scpi.Parse("sens:mix:segm1:poin 21")
scpi.Parse("sens:mix:segm1:outp:freq:sid LOW") scpi.Parse("sens:mix:segm1:stat
on") scpi.Parse("sens:mix:segm1:calc outp") ' Setup segment #2:
scpi.Parse("sens:mix:segm2:inp:freq:star 1.40E9")
scpi.Parse("sens:mix:segm2:inp:freq:stop 1.49E9")
scpi.Parse("sens:mix:segm2:inp:freq:mode swept")
scpi.Parse("sens:mix:segm2:inp:pow -10.0")
scpi.Parse("sens:mix:segm2:lo1:freq:fix 2.2E9")
scpi.Parse("sens:mix:segm2:lo1:freq:mode fixed")
scpi.Parse("sens:mix:segm2:lo1:pow 10.0") scpi.Parse("sens:mix:segm2:poin 21")
scpi.Parse("sens:mix:segm2:outp:freq:sid LOW") scpi.Parse("sens:mix:segm2:stat
on") scpi.Parse("sens:mix:segm2:calc outp") ' Setup segment #3:
scpi.Parse("sens:mix:segm3:inp:freq:star 1.50E9")
scpi.Parse("sens:mix:segm3:inp:freq:stop 1.6E9")
scpi.Parse("sens:mix:segm3:inp:freq:mode swept")
scpi.Parse("sens:mix:segm3:inp:pow -10.0")
scpi.Parse("sens:mix:segm3:lo1:freq:fix 2.2E9")
scpi.Parse("sens:mix:segm3:lo1:freq:mode fixed")
scpi.Parse("sens:mix:segm3:lo1:pow 10.0") scpi.Parse("sens:mix:segm3:poin 21")
scpi.Parse("sens:mix:segm3:outp:freq:sid LOW") scpi.Parse("sens:mix:segm3:stat
off") scpi.Parse("sens:mix:segm3:calc outp") ' Mixer Input to be port 1 '
Mixer output to Port 2 ' Mixer LO to Port 3 scpi.Parse("sens:mix:lo1:name
""Port 3""") ' Apply the scratch mixer scpi.Parse("sens:mix:apply")  
---  
  
* * *

