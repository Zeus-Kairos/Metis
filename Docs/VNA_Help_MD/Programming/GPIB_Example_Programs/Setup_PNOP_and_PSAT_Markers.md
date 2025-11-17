# Set Up PNOP and PSAT Marker Search

* * *

This example program does the following:

  * Sets up measurement for either PNOP or PSAT marker search

  * Sets parameters for search

  * Reads a parameter for each

See [PNOP](../GP-IB_Command_Finder/Calculate/MarkerPNOP.md) and [PSAT](../GP-
IB_Command_Finder/Calculate/MarkerPSAT.htm) SCPI commands.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SearchMkr.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Set app = CreateObject("AgilentPNA835X.Application") Dim scpi set scpi
= app.ScpiStringParser scpi.Execute ("SYST:FPReset") ' View Power Out vs Power
In ' Create and turn on window/channel 1 scpi.Execute ("DISPlay:WINDow1:STATE
ON") 'Define a measurement name, parameter scpi.Execute
("CALCulate1:PARameter:DEFine:EXT 'MyMeas','B,1'") 'Associate ("FEED") the
measurement name ('MyMeas') to WINDow (1) scpi.Execute
("DISPlay:WINDow1:TRACe1:FEED 'MyMeas'") scpi.Execute
("CALCulate1:PARameter:SELect 'MyMeas'") 'perform power sweep scpi.Execute
("SENSe1:SWEep:TYPE POWer") scpi.Execute ("SOURce1:POWer:STARt -5")
scpi.Execute ("SOURce1:POWer:STOP 0") '\-------------------- 'Choose marker
search resp=Msgbox ("PNOP (yes) or PSAT (no)" , 4, "PNA Marker Search Demo")
if resp=6 then PNOP1() Else PSAT1() End If '\-------------------- 'PSAT marker
search Sub PSAT1() scpi.Execute ("CALCulate1:MARKer:PSATuration:BACKoff 2")
'Read PSAT Parameter dim answer answer=scpi.Execute
("CALCulate1:MARKer:PSATuration:GAIN?") wscript.echo("Gain Sat: "& answer) End
Sub '\-------------------- 'PNOP marker search Sub PNOP1() scpi.Execute
("CALCulate1:MARKer:PNOP:BACKoff 2") scpi.Execute
("CALCulate1:MARKer:PNOP:POFFset 1") 'Read PNOP Parameter dim answer
answer=scpi.Execute ("CALCulate1:MARKer:PNOP:GAIN?") wscript.echo("PNOP Gain:
"& answer) End Sub  
---  
  
* * *

