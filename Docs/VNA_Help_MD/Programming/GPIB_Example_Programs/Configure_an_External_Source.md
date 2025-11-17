# Configure an External Source

* * *

This VB Script program configures an External Source.

[Learn more about External Source
Configuration](../../System/Configure_an_External_Device.htm)

These programs can be run as a macro in the VNA. To do this, copy the code
into a text editor file such as Notepad and save on the VNA hard drive as
ExtSource.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

#### See Also:

[External Device Configuration Commands](../GP-
IB_Command_Finder/SystConfigExternalDevice.htm)

[SCPI Example Programs](SCPI_Example_Programs.md)

' Get the VNA application, and ' start the scpi parser, and preset the VNA dim
app Set app = CreateObject("AgilentPNA835x.Application") set scpi =
app.ScpiStringParser scpi.parse "*rst" Configure the external source
scpi.parse "Syst:conf:edev:add 'newSource'" scpi.parse "Syst:conf:edev:dtype
'newSource', 'Source'" scpi.parse "Syst:conf:edev:driver 'newSource', 'AGMXG'"
scpi.parse "Syst:conf:edev:ioconfig 'newSource', 'gpib0::16::instr'" 'Activate
and enable the external source scpi.parse "Syst:conf:edev:ioen 'newSource', 1"
'State activates and talks to the device if "Syst:conf:edev:ioen" is enabled
scpi.parse "Syst:conf:edev:stat 'newSource', 1"  
---  
  
* * *

