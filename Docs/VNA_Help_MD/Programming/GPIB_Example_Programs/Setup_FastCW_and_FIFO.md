## Set Up Fast CW and FIFO

* * *

This example program does the following:

  * Setup an A/R and B/R measurement

  * Turn ON point averaging

  * Set external edge triggering (commented out)

  * Set FIFO and Fast CW

  * Write data into FIFO data buffer

  * Read FIFO data buffer

IMPORTANT \- Because the IFBW is set to 600 kHz, data will NOT be sent to the
FIFO after each acquisition. [Learn
more.](../../IFAccess/FIFO_and_other_Antenna_Features.htm#FastCW)

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as FIFO.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See the SCPI FIFO commands.](../GP-IB_Command_Finder/SystFIFO.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim returnStr Dim app Dim p Dim start Dim complete Dim init Dim finished '
Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set p = app.ScpiStringParser sub
Write (command) if len(returnStr) <> 0 then err.Raise 55,"Write","Query
Unterminated" end if returnStr = p.parse(command) end sub ' sub
WriteIgnoreError(command) returnStr = p.Execute(command) p.Parse("SYST:ERR?")
' clear error queue end sub ' function Read if len(returnStr) = 0 then
err.Raise 55,"Read","Bad read" end if Read = returnStr returnStr = "" end
function ' Setup and measure A/R and B/R Write "SYST:FPRESET" Write "DISP:WIND
ON" Write "CALC:PAR:DEF:EXT 'meas1','A/R1,0'" Write "DISP:WIND:TRACE:FEED
'meas1'" Write "CALC:PAR:DEF:EXT 'meas2','B/R1,0'" Write
"DISP:WIND:TRACE2:FEED 'meas2'" ' Set IFBW to 600 khz (400 thousand
pts/second) Write "SENS:BWID:RES 600khz" ' Point Averaging Count = 1 Write
"SENS:AVER:MODE POINT" Write "SENS:AVER ON" Write "SENS:AVER:COUNT 1" ' Edge
triggering - positive edge 'Write "CONT:SIGN BNC1,TIEPOSITIVE" 'Write
"TRIG:SOUR EXT" 'Write "SENS:SWE:TRIG:POIN ON" ' Setup FIFO and Fast CW count
Write "SENS:SWE:MODE HOLD" Write "SYST:FIFO ON" Write "SYST:FIFO:DATA:CLEAR"
Write "SENS:SWE:TYPE CW" Write "SENS:SWE:TYPE:FACW 1000000"' set the point
count to 1 million Write "SENS:SWE:MODE SING" ' start an asynchronous
acquisition. init = now() ' Gather data 'wait until end of sweep. Timeout
needs to be very large here. Write "*OPC?" ' opcCount = Read() Dim points
Write "SYST:FIFO:DATA:COUNT?" points = Read() msgbox points ' points ==
2000000 ' points = 2million. Took 5 seconds to acquire For I = 0 to 1 ' 2
iterations (2 parameters * 2 sets of 1 million) Dim data Write
"SYST:FIFO:DATA? 1000000" Data = Read() Next 'turn FIFO and FastCW OFF Write
"SYST:FIFO OFF" Write "SENS:SWE:TYPE:FACW 0" finished = now() msgbox "Init ="
& init & vbCrLf & "Done ="& finished  
---  
  
* * *

  

