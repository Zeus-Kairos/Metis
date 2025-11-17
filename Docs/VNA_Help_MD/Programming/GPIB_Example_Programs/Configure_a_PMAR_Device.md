# Configure a PMAR Device

* * *

This VB Script program configures a new Power Meter as Receiver device and
creates a trace using the PMAR.

[Learn more about Power Meter as a
Recevier](../../System/Configure_a_Power_Meter_As_Receiver.htm)

These programs can be run as a macro in the VNA. To do this, copy the code
into a text editor file such as Notepad and save on the VNA hard drive as
PMAR.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also:

[External Device Configuration Commands](../GP-
IB_Command_Finder/SystConfigExternalDevice.htm)

[SCPI Example Programs](SCPI_Example_Programs.md)

' This section gets the VNA application ' starts the scpi parser, and presets
the VNA dim app Set app = CreateObject("AgilentPNA835x.Application") set scpi
= app.ScpiStringParser scpi.parse "*rst" scpi.parse "Syst:conf:edev:add
'newpmar1'" scpi.parse "Syst:conf:edev:dtype 'newpmar1', 'Power Meter'"
scpi.parse "Syst:conf:edev:driver 'pmar', 'AGPM'" scpi.parse
"Syst:conf:edev:ioconfig 'newpmar1', 'gpib0::14::instr'" scpi.parse
"Syst:conf:edev:pmar:sens 'newpmar1', 1" scpi.parse
"Syst:conf:edev:pmar:read:count 'newpmar1', 10" scpi.parse
"Syst:conf:edev:pmar:read:ntolerance 'newpmar1', 0.1" scpi.parse
"Syst:conf:edev:pmar:sens 'newpmar1', 1" scpi.parse "Syst:conf:edev:pmar:fmin
'newpmar1', 100000000" scpi.parse "Syst:conf:edev:pmar:fmax 'newpmar1',
10000000000" scpi.parse "Syst:conf:edev:pmar:flim 'newpmar1', 0" scpi.parse
"Syst:conf:edev:pmar:tabl:rfac 'newpmar1', 100" scpi.parse
"Syst:conf:edev:pmar:tabl:cfac:freq 'newpmar1', 1e9, 2e9, 3e9" scpi.parse
"Syst:conf:edev:pmar:tabl:cfac:data 'newpmar1', 99, 98, 99" scpi.parse
"Syst:conf:edev:pmar:tabl:loss:stat 'newpmar1', 1" scpi.parse
"Syst:conf:edev:pmar:tabl:loss:freq 'newpmar1', 1e9, 2e9, 3e9" scpi.parse
"Syst:conf:edev:pmar:tabl:loss:data 'newpmar1', -1, -2, -3" 'Activate and
enable the PMAR external device scpi.parse "Syst:conf:edev:ioen 'newpmar1', 1"
scpi.parse "Syst:conf:edev:stat 'newpmar1', 1" 'Create a PMAR trace with power
meter connected to port 3 'Use Calc:Par:Def:Ext - NOT CALC:PAR:DEF!!
scpi.parse "CALC:PAR:DEF:EXT 'myPMARTrace', 'newpmar1,3'"  
---  
  
* * *

