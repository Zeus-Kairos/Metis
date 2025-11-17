# Perform a VMC Mixer Characterization

* * *

This example performs a VMC Mixer Characterization ONLY.

To run this example program without error:

  * Replace the ECal module model and serial number with that of your own, or a mechanical cal kit model.

  * Store a 'default.csa' instrument state file on the VNA with the setup information for your mixer. Or add mixer setup information to this program. [See an example.](Create_and_Cal_a_VMC_Measurement.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

[See Other COM Example
Programs](../GPIB_Example_Programs/SCPI_Example_Programs.htm)

dim pna: set pna = CreateObject("AgilentPNA835x.application") pna.recall
"c:\users\public\network analyzer\documents/default.csa" set chan =
pna.activechannel DoBasicVMCCal (chan.channelNumber) sub DoBasicVMCCal(
channel ) dim myMixerCharFile: myMixerCharFile = "C:\Program
Files(x86)\Keysight\Network Analyzer\Documents\com_characterize.s2p" '
construct a VMC calibration object dim calmanager: set calmanager =
pna.GetCalManager dim guidedCal: set guidedCal = calmanager.CreateCustomCalEx(
channel ) dim vmc: set vmc = guidedCal.CustomCalConfiguration ' Initialize the
cal object. ' usecalsetpreference is unused for the mixer characterization
wizard dim useCalSetPreference: useCalSetPreference = false vmc.Initialize
channel, useCalSetPreference ' Define the DUT connectors and kits at port 1 of
the VNA vmc.ConnectorType (1) = "APC 3.5 female" vmc.CalKitType(1) =
"N4691-60004 ECal 02593" ' Define the DUT connectors for the output of the
characterization mixer ' Use (logical) Port 3. vmc.ConnectorType(3) = "APC 3.5
female" ' Specify the mechanical cal kit for measuring the characterization
mixer vmc.CalKitType(3) = "N4691-60004 ECal 02593" vmc.CharacterizeMixerOnly =
true ' this specifies that we will create a characterization files ' this file
will be written (.s2p and .s2px file) vmc.CharFileName = MyMixerCharFile
vmc.AutoOrient = True ' For the mixer char step ONLY, ' Auto orientation is
turned OFF by the VNA. ' Otherwise it would fail because of the loss of the
mixer. ' Manually set the ECal orientation for that step.
vmc.EcalOrientation1Port(1) = "B1" ' the main calibration loop ' a description
for the connection instructions is read ' and then the standard is acquired
dim steps, connectionPrompt steps = vmc.GenerateSteps msgbox "Number of Steps
= " \+ cstr(steps) if (steps > 0) then ' otherwise an error condition occurred
for i = 1 to steps connectionPrompt = vmc.GetStepDescription( i ) msgbox
connectionPrompt vmc.AcquireStep( i ) next vmc.GenerateErrorTerms end if end
sub  
---

