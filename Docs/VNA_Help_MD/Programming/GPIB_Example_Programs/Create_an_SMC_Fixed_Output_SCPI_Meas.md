# Create an SMC Fixed Output Measurement

* * *

This VB Script example creates a calibrated SMC fixed output measurement using
an external, controlled LO. Then a single sweep is taken and data is
retrieved. The external LO is NOT required when using the internal second VNA
source for the LO.

Requirements:

  * The external LO should be configured to match the SENS:MIX:LO:NAME command below.

Fixed output measurements require that an external LO source be swept and
synchronized with the VNA source. FCA performs this synchronization using the
external source configuration settings. See [Configure an External
Source](Configure_an_External_Source.htm) using SCPI.

The fastest, and recommended, method of controlling the LO source is [Hardware
List (BNC) triggering
mode](../../System/Configure_an_External_Device.htm#ext_source_config).
However, in this mode, FCA channels will not respond to manual triggers.
Therefore, the example uses the following mechanism to trigger a sweep:

Write "SENS:SWE:MODE HOLD" 'place channel 1 in HOLD mode  
Write "INIT:CONT ON" 'place VNA in internal trigger mode  
Write "SENS:SWE:MODE SINGle  
Write "*OPC?" 'wait until the sweep is complete  
Read

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You can run a VBScript (*.vbs) program from the VNA [using
Macros.](../Using_Macros.htm) To run this program, copy the following code
into a text editor and save it as a *.vbs file.

option explicit ' Setup infrastructure to use the SCPI over COM dim app set
app = createobject("Agilentpna835x.application") dim p set p =
app.scpistringparser dim returnStr sub Write (command) if len(returnStr) <> 0
then err.Raise 55,"Write","Query Unterminated" end if returnStr =
p.parse(command) end sub sub WriteIgnoreError(command) returnStr =
p.Execute(command) p.Parse("SYST:ERR?") ' clear error queue end sub function
Read if len(returnStr) = 0 then err.Raise 55,"Read","Bad read" end if Read =
returnStr returnStr = "" end function Write "SYST:PRES" ' When programming in
remote mode, hold mode is recommended Write "SENS:SWE:MODE HOLD" ' Delete the
standard measurement Write "CALC:PAR:DEL:ALL" ' Create an SC21 measurement
Write "CALC:CUST:DEF 'MySC21', 'Scalar Mixer/Converter', 'SC21'" Write
"DISP:WIND:TRACE:FEED 'MySC21'" Write "CALC:PAR:SEL 'MySC21'" ' Set number of
points to 11 Write "SENS:SWE:POIN 11" ' Setup the mixer parameters for a swept
LO, fixed output measurement Write "SENS:MIX:INP:FREQ:START 200e6" Write
"SENS:MIX:INP:FREQ:STOP 700e6" Write "SENS:MIX:LO:FREQ:MODE Swept" Write
"SENS:MIX:OUTPUT:FREQ:FIX 3.4e9" Write "SENS:MIX:OUTP:FREQ:SID HIGH" Write
"SENS:MIX:CALC LO_1" Write "SENS:MIX:INP:POW -17" Write "SENS:MIX:LO:POW 10"
Write "SENS:MIX:APPLY ' Specify the LO name, for controlled LO. ' This name is
setup in the External Source Config Dialog Write "SENS:MIX:LO:NAME '8360'"
Write "SENS:MIX:APPLY ' Create an S11 in the same channel Write "CALC:CUST:DEF
'MyS11', 'Scalar Mixer/Converter', 'S11'" Write "DISP:WIND:TRACE2:FEED
'MyS11'" Write "CALC:PAR:SEL 'MyS11'" ' Create an IPwr in the same channel
Write "CALC:CUST:DEF 'MyIPwr', 'Scalar Mixer/Converter', 'IPwr'" Write
"DISP:WIND:TRACE3:FEED 'MyIPwr'" Write "CALC:PAR:SEL 'MyIPwr'" ' Create an
OPwr in the same channel Write "CALC:CUST:DEF 'MyOPwr', 'Scalar
Mixer/Converter', 'OPwr'" Write "CALC:PAR:SEL 'MyOPwr'" Write
"DISP:WIND:TRACE4:FEED 'MyOPwr'" ' Perform a single sweep, synchronously. When
*OPC returns, the sweep is done Write "SENS:SWE:MODE SINGle" Write "*OPC?"
Read ' Retrieve the SC21 data Write "CALC:PAR:SEL 'MySC21'" Write "CALC:DATA?
SDATA" dim data data = Read() wscript.echo("SC21=" & data) 'Retrieve the S11
data Write "CALC:PAR:SEL 'MyS11'" Write "CALC:DATA? SDATA" data = Read()
wscript.echo("S11=" & data)  
---  
  
* * *

* * *

