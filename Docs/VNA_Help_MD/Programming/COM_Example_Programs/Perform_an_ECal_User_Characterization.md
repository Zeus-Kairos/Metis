## Perform an ECal User Characterization

* * *

This example performs a user-characterization and stores it to both the ECal
module memory and VNA disk memory.

It then performs two 2-port cals: the first using the characterization from
module memory, then using the characterization from disk memory.

Note: This example requires that channel 1 be already calibrated.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as ECal.vbs.

### See Also

[How to setup and run the macro.](../Using_Macros.md#HowToSetup)

[ECalUserCharacterizer
Object](../COM_Reference/Objects/ECalUserCharacterizer_Object.htm)

[About User Characterization](../../S3_Cals/ECal_User_Characterization.md)

[See Other COM Example Programs](COM_Example_Intro.md)

Option Explicit Dim pna Set pna = CreateObject("AgilentPNA835x.Application")
Dim calMgr Set calMgr = pna.GetCalManager ' Get ECal User Characterizer COM
object Dim ecalCharacterizer Set ecalCharacterizer =
calMgr.GetECalUserCharacterizer ' Substitute here the model number and serial
number of your own ECal. ' Note that this example corresponds to a 4-port ECal
module with ' serial number 00001. If instead you have a 2-port ECal module, '
their model numbers are '5x5' numbers -- for example, 'N4691-60001'. Dim
ecalModelNum ecalModelNum = "N4433A" Dim ecalSerialNum ecalSerialNum = "00001"
ecalCharacterizer.ECalID = ecalModelNum & "," & ecalSerialNum MsgBox "ECal
module to be characterized is: " & ecalCharacterizer.ECalID ' Set which user
characterization number (1-12) the new characterization ' will be stored to in
the ECal module when it is done. If you intend to ' store your user
characterization just to VNA Disk Memory and NOT the ' ECal module's memory,
then omit the setting of this property.
ecalCharacterizer.CharacterizationNumber = 1 ' The following commented-out
lines of code show how you can access ' the list of connector type names you
can set for the ports of an ' ECal when you user-characterize it. However,
please note that if ' you are writing the user characterization to the ECal
module's memory, ' as of yet only the Factory Defined set of connector choices
will work ' properly (see the
[ValidConnectorType](../COM_Reference/Properties/ValidConnectorType_Property.md)
property). ' If you will be saving your characterization to just ' VNA Disk
Memory only, then all connector names returned by this call ' will work, user-
defined connector names as well as factory-defined. 'Dim connTypeArray
'connTypeArray = ecalCharacterizer.ValidConnectorTypes 'MsgBox
connTypeArray(1) ' Access element 1 in the string array ' For each port of the
ECal module, specify which connector type ' is at the end of the adapter (or
cable or fixture) that is ' connected to that port of the ECal for the
characterization ' (must be one of the connector types that is included in the
' list that the ValidConnectorTypes method returns). The default ' is "No
adapter", which assumes you are characterizing that port ' of the ECal "as is"
(nothing attached to it). So in this example, ' Ports C and D of the ECal are
being characterized to just the ' ECal's connectors.
ecalCharacterizer.ConnectorType(1) = "APC 3.5 male" ' ECal Port A
ecalCharacterizer.ConnectorType(2) = "APC 3.5 male" ' ECal Port B ' As with
the connector types, the information set in these next ' few properties also
gets stored within the characterization. ' Set the name of the person and/or
company that is producing ' this characterization. ecalCharacterizer.UserName
= "John Doe, Acme Inc." ' Set user-specified description of the VNA being
used. ecalCharacterizer.UserDescriptionOfPNA = "SN US12345678" ' Set
descriptions of what you have connected to the ECal module's ' ports for the
characterization. ecalCharacterizer.PortDescription(1) = "3.5 mm adapter, SN
00001" ' Port A of the ECal ecalCharacterizer.PortDescription(2) = "3.5 mm
adapter, SN 00002" ' Port B of the ECal ' Begin a user characterization on
Channel 1. ' If you will be storing this characterization to the ECal module's
memory, then ' the boolean argument to this command should be set to True. If
you will be storing ' this characterization to VNA disk memory ONLY, then you
should specify False for ' that argument. In this example we will be storing
the characterization to both ' module memory and VNA disk memory, so we use
True. ecalCharacterizer.InitializeEx 1, True ' Generate the measurement steps
for the user characterization. Dim numSteps numSteps =
ecalCharacterizer.GenerateSteps ' Measure the steps. ' You must ensure you
have already applied the appropriate calibration to the channel ' already, or
else an error will be thrown indicating that. Dim i For i = 1 To numSteps
MsgBox ecalCharacterizer.GetStepDescription(i)
ecalCharacterizer.AcquireStep(i) MsgBox "Acquire is complete" Next MsgBox "Now
the user characterization will be saved to the ECal module and to PNA disk
memory" ' Save the user characterization to the ECal module's memory. ' Note
that this can take multiple minutes, depending on how ' many sweep points the
channel has. ecalCharacterizer.SaveToECal ' Save the user characterization to
VNA Disk Memory. Dim characterizationName characterizationName = "test"
ecalCharacterizer.SaveToDiskMemory(characterizationName) MsgBox "User
characterization is complete. Now we will calibrate using it. First we will
use it from ECal module memory." Dim moduleMemCalKitName moduleMemCalKitName =
GetCalKitName("User " & CStr(ecalCharacterizer.CharacterizationNumber))
DoTwoPortCal moduleMemCalKitName MsgBox "Now we will calibrate using the
characterization from PNA Disk Memory." Dim pnaDiskMemCalKitName
pnaDiskMemCalKitName = GetCalKitName(characterizationName) DoTwoPortCal
pnaDiskMemCalKitName MsgBox "Example has completed" Function
GetCalKitName(characterizationName) Dim calKitName calKitName = ecalModelNum
If Len(characterizationName) > 0 Then calKitName = calKitName & " " &
characterizationName calKitName = calKitName & " ECal " & ecalSerialNum
GetCalKitName = calKitName End Function Sub DoTwoPortCal(calKitName) '
Initialize guided cal to be performed on Channel 1. Dim guidedCal Set
guidedCal = calMgr.GuidedCalibration guidedCal.Initialize 1, True ' Specify
the DUT connector for each VNA port to be calibrated (DUT connector = ECal
characterization's connector) guidedCal.ConnectorType(1) = "APC 3.5 male"
guidedCal.ConnectorType(2) = "APC 3.5 male" ' Specify the "cal kit" for each
of those ports guidedCal.CalKitType(1) = calKitName guidedCal.CalKitType(2) =
calKitName ' We know this example will result in a calibration sequence of a
single "connection step" Dim numSteps numSteps = guidedCal.GenerateSteps '
Acquire the cal connection step guidedCal.AcquireStep 1 ' Conclude the cal and
turn it on guidedCal.GenerateErrorTerms End Sub  
---  
  
* * *

