# Set Up Phase Control

* * *

This VBScript program configures and displays Phase Sweep measurements.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as RxLev.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

### See Also

[Phase Control SCPI commands](../GP-IB_Command_Finder/source.md)

[About Phase Control](../../S1_Settings/Phase_Control.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

'Assume port 1 is connected to port 3 Set pna =
CreateObject("AgilentPNA835x.Application") Set SCPI = PNA.ScpiStringParser
'Create 3 trace S33, R3/C(amp),R3/C(phase) SCPI.Parse("SYST:FPR")
SCPI.Parse("DISP:WIND:STATE ON") SCPI.Parse("CALC:PAR:DEF 'MyMeas1',S33")
SCPI.Parse("DISP:WIND1:TRAC1:FEED 'MyMeas1'") SCPI.Parse("CALC:PAR:SEL
'MyMeas1'") SCPI.Parse("CALC:FORM SMIT") SCPI.Parse("CALC:PAR:DEF
'MyMeas2',R3C,3") SCPI.Parse("DISP:WIND1:TRAC2:FEED 'MyMeas2'")
SCPI.Parse("CALC:PAR:SEL 'MyMeas2'") SCPI.Parse("CALC:FORM MLOG")
SCPI.Parse("CALC:PAR:DEF 'MyMeas3',R3C,3") SCPI.Parse("DISP:WIND1:TRAC3:FEED
'MyMeas3'") SCPI.Parse("CALC:PAR:SEL 'MyMeas3'") SCPI.Parse("CALC:FORM PHAS")
SCPI.Parse("SENS:SWE:TYPE PHAS") 'turn on 3 and 1 SCPI.Parse("SOUR:POW1:MODE
ON") SCPI.Parse("SOUR:POW3:MODE ON") 'set port3's control parameter to R3/C
SCPI.Parse("SOUR:PHAS3:PAR 'R3/C'") 'Set port3 to PAR mode
SCPI.Parse("SOUR:PHAS3:PAR:MODE PAR") SCPI.Parse("SOUR:PHAS3:PAR:PORT 1")
SCPI.Parse("SOUR:PHAS3:POFF:FIX 3") SCPI.Parse("SOUR:PHAS3:STAR 0")
SCPI.Parse("SOUR:PHAS3:STOP 180")  
---  
  
* * *

  

