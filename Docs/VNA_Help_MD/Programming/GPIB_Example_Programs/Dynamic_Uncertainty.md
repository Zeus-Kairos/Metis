# Dynamic Uncertainty

* * *

This example does the following in separate subprograms:

  * Setup Uncertainty Manager Workspace

  * Perform a standard 2-port Guided Cal

  * Perform a Cable Characterization

  * Perform a Noise Characterization

  * Perform a 2-Port Uncertainty Cal

  * Make Uncertainty Trace Settings

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

#### See Also

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See all Dynamic Uncertainty commands](../CalTopic.md#uncertainty)

[Learn about Dynamic Uncertainty (Option
S93015A/B)](../../S3_Cals/Dynamic_Uncertainty.htm)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
'Preset the analyzer scpi.Parse "SYST:PRESet" SetupWorkspace TwoPortGuidedCal
PerformCableChar PerformNoiseChar TwoPortUncertCal MakeTraceSettings
'********************************************* ' Setup Uncertainty Workspace '
Sub SetupWorkspace cableCatalog =
scpi.Parse("SYSTem:UNCertainty:CABLe:CATalog?") ' Strip the leading and
trailing quotation ' marks from the catalog string cableCatalog =
Mid(cableCatalog, 2, Len(cableCatalog) - 3) ' Tokenize the comma-delimited
list string ' into an array of the individual substrings cables =
Split(cableCatalog, ",") ' Re-assemble the cable list into one string
delimited by linefeed characters cableCatalog = "" For i = 0 To UBound(cables)
cableCatalog = cableCatalog & cables(i) & Chr(10) ' Uncomment the following
line to reset (clear) repeatability data for the cable 'scpi.Parse
"SYSTem:UNCertainty:CABLe:REPeat:RESet '" & cables(i) & "'" Next MsgBox
"Cables:" & Chr(10) & Chr(10) & cableCatalog portCatalog =
scpi.Parse("SOURce:CATalog?") ' Strip the leading and trailing quotation '
marks from the catalog string portCatalog = Mid(portCatalog, 2,
Len(portCatalog) - 3) ' Tokenize the comma-delimited list string ' into an
array of the individual substrings ports = Split(portCatalog, ",") portCatalog
= "" For i = 0 To UBound(ports) portNum = i + 1 ' Ensuring we only count the
actual testports and not any source-only ports like external sources If
(ports(i) = "Port " & CStr(portNum)) Then cable =
scpi.Parse("SYSTem:UNCertainty:PORT" & CStr(portNum) & ":CABLe:SELect?")
portCatalog = portCatalog & ports(i) & ": " & cable & Chr(10) ' Uncomment the
following line to reset (clear) noise data for the port 'scpi.Parse
"SYSTem:UNCertainty:PORT" & CStr(portNum) & ":NOISe:RESet" End If Next MsgBox
"Port Cables:" & Chr(10) & Chr(10) & portCatalog ' Uncomment the following
line to select the particular cable for all ports 'scpi.Parse
"SYSTem:UNCertainty:PORT:CABLe:ALL:SELect '" & cables(0) & "'" ' Uncomment the
following line to copy the noise data for Port 1 to be used for all ports
'scpi.Parse "SYSTem:UNCertainty:PORT:NOISe:ALL:COPY 1" ' Uncomment the
following line to reset (clear) the noise data for all ports 'scpi.Parse
"SYSTem:UNCertainty:PORT:NOISe:ALL:RESet" ' The next lines toggle uncertainty
manager properties on scpi.Parse "SYSTem:UNCertainty:ETERm:NOISe:ENABle ON"
MsgBox "Noise enabled for cals = " &
scpi.Parse("SYSTem:UNCertainty:ETERm:NOISe:ENABle?") scpi.Parse
"SYSTem:UNCertainty:ETERm:CABle:REPeat:ENABle ON" MsgBox "Cable repeatability
enabled for cals = " &
scpi.Parse("SYSTem:UNCertainty:ETERm:CABle:REPeat:ENABle?") scpi.Parse
"SYSTem:UNCertainty:ETERm:SDEFinitions:ENABle ON" MsgBox "Standards definition
uncertainties enabled for cals = " &
scpi.Parse("SYSTem:UNCertainty:ETERm:SDEFinitions:ENABle?") ' Uncomment the
following line to change the max number of uncertainty points for cals to be
500 'scpi.Parse "SYSTem:UNCertainty:POINts:MAXimum 500" MsgBox "Max number of
uncertainty points for cals = " &
scpi.Parse("SYSTem:UNCertainty:POINts:MAXimum?") ' Perform a Save of the
currently loaded uncertainty workspace ('.ml4') file scpi.Parse
"SYSTem:UNCertainty:STORe" ' Uncomment the following line to save the
currently loaded uncertainty workspace to a specific ('.ml4') filename
'scpi.Parse "SYSTem:UNCertainty:STORe 'myUncertaintyWorkspace.ml4'" '
Uncomment the following line to recall the uncertainty workspace ('.ml4') file
that we just saved 'scpi.Parse "SYSTem:UNCertainty:LOAD
'myUncertaintyWorkspace.ml4'" End Sub
'********************************************* ' Measure the steps of a cable
characterization, ' noise characterization, or a calibration. Sub
MeasureStepsOfCharacterizationOrCal(isNoiseCharacterization, numSteps) Dim
retVal Dim opc For i = 1 To numSteps step = "Step " \+ CStr(i) + " of " \+
CStr(numSteps) ' A "connection adjustment" means the user has to change
something about the connection, ' such as wiggling cable and re-connecting
standard during a repeatability characterization, ' or to move the slide
position of a sliding load if a connection step in a calibration ' were to
involve a sliding load. If isNoiseCharacterization = False Then
numConnectionAdjustmentsPerStep = scpi.Parse("sens1:corr:coll:guid:iter:min? "
\+ CStr(i)) Else ' noise characterization ' in this case, "iterations" are
just repetitive measurements, not re-adjust/re-measure the standard
numConnectionAdjustmentsPerStep = 1 End If For j = 1 To
numConnectionAdjustmentsPerStep strPrompt =
scpi.Parse("sens1:corr:coll:guid:desc? " \+ CStr(i)) retVal =
MsgBox(strPrompt, vbOKCancel, step) If retVal = vbCancel Then WScript.Quit opc
= scpi.Parse("sens1:corr:coll:guid:acq STAN" \+ CStr(i) + ";*OPC?") Next Next
scpi.Parse "sens1:corr:coll:guid:save" End Sub Function FormatList(list) Dim
tokens ' Strip the leading and trailing quotation ' marks from the list string
list = Mid(list, 2, Len(list) - 3) ' Tokenize the comma-delimited list string
' into an array of the individual substrings tokens = Split(list, ",") ' Using
Trim to remove leading and trailing spaces. For i = 0 To UBound(tokens)
tokens(i) = Trim(tokens(i)) Next FormatList = tokens End Function
'********************************************* ' Performing a NON-UNCERTAINTY
Guided 2-port cal (Ports 1 and 2) Sub TwoPortGuidedCal Dim connList Dim
connIndex1, connIndex2 Dim kitList Dim kitIndex Dim message Dim
formattedConnListStr message = "A non-uncertainty 2-port calibration will now
be performed, " message = message & "because a calibration is needed for
characterizing the cables" MsgBox message ' Query the list of connectors that
the VNA system recognizes connList =
scpi.Execute("sens:corr:coll:guid:conn:cat?") ' Turn the list from comma-
delimited string into an array of strings connList = FormatList(connList)
message = "Enter the index number (from this list) of your DUT connector for
Port 1:" & Chr(10) & Chr(10) ' Note: the array's indexing is 0-based but the
numbering is being presented in the InputBox as 1-based For i = 0 To
UBound(connList) formattedConnListStr = formattedConnListStr & Chr(9) &
CStr(i+1) + ") " & connList(i) & Chr(10) Next connIndex1 = InputBox(message &
formattedConnListStr) If connIndex1 = "" Then WScript.Quit ' Convert number
from String to Long and from 1-based index to 0-based connIndex1 =
CLng(connIndex1) - 1 scpi.Execute "sens:corr:coll:guid:conn:port1 '" &
connList(connIndex1) & "'" message = "Enter the index number (from this same
list again) of your DUT connector for Port 2:" & Chr(10) & Chr(10) connIndex2
= InputBox(message & formattedConnListStr) If connIndex2 = "" Then
WScript.Quit ' Convert number from String to Long and from 1-based index to
0-based connIndex2 = CLng(connIndex2) - 1 scpi.Execute
"sens:corr:coll:guid:conn:port2 '" & connList(connIndex2) & "'" ' Note: If
your VNA has more than 2 ports, then uncomment ' one or both of these next two
lines. 'scpi.Execute "sens:corr:coll:guid:conn:port3 ""Not used"" "
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
connList(connIndex1) & "','"& connList(connIndex2) & "'") ' The adapterNum
string contains a '+' character.  ' Here we convert to integer to remove that.
'adapterNum = CStr( CInt(adapterNum) ) ' Specify that this adapter has 10
nanoseconds electrical delay (coaxial). 'scpi.Execute
"sens:corr:coll:guid:adap" & adapterNum & ":del 10E-9" ' Text description of
adapter 'scpi.Execute "sens:corr:coll:guid:adap" & adapterNum & ":desc 'My
adapter'" ' Select to use this adapter specifically between ports 1 and 2
'scpi.Execute "sens:corr:coll:guid:adap" & adapterNum & ":path 1,2" ' End of
adapter block ' Query the list of acceptable cal kits and ' ECal module
characterizations for Port 1. kitList =
scpi.Execute("sens:corr:coll:guid:ckit:cat? '" & connList(connIndex1) & "'") '
Turn the list from a comma-delimited string into an array kitList =
FormatList(kitList) ' Select the Cal Kit or ECal module characterization to
use for Port 1. message = "Enter the index number (from this list) of your cal
kit or ECal module characterization for Port 1:" message = message & Chr(10) &
Chr(10) For i = 0 To UBound(kitList) message = message & Chr(9) & CStr(i+1) +
") " & kitList(i) & Chr(10) Next kitIndex = InputBox(message) If kitIndex = ""
Then WScript.Quit ' Convert number from String to Long and from 1-based index
to 0-based kitIndex = CLng(kitIndex) - 1 scpi.Execute
"sens:corr:coll:guid:ckit:port1 '" & kitList(kitIndex) & "'" ' Query the list
of acceptable cal kits ' and ECal module characterizations for Port 2. kitList
= scpi.Execute("sens:corr:coll:guid:ckit:cat? '" & connList(connIndex2) & "'")
' Turn the list from a comma-delimited string into an array kitList =
FormatList(kitList) ' Select the Cal Kit or ECal module characterization to
use for Port 2. message = "Enter the index number (from this list) of your cal
kit or ECal module characterization for Port 2:" message = message & Chr(10) &
Chr(10) For i = 0 To UBound(kitList) message = message & Chr(9) & CStr(i+1) +
") " & kitList(i) & Chr(10) Next kitIndex = InputBox(message) If kitIndex = ""
Then WScript.Quit ' Convert number from String to Long and from 1-based index
to 0-based kitIndex = CLng(kitIndex) - 1 scpi.Execute
"sens:corr:coll:guid:ckit:port2 '" & kitList(kitIndex) & "'" ' This determines
whether the cal will be a "Guided Power Cal" ' or just a traditional
S-parameter cal. message = "On which port number shall power be measured? "
message = message & "For a traditional guided cal without power cal, enter 0"
Dim powerPort powerPort = CInt( InputBox(message) ) If powerPort > 0 Then
scpi.Execute("sens:corr:coll:guid:psen" & CStr(powerPort) & ":stat on") Dim
retVal retVal = MsgBox("Is the power sensor's connector type or gender
different from the DUT connector for that port?", vbYesNo) If retVal = vbYes
Then message = "Enter the index number of your power sensor's connector.
Choose from this list:" & Chr(10) & Chr(10) ' Select the sensor's connector.
connIndex1 = InputBox(message & formattedConnListStr) If connIndex1 = "" Then
WScript.Quit connIndex1 = CLng(connIndex1) - 1 scpi.Execute
"sens:corr:coll:guid:psen" & CStr(powerPort) & ":conn '" &
connList(connIndex1) & "'" ' Query the list of acceptable cal kits and ECal
module characterizations ' that are applicable for the sensor's connector.
kitList = scpi.Execute("sens:corr:coll:guid:ckit:cat? '" &
connList(connIndex1) & "'") ' Turn the list from comma-delimited string into
an array of strings kitList = FormatList(kitList) ' Select the Cal Kit or ECal
module characterization to use for de-embed of the sensor's connector. message
= "Enter index number of your cal kit or ECal module characterization to use
for de-embed of the sensor's connector. " message = message & "Choose from
this list:" & Chr(10) & Chr(10) For i = 0 To UBound(kitList) message = message
& Chr(9) & CStr(i+1) + ") " & kitList(i) & Chr(10) Next kitIndex =
InputBox(message) If kitIndex = "" Then WScript.Quit kitIndex = CLng(kitIndex)
- 1 scpi.Execute "sens:corr:coll:guid:psen" & CStr(powerPort) & ":ckit '" &
kitList(kitIndex) & "'" Else scpi.Execute("sens:corr:coll:guid:psen" &
CStr(powerPort) & ":conn 'Ignored'") End If ' End of block that considers the
sensor's connector ' Ask for the power level to perform the power cal at ' (if
this command is omitted, the default is 0 dBm). Dim powerLevel powerLevel =
InputBox("Enter the power level for the power cal to be performed at") If
powerLevel = "" Then Exit Sub scpi.Execute "sens:corr:coll:guid:psen" &
CStr(powerPort) & ":pow:lev " & powerLevel Else
scpi.Execute("sens:corr:coll:guid:psen1:stat off") End If ' End of block that
considers if the cal will include power calibration ' This next block of
commented code ' shows optional functions when using ECal. ' Send these
"sens:corr:pref" commands prior to the ' "sens:corr:coll:guid:init" command. '
Read ECAL information from ECal module #1 on the USB bus ' about the Keysight
factory characterization data 'module1Info =
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
setup ' Initiate the calibration and query the number of steps scpi.Execute
"sens:corr:coll:guid:init" numCalSteps =
CLng(scpi.Execute("sens:corr:coll:guid:steps?")) MsgBox "Number of steps is "
\+ CStr(numCalSteps) ' Measure the standards and conclude the cal
MeasureStepsOfCharacterizationOrCal False, numCalSteps MsgBox "The cal needed
for the cable repeatability characterizations is done" End Sub
'********************************************* ' Perform Cable
Characterization Sub PerformCableChar ' Select/activate the default (S11)
measurement that should still ' be present since a Preset preceded this
subroutine scpi.Parse "CALC1:PAR:SEL 'CH1_S11_1'" ' Ensure the previously-
performed calibration is turned on for that selected measurement scpi.Parse
"CALC1:CORR ON" ' Initiate repeatability characterizations on Channel 1 for
Ports 1 and 2, with 3 ' iterative measurements of each standard (normally
users should specify more than 3 ' iterations per standard but it just makes
this example speedier) Dim numRequestedIterations numRequestedIterations = 3 '
Begin characterization for port 1 scpi.Parse
"sens1:corr:coll:guid:unc:char:cable 1, " \+ CStr(numRequestedIterations) Dim
numCharSteps ' Query the number of connection steps numCharSteps =
CLng(scpi.Parse("sens1:corr:coll:guid:steps?")) message = "Now to characterize
the cable currently associated with port 1. " message = message & "Number of
standard steps for characterizing port 1 cable = " & numCharSteps MsgBox
message MeasureStepsOfCharacterizationOrCal False, numCharSteps MsgBox "Cable
characterization for port 1 is done" ' Begin characterization for port 2
scpi.Parse "sens1:corr:coll:guid:unc:char:cable 2, " \+
CStr(numRequestedIterations) ' Query the number of connection steps
numCharSteps = CLng(scpi.Parse("sens1:corr:coll:guid:steps?")) message = "Now
to characterize the cable currently associated with port 2. " message =
message & "Number of standard steps for characterizing port 2 cable = " &
numCharSteps MsgBox message MeasureStepsOfCharacterizationOrCal False,
numCharSteps MsgBox "Cable characterization for port 2 is done" End Sub
'********************************************* 'Perform Noise Characterization
Sub PerformNoiseChar ' Initiate noise characterization on Channel 1 for Ports
1 and 2, with 3 iterative ' measurements of each standard (normally users
should specify more than 3 iterations ' per standard but it just makes this
example speedier) scpi.Parse "sens1:corr:coll:guid:unc:char:noise 1, 2, 3" Dim
numCharSteps ' Query the number of connection steps numCharSteps =
CLng(scpi.Parse("sens1:corr:coll:guid:steps?")) message = "Now to characterize
the system noise for ports 1 and 2. " message = message & "Number of
connection steps to be made = " & numCharSteps MsgBox message
MeasureStepsOfCharacterizationOrCal True, numCharSteps MsgBox "Noise
characterization is done" End Sub
'********************************************* 'Perform 2-port Uncertainty
Calibration (Ports 1 and 2) on Channel 1 Sub TwoPortUncertCal Dim kitList Dim
kitIndex Dim message ' Specify this calibration is to be performed with
uncertainties. scpi.Parse "sens1:corr:coll:guid:UNCertainty:ENABle ON" ' Query
the list of uncertainty cal kits and ' ECal module factory characterizations
applicable for the port cable connector. kitList =
scpi.Parse("sens:corr:coll:guid:ckit:port1:cat?") ' Turn the list from comma-
delimited string into an array of strings kitList = FormatList(kitList)
message = "Now to perform an uncertainty calibration for ports 1 and 2. "
message = message & "Enter the index number (from this list) of your cal kit
or ECal module to use:" message = message & Chr(10) & Chr(10) ' Note: the
array's indexing is 0-based but the numbering is being presented in the
InputBox as 1-based For i = 0 To UBound(kitList) message = message & Chr(9) &
CStr(i+1) + ") " & kitList(i) & Chr(10) Next ' Select the Cal Kit or ECal
module to use for both ports. ' If the selected kit does not have a suitable
set of standards ' that can mate the connector of the cable attached to Port
2, ' then the attempt to INIT the cal should yield an applicable error
message. kitIndex = InputBox(message) If kitIndex = "" Then WScript.Quit '
Convert from String to Long and from 1-based index to 0-based kitIndex =
CLng(kitIndex) - 1 scpi.Parse "sens:corr:coll:guid:ckit:port1 '" &
kitList(kitIndex) & "'" scpi.Parse "sens:corr:coll:guid:ckit:port2 '" &
kitList(kitIndex) & "'" ' Note: If your VNA has more than 2 ports, then
uncomment ' one or both of these next two lines just in case this channel '
may have had a remote non-Uncert cal performed prior that ' involving port 3
and/or 4. 'scpi.Parse "sens:corr:coll:guid:conn:port3 """" " 'scpi.Parse
"sens:corr:coll:guid:conn:port4 """" " ' This next block of commented code '
shows optional functions when using ECal. ' Send these "sens:corr:pref"
commands prior to the ' "sens:corr:coll:guid:init" command. ' Read ECAL
information from ECal module #1 on the USB bus ' about the factory
characterization data 'module1Info = scpi.Parse("sens:corr:coll:ckit:inf?
ECAL1,CHAR0") 'MsgBox "Description of ECal Module #1:" & Chr(10) & Chr(10) &
module1Info ' The following command enables auto orientation of ' the ECal
module (The VNA senses which port of the ' module is connected to which port
of the VNA). 'scpi.Parse "sens:corr:pref:ecal:ori ON" ' However, if you are
measuring at very low power levels where ' the VNA may fail to sense the
module's orientation, then turn auto ' orientation OFF and specify how the
module is connected. ' "A1,B2" indicates Port A of the module is connected '
to VNA Port 1 and Port B is connected to VNA Port 2). 'scpi.Parse
"sens:corr:pref:ecal:ori OFF" 'scpi.Parse "sens:corr:pref:ecal:pmap
ECAL1,'A1,B2'" ' End of optional ECal setup ' Initiate the calibration and
query the number of steps scpi.Parse "sens:corr:coll:guid:init" numCalSteps =
scpi.Parse("sens:corr:coll:guid:steps?") MsgBox "Number of steps is " \+
CStr(numCalSteps) ' Measure the standards and conclude the cal
MeasureStepsOfCharacterizationOrCal False, numCalSteps MsgBox "Cal is done"
End Sub '********************************************* 'Make Uncertainty Trace
Settings Sub MakeTraceSettings ' Note: normally you would first ensure your
active measurement is an S-parameter channel ' measurement before this point,
and that the channel has an uncertainty cal to be ' able to turn on
uncertainty display, but as the TwoPortUncertCal subroutine has ' executed
right before this one, that is already ensured. chanNum =
CInt(scpi.Parse("SYSTem:ACTive:CHANnel?")) If (chanNum = 0) Then MsgBox "No
active channel" WScript.Quit End If activeMeasName =
scpi.Parse("SYSTem:ACTive:MEASurement?") scpi.Parse "CALCulate" &
CStr(chanNum) & ":PARameter:SELect " & activeMeasName MsgBox "Uncertainty
Display Type = " & scpi.Parse("CALCulate" & CStr(chanNum) &
":UNCertainty:DISPlay:TYPE?") On Error Resume Next scpi.Parse "CALCulate" &
CStr(chanNum) & ":UNCertainty:DISPlay:TYPE SHADe" If Err.Number <> 0 Then
MsgBox Err.Description Err.Clear Else MsgBox "Uncertainty Display Type = " &
scpi.Parse("CALCulate" & CStr(chanNum) & ":UNCertainty:DISPlay:TYPE?") End If
On Error GoTo 0 MsgBox "CoverageFactor = " & scpi.Parse("CALCulate" &
CStr(chanNum) & ":UNCertainty:DISPlay:CFACtor?") ' Uncomment the following
line to try setting the CoverageFactor = 3 'scpi.Parse "CALCulate" &
CStr(chanNum) & ":UNCertainty:DISPlay:CFACtor 3" scpi.Parse "CALCulate" &
CStr(chanNum) & ":UNCertainty:MODE:CABLe:REPeat OFF" MsgBox "Cable
Repeatability Uncertainty state = " & scpi.Parse("CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:CABLe:REPeat?") scpi.Parse "CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:CABLe:REPeat ON" MsgBox "Cable Repeatability Uncertainty
state = " & scpi.Parse("CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:CABLe:REPeat?") scpi.Parse "CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:NOISe OFF" MsgBox "Measurement Noise Uncertainty state = "
& scpi.Parse("CALCulate" & CStr(chanNum) & ":UNCertainty:MODE:NOISe?")
scpi.Parse "CALCulate" & CStr(chanNum) & ":UNCertainty:MODE:NOISe ON" MsgBox
"Measurement Noise Uncertainty state = " & scpi.Parse("CALCulate" &
CStr(chanNum) & ":UNCertainty:MODE:NOISe?") scpi.Parse "CALCulate" &
CStr(chanNum) & ":UNCertainty:MODE:ETERm OFF" MsgBox "Error Term Uncertainty
state = " & scpi.Parse("CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:ETERm?") scpi.Parse "CALCulate" & CStr(chanNum) &
":UNCertainty:MODE:ETERm ON" MsgBox "Error Term Uncertainty state = " &
scpi.Parse("CALCulate" & CStr(chanNum) & ":UNCertainty:MODE:ETERm?") End Sub  
---  
  
* * *

