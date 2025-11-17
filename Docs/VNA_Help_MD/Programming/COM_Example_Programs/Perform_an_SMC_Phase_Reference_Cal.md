# Perform an SMC Phase Reference Cal

* * *

This example sets Phase Reference Cal properties, then performs a Phase
Reference calibration.

It is NOT necessary to create an SMC measurement before performing a remote
Phase Reference Cal. It is necessary when performed from the user interface.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as PMAR.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

[PhaseReferenceCalibration
Object](../COM_Reference/Objects/PhaseReferenceCalibration_Object.htm)

[Learn about SMC+ Phase](../../FreqOffset/SMC_plus_Phase.md)

[See other COM Example Programs](COM_Example_Intro.md)

Example Program: performs a phase reference calibration between 1Ghz to 10Ghz
on Ports 1, 2, and 4. Set app = CreateObject("agilentpna835x.application")
app.preset app.activechannel.hold 1 Set PhaseReferenceCal =
app.GetCalManager().PhaseReferenceCalibration ' always call reset at the
beginning of your cal PhaseReferenceCal.Reset PhaseReferenceCal.StartFrequency
= 1e9 PhaseReferenceCal.StopFrequency = 10e9 ' Read serial numbers of
connected phase references ' Into variant array refs =
PhaseReferenceCal.GetConnectedPhaseReferences 'Change the following to your
own phase reference name PhaseReferenceCal.PhaseReference = "MYPILOT44"
PhaseReferenceCal.SourceAttenuator = 10 PhaseReferenceCal.Calset = "Remote
Phase Reference" PhaseReferenceCal.ConnectorType = "APC 3.5 female"
PhaseReferenceCal.CalKitType = "85052D" ' Perform the calibration on Port 4
(Port 1 and Port 2 are always included) PhaseReferenceCal.IncludePort(4) =
true ' Uncomment the following line to use an unknown mixer ' to extend the
phase reference cal down to 10 Mhz ' If an unknown mixer is used, then the
start frequency is always 10 Mhz ' PhaseReferenceCal.IncludeUnknownMixer =
true Set guidedCal = PhaseReferenceCal.GuidedCalibration Steps =
guidedCal.GenerateSteps for i = 1 to steps Msgbox
guidedCal.GetStepDescription(i) guidedCal.AcquireStep i next msgbox
guidedCal.GenerateErrorTerms msgbox "done"  
---  
  
* * *

