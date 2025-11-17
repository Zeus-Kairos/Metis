# Create and Cal a VMC Measurement

* * *

The following example program sets up a 1-stage mixer, then performs a VMC
calibration using an N4691-60004 ECal module.

By removing the comments ( ' ) at the start of the BLUE code, it can also do
the following:

  * Use a mechanical cal kit

  * Perform manual ECAL orientation

  * Load a Mixer Characterization file

### See Also

[Converter Object](../COM_Reference/Objects/Converter_Object.md)

[VMCType Object](../COM_Reference/Objects/VMC_Type_Object.md)

[Example - Perform a VMC Mixer Characterization
ONLY](Perform_a_VMC_Mixer_Cal.htm)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as VMC.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

dim NASWEPT: NASWEPT = 0 dim NAFIXED: NAFIXED = 1 dim LOWSIDE: LOWSIDE = 0 dim
HIGHSIDE: HIGHSIDE = 1 dim MIXEROUT: MIXEROUT = 2 dim pna: set pna =
CreateObject("AgilentPNA835x.application") pna.reset ' Create a VMC channel '
Other valid measurement strings are: "S11", and "S22"
pna.CreateCustomMeasurementEx 1, "Vector Mixer/Converter","VC21",1 ' Setup
Stimulus dim chan: set chan = pna.activechannel dim cv: set cv =
chan.Converter chan.NumberOfPoints = 11 chan.IFBandwidth = 1000
cv.InputStartFrequency = 3.6e9 cv.InputStopFrequency = 3.9e9
cv.LOFixedFrequency(1) = 1e9 cv.LOPower(1) = 10 cv.OutputSideband = LOWSIDE
cv.Calculate MIXEROUT cv.LOName(1) = "Port 3" cv.Apply() DoBasicVMCCal
(chan.channelNumber) sub DoBasicVMCCal( channel ) dim myMixerCharFile:
myMixerCharFile = "C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\MyMixerS2P.s2p" ' construct a VMC calibration object dim
calmanager: set calmanager = pna.GetCalManager dim guidedCal: set guidedCal =
calmanager.CreateCustomCalEx( channel ) dim vmc: set vmc =
guidedCal.CustomCalConfiguration ' Initialize the cal object. ' Choose to
respect or ignore the Preference: Cal: Auto Save to User Calset ' if you set
this true, the behavior will be dependent on the setting ' of the preference.
dim useCalSetPreference: useCalSetPreference = false vmc.Initialize channel,
useCalSetPreference ' Define the DUT connectors and kits at ports 1 and 2 of
the VNA vmc.ConnectorType (1) = "APC 3.5 female" vmc.ConnectorType (2) = "APC
3.5 male" ' Use Mechanical cal kits vmc.CalKitType(1) = "85033D/E"
vmc.CalKitType(2) = "85033D/E" ' To use an ECal module instead, comment out
the above two lines ' and uncomment the appropriate lines below: ' Your ECal
module must already be connected ' via USB to the VNA. ' vmc.CalKitType(1) =
"N4691-60004 ECal" ' vmc.CalKitType(2) = "N4691-60004 ECal" ' Non-factory
characterizations are specified as follows: ' vmc.CalKitType(1) = "N4691-60004
User 1 ECal" ' When two or more ECal modules with the same model number are
connected ' also specify the serial number as follows: ' vmc.CalKitType(1) =
"N4691-60004 ECal 01234" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows: '
vmc.CalKitType(1) = "N4691-60004 MyDskChar ECal 01234" ' MsgBox("Cal kits
defined for Ports 1 and 2") ' By default, VMC requires the measurement of a
Calibration Mixer. ' To determine the conversion loss of the calmixer, the cal
wizard ' will add a step to perform a 1 port cal at the output of the mixer. '
The following commands opt to perform the mixer ' characterization using a cal
kit. ' Do both characterization and full 2-port cal vmc.CharacterizeMixerOnly
= False ' Define the DUT connectors for the output of the characterization
mixer ' Use (logical) Port 3\. If it is already used by the DUT, ' then
specify port 4. vmc.ConnectorType(3) = "APC 3.5 male" ' Specify the mechanical
cal kit for port 3 vmc.CalKitType(3) = "85033D/E" ' To avoid performing the
1-port cal steps, provide the wizard with a ' mixer characterization file.
Uncomment the following two lines to ' specify the characterization file. This
is an .S2P file. ' vmc.CharFileName = myMixerCharFile ' this file will be read
' vmc.LoadCharFromFile = true ' By default, auto orientation of the ecal
module is performed ' Uncomment the following lines to manually orient the
ecal ' vmc.autoorient = false ' for 2-port portion, ecal port A connected to
VNA port 1 ' vmc.EcalOrientation2Port(1) ="A1,B2" ' for mixer char, ecal port
A connected to cal mixer output ' vmc.EcalOrientation1Port(1) = "A1" ' the
main calibration loop ' a description for the connection instructions is read
' and then the standard is acquired dim steps, connectionPrompt steps =
vmc.GenerateSteps wscript.echo "Number of Steps = " \+ cstr(steps) if (steps >
0) then ' otherwise an error condition occurred for i = 1 to steps
connectionPrompt = vmc.GetStepDescription( i ) wscript.echo connectionPrompt
vmc.AcquireStep( i ) next vmc.GenerateErrorTerms end if end sub  
---  
  
* * *

