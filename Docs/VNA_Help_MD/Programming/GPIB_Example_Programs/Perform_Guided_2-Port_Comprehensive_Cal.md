# Perform a Guided Calibration using SCPI

* * *

This VBScript program performs a Guided Calibration using ECal or Mechanical
standards. This example includes optional ECal orientation features.

This example has been updated to include:

  * Guided Power Cal (Oct 8, 2010)

  * The setting of Unknown Thru or Adapter Removal adapter delay. (March 2006).

  * The activation of a channel to be calibrated. (Aug. 2006).

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Guided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

' Performing a Guided 2-port cal (Ports 1 and 2) TwoPortGuidedCal Sub
TwoPortGuidedCal Dim app Dim scpi Dim connList Dim selectedConn1,
selectedConn2 Dim kitList Dim selectedKit Dim message ' Create / Get the VNA
application. Set app = CreateObject("AgilentPNA835x.Application") Set scpi =
app.ScpiStringParser 'The following demonstrates that the Active Channel is
cal'd 'Preset the VNA scpi.Execute "SYST:UPR" 'Create a new measurement on
Chan 2 'Now there are two windows, channels and measurements 'This becomes the
Active Measurement scpi.Execute ("DISPlay:WINDow2:STATE ON") 'Define a
measurement name, parameter scpi.Execute ("CALCulate2:PARameter:DEFine:EXT
'MyMeas',S21") '"FEED" the measurement scpi.Execute
("DISPlay:WINDow2:TRACe1:FEED 'MyMeas'") 'This is the Active Measurement
'Activate the 'Preset' measurement to cal chan 1 scpi.Execute ("CALC1:PAR:SEL
'CH1_S11_1'") ' Query the list of connectors that the VNA system recognizes
connList = scpi.Execute("sens:corr:coll:guid:conn:cat?") ' Format the list
with linefeed characters in place of the commas connList =
FormatList(connList) message = "Enter your DUT connector for Port 1. Choose
from this list:" message = message & Chr(10) & Chr(10) & connList ' Select the
connector for Port 1 selectedConn1 = InputBox(message) If selectedConn1 = ""
Then Exit Sub scpi.Execute "sens:corr:coll:guid:conn:port1 '" & selectedConn1
& "'" message = "Enter your DUT connector for Port 2. Again, choose from this
list:" message = message & Chr(10) & Chr(10) & connList ' Select the connector
for Port 2 selectedConn2 = InputBox(message) If selectedConn2 = "" Then Exit
Sub scpi.Execute "sens:corr:coll:guid:conn:port2 '" & selectedConn2 & "'" '
Note: If your VNA has more than 2 ports, then uncomment ' one or both of these
next two lines. 'scpi.Execute "sens:corr:coll:guid:conn:port3 ""Not used"" "
'scpi.Execute "sens:corr:coll:guid:conn:port4 ""Not used"" " ' This next block
of commented code demonstrates how to specify an adapter ' and it's electrical
delay, in situations where you are performing an ' Unknown Thru or Adapter
Removal calibration. In most situations, the ' VNA is able to correctly
determine an adapter's electrical length ' at the end of the calibration.
However, there are scenarios where ' the VNA cannot correctly calculate the
length -- such as when the channel ' has a relatively small number of
measurement points (for example, 201 or less) ' and the adapter is
significantly long (for example, a cable that is several feet). ' In these
cases, the ADAP commands (below) enable you to explicitly specify ' the
adapter you are using. ' Send these commands prior to the
"sens:corr:coll:guid:init" command. ' Create adapter and return the adapter
number 'adapterNum = scpi.Execute("sens:corr:coll:guid:adap:cre? '" &
selectedConn1 & "','"& selectedConn2 & "'") ' The adapterNum string contains a
'+' character.  ' Here we convert to integer to remove that. 'adapterNum =
CStr( CInt(adapterNum) ) ' Specify that this adapter has 10 nanoseconds
electrical delay (coaxial). 'scpi.Execute "sens:corr:coll:guid:adap" &
adapterNum & ":del 10E-9" ' Text description of adapter 'scpi.Execute
"sens:corr:coll:guid:adap" & adapterNum & ":desc 'My adapter'" ' Select to use
this adapter specifically between ports 1 and 2 'scpi.Execute
"sens:corr:coll:guid:adap" & adapterNum & ":path 1,2" ' End of adapter block '
Query the list of acceptable cal kits and ' ECal module characterizations for
Port 1. kitList = scpi.Execute("sens:corr:coll:guid:ckit:cat? '" &
selectedConn1 & "'") ' Format the list with linefeed ' characters in place of
the commas kitList = FormatList(kitList) message = "Enter your cal kit or ECal
module characterization for Port 1. " message = message & "Choose from this
list:" message = message & Chr(10) & Chr(10) & kitList ' Select the Cal Kit or
ECal module ' characterization to use for Port 1. selectedKit =
InputBox(message) If selectedKit = "" Then Exit Sub scpi.Execute
"sens:corr:coll:guid:ckit:port1 '" & selectedKit & "'" ' Query the list of
acceptable cal kits ' and ECal module characterizations for Port 2. kitList =
scpi.Execute("sens:corr:coll:guid:ckit:cat? '" & selectedConn2 & "'") ' Format
the list with linefeed characters in place of the commas kitList =
FormatList(kitList) message = "Enter your cal kit or ECal module
characterization for Port 2. " message = message & "Choose from this list:"
message = message & Chr(10) & Chr(10) & kitList ' Select the Cal Kit or ECal
module ' characterization to use for Port 2. selectedKit = InputBox(message)
If selectedKit = "" Then Exit Sub scpi.Execute "sens:corr:coll:guid:ckit:port2
'" & selectedKit & "'" ' This determines whether the cal will be a "Guided
Power Cal" ' or just a traditional S-parameter cal. message = "On which port
number shall power be measured? " message = message & "For a traditional
guided cal without power cal, enter 0" Dim powerPort powerPort = CInt(
InputBox(message) ) If powerPort > 0 Then
scpi.Execute("sens:corr:coll:guid:psen" & CStr(powerPort) & ":stat on") Dim
retVal retVal = MsgBox("Is the power sensor's connector type or gender
different from the DUT connector for that port?", vbYesNo) If retVal = vbYes
Then message = "Enter your power sensor's connector. Choose from this list:"
message = message & Chr(10) & Chr(10) & connList ' Select the sensor's
connector. selectedConn1 = InputBox(message) If selectedConn1 = "" Then Exit
Sub scpi.Execute "sens:corr:coll:guid:psen" & CStr(powerPort) & ":conn '" &
selectedConn1 & "'" ' Query the list of acceptable cal kits and ECal module
characterizations ' that are applicable for the sensor's connector. kitList =
scpi.Execute("sens:corr:coll:guid:ckit:cat? '" & selectedConn1 & "'") ' Format
the list with linefeed ' characters in place of the commas kitList =
FormatList(kitList) message = "Enter your cal kit or ECal module
characterization to use for de-embed of the sensor's connector. " message =
message & "Choose from this list:" message = message & Chr(10) & Chr(10) &
kitList ' Select the Cal Kit or ECal module characterization to use for de-
embed of the sensor's connector. selectedKit = InputBox(message) If
selectedKit = "" Then Exit Sub scpi.Execute "sens:corr:coll:guid:psen" &
CStr(powerPort) & ":ckit '" & selectedKit & "'" Else
scpi.Execute("sens:corr:coll:guid:psen" & CStr(powerPort) & ":conn 'Ignored'")
End If ' End of block that considers the sensor's connector ' Ask for the
power level to perform the power cal at ' (if this command is omitted, the
default is 0 dBm). Dim powerLevel powerLevel = InputBox("Enter the power level
for the power cal to be performed at") If powerLevel = "" Then Exit Sub
scpi.Execute "sens:corr:coll:guid:psen" & CStr(powerPort) & ":pow:lev " &
powerLevel Else scpi.Execute("sens:corr:coll:guid:psen1:stat off") End If '
End of block that considers if the cal will include power calibration ' This
next block of commented code ' shows optional functions when using ECal. '
Send these "sens:corr:pref" commands prior to the ' "sens:corr:coll:guid:init"
command. ' Read ECAL information from ECal module #1 on the USB bus ' about
the Keysight factory characterization data 'module1Info =
scpi.Execute("sens:corr:coll:ckit:inf? ECAL1,CHAR0") 'MsgBox "Description of
ECal Module #1:" & Chr(10) & Chr(10) & module1Info ' The following command
enables auto orientation of ' the ECal module (The VNA senses which port of
the ' module is connected to which port of the VNA). 'scpi.Execute
"sens:corr:pref:ecal:ori ON" ' However, if you are measuring at very low power
levels where ' the VNA may fail to sense the module's orientation, then turn
auto ' orientation OFF and specify how the module is connected. ' "A1,B2"
indicates Port A of the module is connected ' to VNA Port 1 and Port B is
connected to VNA Port 2). 'scpi.Execute "sens:corr:pref:ecal:ori OFF"
'scpi.Execute "sens:corr:pref:ecal:pmap ECAL1,'A1,B2'" ' End of optional ECal
setup ' Select the thru method of "Default". This instructs the VNA to '
determine which thru standard measurement technique to use ' based upon the
selected connectors and ' calibration kit(s) and the VNA model number. ' with
new CMET and TMET 'default' is set by not sending the commands ' ' Initiate
the calibration and query the number of steps scpi.Execute
"sens:corr:coll:guid:init" numSteps =
scpi.Execute("sens:corr:coll:guid:steps?") MsgBox "Number of steps is " \+
CStr(numSteps) ' Measure the standards For i = 1 To numSteps step = "Step " \+
CStr(i) + " of " \+ CStr(numSteps) strPrompt =
scpi.Execute("sens:corr:coll:guid:desc? " \+ CStr(i)) MsgBox strPrompt,
vbOKOnly, step scpi.Execute "sens:corr:coll:guid:acq STAN" \+ CStr(i) Next '
Conclude the calibration scpi.Execute "sens:corr:coll:guid:save" MsgBox "Cal
is done!" End Sub Function FormatList(list) Dim tokens ' Strip the leading and
trailing quotation ' marks from the list string list = Mid(list, 2, Len(list)
- 3) ' Tokenize the comma-delimited list string ' into an array of the
individual substrings tokens = Split(list, ",") ' Rebuild the list string,
placing linefeed ' characters where the commas were, ' using Trim to remove
leading and trailing spaces. list = "" For i = 0 To UBound(tokens) tokens(i) =
Trim(tokens(i)) list = list & tokens(i) & Chr(9) If i < UBound(tokens) Then i
= i + 1 tokens(i) = Trim(tokens(i)) list = list & tokens(i) & Chr(10) End If
Next FormatList = list End Function  
---  
  
* * *

