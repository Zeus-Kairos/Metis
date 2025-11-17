# Active (Hot) Parameters

This program can be run as a macro in the PNA. To do this, copy the code into
a text editor file such as Notepad and save on the PNA hard drive as
<filename>.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also:

[Active Parameters Commands](../GP-IB_Command_Finder/Sense/XMatch.md)

[SCPI Example Programs](SCPI_Example_Programs.md)

'Demonstration of Active Parameters setup.  
Dim app  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser scpi.Parse "SYST:FPR"  
scpi.Parse "CALC:CUST:DEF 'mytrace', 'Active Parameters', 'IPwr' "  
scpi.Parse "DISP:WIND ON"  
scpi.Parse "DISP:WIND:TRAC:FEED 'mytrace'" scpi.Parse "SENS:ACT:SWE:TYPE MULT"
'Sweep type to multi sweep  
scpi.Parse "SENS:ACT:SWE:POW:STAR -15" 'Start power -15dBm  
scpi.Parse "SENS:ACT:SWE:POW:STOP 0" 'Stop power 0dBm  
scpi.Parse "SENS:ACT:SWE:POW:STEP 4" '4 steps with -15,-10,-5,0dBm scpi.Parse
"SENS:ACT:DISP:TRAC1:IPW -5" 'Set the display as the -5dBm input  
---

