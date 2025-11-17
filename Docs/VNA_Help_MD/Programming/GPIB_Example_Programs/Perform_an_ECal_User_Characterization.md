## Perform an ECal User Characterization

* * *

This example performs a user-characterization and stores it to both the ECal
module memory and VNA disk memory. It also demonstrates the use of the EXPort,
CLEar, IMPort and KNAMe:INF? commands.

It then performs two 2-port cals: the first using the characterization from
module memory, then using the characterization from disk memory.

Note: This example requires that channel 1 be already calibrated.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as ECal.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See all ECal User Characterization SCPI commands](../GP-
IB_Command_Finder/Sense/ECalCharacterize.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Option Explicit Dim pna Set pna = CreateObject("AgilentPNA835x.Application")
Dim scpi Set scpi = pna.ScpiStringParser ' Substitute here the model number
and serial number of your own ECal. ' Note that this example corresponds to a
4-port ECal module with ' serial number 00001. If you have a 2-port ECal
module, their model ' numbers are '5x5' numbers -- for example, 'N4691-60001'.
Dim ecalModelNum ecalModelNum = "N4433A" Dim ecalSerialNum ecalSerialNum =
"00001" scpi.Parse "SENS1:CORR:CKIT:ECAL:CHAR:ID '" & ecalModelNum & "," &
ecalSerialNum & "'" MsgBox "ECal module to be characterized is: " &
scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:ID?") ' Set which user characterization
number (1-12) the new characterization ' will be stored to in the ECal module
when it is done. If you intend to ' store your user characterization just to
VNA Disk Memory and NOT the ' ECal module's memory, then omit this command.
Dim characterizationNumber characterizationNumber = 1 scpi.Parse
"SENS1:CORR:CKIT:ECAL:CHAR:CNUM " & CStr(characterizationNumber) ' The
following commented-out lines of code show how you can access ' the list of
connector type names you can set for the ports of an ' ECal when you user-
characterize it. However, please note that if ' you are writing the user
characterization to the ECal module's memory, ' as of yet only the Factory
Defined set of connector choices will work ' properly (see
[SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT?](../GP-
IB_Command_Finder/Sense/ECalCharacterize.htm#ConnCat)). If you will be saving
' your characterization to just VNA Disk Memory only, then all connector '
names returned by this query will work, ' user-defined connector names as well
as factory-defined. 'Dim connTypeList 'connTypeList =
scpi.Parse("SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT?") 'MsgBox connTypeList ' For
each port of the ECal module, specify which connector type ' is at the end of
the adapter (or cable or fixture) that is ' connected to that port of the ECal
for the characterization ' (must be one of the connector types that is
included in the ' list that "SENS:CORR:CKIT:ECAL:CHAR:CONN:CAT?" returns). The
' default is "No adapter", which assumes you are characterizing that ' port of
the ECal "as is" (nothing attached to it). So in this ' example, Ports C and D
of the ECal are being characterized to just ' the ECal's connectors.
scpi.Parse "SENS1:CORR:CKIT:ECAL:CHAR:CONN:PORT1 'APC 3.5 male'" ' ECal Port A
scpi.Parse "SENS1:CORR:CKIT:ECAL:CHAR:CONN:PORT2 'APC 3.5 male'" ' ECal Port B
' As with the connector types, the information set in these next ' few
properties also gets stored within the characterization. ' Set the name of the
person and/or company that is producing ' this characterization. scpi.Parse
"SENS1:CORR:CKIT:ECAL:CHAR:DESC:USER 'John Doe, Acme Inc.'" ' Set user-
specified description of the VNA being used. scpi.Parse
"SENS1:CORR:CKIT:ECAL:CHAR:DESC:VNA 'SN US12345678'" ' Set descriptions of
what you have connected to the ECal module's ' ports for the characterization.
' Port A of the ECal scpi.Parse "SENS1:CORR:CKIT:ECAL:CHAR:DESC:PORT1 '3.5 mm
adapter, SN 00001'" ' Port B of the ECal scpi.Parse
"SENS1:CORR:CKIT:ECAL:CHAR:DESC:PORT2 '3.5 mm adapter, SN 00002'" ' Note that
the "SENS:CORR:CKIT:ECAL:CHAR:" INITiate, ACQuire and SAVE ' ("CHAR:SAVE" but
not "CHAR:DMEMory:SAVE") commands can all each take a significant ' amount of
time to execute/complete. If you are looking at this example to ' leverage
this functionality into a SCPI via GPIB or SCPI via SICL-LAN ' (VXI-11.2/11.3)
application, then you could issue the "*CLS" and "*ESE 1" commands ' as shown
in the commented-out lines below, and use your I/O libraries' Serial Poll '
function to repeatedly read the status byte until you detect bit 5 (weight of
32) ' in that byte is set. That will happen when the command you are pairing
with ' ";*OPC" has completed its operation. But that technique only works for
the GPIB ' and SICL-LAN interfaces. If you need to use the TCPIP Socket or COM
' ScpiStringParser (as is used in this example) SCPI interfaces where there's
' no "built-in" Serial Poll type of function, to ensure your program operates
in a ' synchronized manner it will need to wait on the "*OPC?" reply (and not
time out) ' before proceeding to the next line of your program. In that event,
we recommend ' you execute these commands on a thread of execution separate
from your program's ' user interface thread. ' Of the
"SENS:CORR:CKIT:ECAL:CHAR:" INITiate, ACQuire and SAVE commands, the SAVE '
command takes the longest amount of time to complete (unless you've set up
your ' measurement channel to have a very slow sweep time, in which case the
ACQuire ' command could take longer). For an ECal that is a N469x, N4432A or
N4433A, or an ' 8509x or N4431x produced by Keysight in 2005 or later, the
SAVE command can take a ' maximum of approximately 4 to 5 minutes to complete
(that corresponds to a ' characterization that will result in the ECal's
memory becoming completely filled). ' For an 8509x or N4431x ECal that was
produced in 2004 or earlier, the SAVE command ' can take a maximum of 9 to 10
minutes to complete (again that corresponds to a ' characterization that will
result in the ECal's memory becoming completely full). ' Begin a user
characterization on Channel 1. ' If you will be storing this characterization
to the ECal module's memory, then ' the boolean argument to this command is
optional (but if you choose to include it ' for that case then you must
specify it as 1 or ON). If you will be storing this ' characterization to VNA
disk memory ONLY, then you should specify 0 or OFF for ' that argument. In
this example we will be storing the characterization to both ' module memory
and VNA disk memory, so we can just omit the argument and let it ' default to
1. scpi.Parse "SENS1:CORR:CKIT:ECAL:CHAR:INIT" Dim numSteps numSteps = CLng(
scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:STEP?") ) Dim opcReply 'Dim statusByte '
Measure the steps. ' Note: prior to measuring the steps you must already have
a calibration of the ' necessary number of ports applied to the channel (which
in this example is Channel 1). ' Otherwise an error will be reported to the
SCPI error queue. Dim i For i = 1 To numSteps ' Display the step's
description. MsgBox scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:DESC? " & i) ' Clear
the instrument's Status Byte. ' scpi.Execute "*CLS" ' Enable for the OPC bit
(bit 0, which has weight 1) in the instrument's ' Event Status Register, so
that when that bit's value transitions from 0 to 1 ' then the Event Status
Register bit in the Status Byte (bit 5 of that byte, ' weight 32) will become
set. ' scpi.Execute "*ESE 1" ' Issue the ACQuire command opcReply =
scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:ACQ STAN" & CStr(i) & ";*OPC?") '
scpi.Execute "SENS1:CORR:CKIT:ECAL:CHAR:ACQ STAN" & CStr(i) & ";*OPC" ' Do '
here is where if you leverage this example into an environment where ' you are
using SCPI via GPIB or SICL-LAN, that in this loop you could do a ' Serial
Poll via that interface to read the status byte into this ' statusByte
variable. Then this If statement would detect when bit 5 is set. ' If (
(statusByte/32) Mod 2) Then Exit Do ' And note that normally you would want to
have your program do some other ' processing (for example, check for user
input from keyboard/mouse, for ' a cancellation request) here in this loop. '
Loop MsgBox "ACQuire is complete" Next MsgBox "Now the user characterization
will be saved to the ECal module and to PNA disk memory" 'scpi.Execute
"*CLS;*ESE 1" ' Save the user characterization to the ECal module's memory.
opcReply = scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:SAVE;*OPC?") 'scpi.Execute
"SENS1:CORR:CKIT:ECAL:CHAR:SAVE;*OPC" 'Do ' again here you could do a Serial
Poll to get statusByte if using GPIB or SICL-LAN ' If ( (statusByte/32) Mod 2)
Then Exit Do 'Loop ' Save the user characterization to VNA Disk Memory. Dim
characterizationName characterizationName = "test" opcReply =
scpi.Parse("SENS1:CORR:CKIT:ECAL:CHAR:DMEM:SAVE '" & characterizationName &
"';*OPC?") Dim pnaDiskMemCalKitName pnaDiskMemCalKitName =
GetCalKitName(characterizationName) ' Exporting the characterization from VNA
disk memory into a file. ' The file can be used for loading the
characterization into VNA disk memory on another VNA. scpi.Parse
"SENS:CORR:CKIT:ECAL:EXP '" & pnaDiskMemCalKitName & "'" ' Demonstrating that
the characterization can be cleared from VNA disk memory and ' then re-loaded
(IMPorted) from the file that was created by the '"SENS:CORR:CKIT:ECAL:EXP".
scpi.Parse "SENS:CORR:CKIT:ECAL:DMEM:CLE '" & pnaDiskMemCalKitName & "'"
scpi.Parse "SENS:CORR:CKIT:ECAL:DMEM:IMP 'C:/Program Files/Keysight/Network
Analyzer/ECal User Characterizations/" & pnaDiskMemCalKitName & ".euc'" Dim
moduleMemCalKitName moduleMemCalKitName = GetCalKitName("User " &
CStr(characterizationNumber)) MsgBox "Information about the characterization
from ECal module memory = " & scpi.Parse("SENS:CORR:CKIT:ECAL:KNAM:INF? '" &
moduleMemCalKitName & "'") MsgBox "Information about the characterization from
PNA disk memory = " & scpi.Parse("SENS:CORR:CKIT:ECAL:KNAM:INF? '" &
pnaDiskMemCalKitName & "'") MsgBox "User characterization is complete. Now we
will calibrate using it. First we will use it from ECal module memory."
DoTwoPortCal moduleMemCalKitName MsgBox "Now we will calibrate using the
characterization from PNA Disk Memory." DoTwoPortCal pnaDiskMemCalKitName
MsgBox "Example has completed" ' Function GetCalKitName(characterizationName)
Dim calKitName calKitName = ecalModelNum If Len(characterizationName) > 0 Then
calKitName = calKitName & " " & characterizationName calKitName = calKitName &
" ECal " & ecalSerialNum GetCalKitName = calKitName End Function Sub
DoTwoPortCal(calKitName) ' Specify the DUT connector for each VNA port to be
calibrated (DUT connector = ECal characterization's connector) scpi.Parse
"SENS1:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'" scpi.Parse
"SENS1:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" ' Specify the "cal kit" for
each of those ports scpi.Parse "SENS1:CORR:COLL:GUID:CKIT:PORT1 '" &
calKitName & "'" scpi.Parse "SENS1:CORR:COLL:GUID:CKIT:PORT2 '" & calKitName &
"'" ' This results in a calibration sequence of a single "connection step"
scpi.Parse "SENS1:CORR:COLL:GUID:INIT" ' Acquire the cal connection step
opcReply = scpi.Parse("SENS1:CORR:COLL:GUID:ACQ STAN1;*OPC?") ' Again here
instead of waiting for opcReply you could do a Serial Poll to get statusByte
if using GPIB or SICL-LAN 'scpi.Execute "SENS1:CORR:COLL:GUID:ACQ STAN1;*OPC"
'Do ' If ( (statusByte/32) Mod 2) Then Exit Do 'Loop ' Conclude the cal and
turn it on scpi.Parse "SENS1:CORR:COLL:GUID:SAVE" End Sub  
---  
  
* * *

