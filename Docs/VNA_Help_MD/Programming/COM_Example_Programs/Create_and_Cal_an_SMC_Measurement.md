# Create and Cal an SMC Measurement

* * *

This example creates and calibrates an SMC measurement. A power sensor must
first be connected to the VNA.

By removing the comments ( ' ) at the start of the BLUE code, it can also do
the following:

  * Load a Mixer setup file from the VNA at: C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr.

  * Cal using an ECal module.

  * Perform manual ECAL orientation

  * Load a [Phase Reference calibration](../../FreqOffset/SMC_plus_Phase.md).

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as SMC.vbs. Learn how to setup and run the macro.

### See Also

[Create an SMC Fixed Output Meas](Create_an_SMC_Fixed_Output_Meas.md)

[Use Existing Power Cal for SMC](Use_Existing_Power_Cal_for_SMC.md)

Dim App Set App = CreateObject("AgilentPNA835x.Application") App.Preset Dim
Meas Set Meas = App.ActiveMeasurement Meas.Delete
App.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter","SC21" 'Other valid
strings that can be specified to create a measurement with a parameter 'other
than'"SC21" are: "S11", "S22", "IPwr", and "OPwr" dim chan set chan =
app.activechannel 'Attenuator setting must match optional Phase Ref Cal
setting chan.attenuator(1) = 10 chan.NumberOfPoints = 11 chan.IFBandwidth =
1000 'You can perform mixer setup here or 'recall a previous mixer setup from
the VNA Hard drive. 'This is how to perform mixer setup using IConverter. '
Setup Stimulus dim cv set cv = chan.Converter cv.InputStartFrequency = 3.6e9
cv.InputStopFrequency = 4.9e9 cv.LOFixedFrequency(1) = 1e9 cv.LOPower(1) = 10
cv.OutputSideband = 0 'Lowside cv.Calculate 2 'Calc output 'cv.EnablePhase =
True cv.LOName(1)="Port 3" cv.Apply() ' Alternatively, recall a mixer setup
from the VNA Hard drive 'Meas.LoadFile "C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Mixer\MyMixer.mxr" ' Begin Calibration Dim CalMgr Set
CalMgr = App.GetCalManager Dim SMC Set SMC = CalMgr.CreateCustomCal("SMC")
SMC.Initialize 1, 1 SMC.ConnectorType(1) = "APC 3.5 male" SMC.ConnectorType(2)
= "APC 3.5 female" ' Use Mechanical cal kits SMC.CalKitType(1) = "85033D/E"
SMC.CalKitType(2) = "85033D/E" ' To use an ECal module instead, comment out
the above two lines ' and uncomment the appropriate lines below: ' Your ECal
module must already be connected ' via USB to the VNA. ' SMC.CalKitType(1) =
"N4691-60004 ECal" ' SMC.CalKitType(2) = "N4691-60004 ECal" ' Non-factory
characterizations are specified as follows: ' SMC.CalKitType(1) = "N4691-60004
User 1 ECal" ' When two or more ECal modules with the same model number are
connected ' also specify the serial number as follows: ' SMC.CalKitType(1) =
"N4691-60004 ECal 01234" ' When Disk Memory ECal user characterizations are
used, ' specify both the User char and the serial number as follows: '
SMC.CalKitType(1) = "N4691-60004 MyDskChar ECal 01234" ' Turn on auto
orientation for the ECal (default behavior). ' SMC.AutoOrient = 1' MsgBox("Cal
kits defined for Ports 1 and 2") ' Import power cal data from an existing SMC
calset. ' This calset MUST exist on the VNA. SMC.ImportDataSet "Phase
Reference-full-span","POWER_AND_PHASE" 'Omit the isolation part of the 2-port
cal (default behavior). SMC.OmitIsolation = 1 Dim steps steps =
SMC.GenerateSteps For i = 1 To steps MsgBox SMC.GetStepDescription(i)
SMC.AcquireStep i Next Dim calset calset = SMC.GenerateErrorTerms Msgbox("SMC
Cal Complete!")  
---  
  
* * *

* * *

