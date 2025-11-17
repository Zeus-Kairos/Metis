# Create a Differential I/Q Measurement

* * *

This example program creates a Differential I/Q measurement setup.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
DIQ.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See the Differential I/Q commands.](../GP-IB_Command_Finder/Sense/DIQ.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' This section gets the VNA application ' starts the scpi parser, and presets
the VNA Set app = CreateObject("AgilentPNA835x.Application") Set scpi=
app.ScpiStringParser scpi.Parse "SYST:FPR" scpi.Parse "CALC:CUST:DEF
'mytrace','Differential I/Q','IPwrF1'" scpi.Parse "DISP:WIND ON" scpi.Parse
"DISP:WIND:TRAC:FEED 'mytrace'" scpi.Parse "SENS:DIQ:FREQ:RANG:ADD" scpi.Parse
"SENS:DIQ:FREQ:RANG1:STARt 1e9" scpi.Parse "SENS:DIQ:FREQ:RANG1:STOP 2e9"
scpi.Parse "SENS:DIQ:FREQ:RANG2:COUP:STATe ON" scpi.Parse
"SENS:DIQ:FREQ:RANG2:COUP:ID 1" scpi.Parse "SENS:DIQ:FREQ:RANG2:COUP:MULT 2"
scpi.Parse "SENS:DIQ:PORT1:RANG 1" scpi.Parse "SENS:DIQ:PORT1:STATe ON"
scpi.Parse "SENS:DIQ:PORT1:MATC:CORR:STATe ON" scpi.Parse
"SENS:DIQ:PORT1:MATC:CORR:RANGe 'F1'" scpi.Parse
"SENS:DIQ:PORT1:MATC:CORR:TREC 'b3'" scpi.Parse "SENS:DIQ:PORT1:MATC:CORR:RREC
'a3'" scpi.Parse "SENS:DIQ:PORT1:POW:SWE:STATe OFF" scpi.Parse
"SENS:DIQ:PORT1:POW:STARt -5" scpi.Parse "SENS:DIQ:PORT:POW:ATT 5" scpi.Parse
"SENS:DIQ:PORT:POW:ATT:AUTO ON"  
---

