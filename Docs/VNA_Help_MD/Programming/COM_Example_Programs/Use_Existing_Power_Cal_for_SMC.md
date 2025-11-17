# Use an Existing Power Cal During an SMC Cal

* * *

This example shows how to use an existing Source Power Cal instead of the
power cal that is performed during an SMC calibration. To run this program
without modification, you need the following:

  * A Mixer setup file saved on the VNA: C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr.

  * If the mixer file uses an external LO source, it must be connected and configured.

  * An ECal module that covers the frequency range of the measurement.

  * An SMC cal set named "SMC_CAL". This is the cal set that source power correction data will be imported from. The input and output frequency ranges of the cal set must cover the corresponding ranges used during calibration, or guided cal initialization will fail.

### Error Messages

  * If you attempt to import power cal data from an SMC calset that uses different ports than the ones currently in use, the message The necessary calibration standards were not found. will appear.

  * If the imported Cal Set does not cover the frequency range of the current cal, the message Interpolation target is out of range. Cannot interpolate. will appear.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as SMC.vbs. Learn how to setup and run the macro.

### See Also

[SMC Type Object](../COM_Reference/Objects/SMC_Type_Object.md)

[ImportDataSet Method](../COM_Reference/Methods/ImportDataSet_Method.md)

[See Other COM Example Programs](COM_Example_Intro.md)

Dim App Set App = CreateObject("AgilentPNA835x.Application") App.Preset Dim
Meas Set Meas = App.ActiveMeasurement Meas.Delete
App.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter","SC21" 'Other valid
strings that can be specified to create a measurement with a parameter 'other
than'"SC21" are: "S11", "S22", "IPwr", and "OPwr" Set Meas =
App.ActiveMeasurement 'You can perform mixer setup here or 'recall a previous
mixer setup from the VNA Hard drive. ' This is how the mixer could be
configured through the IMixer interface Dim mix Set mix = Meas ' reference to
IMixer object mix.ActiveXAxisRange = 0 ' 0 = mixINPUT (Input frequency range)
' Alternatively, recall a previous mixer setup from the VNA Hard drive
Meas.LoadFile "c:\users\public\network analyzer\documents/Mixer/MyMixer.mxr"
app.activechannel.numberofpoints = 21 Dim CalMgr Set CalMgr =
App.GetCalManager Dim SMC Set SMC = CalMgr.CreateCustomCal("SMC")
SMC.Initialize 1, 1 SMC.ConnectorType(1) = "APC 3.5 male" SMC.ConnectorType(2)
= "APC 3.5 female" SMC.CalKitType(1) = "N4691-60004 ECal" SMC.CalKitType(2) =
"N4691-60004 ECal" ' Import power cal data from an existing SMC calset.
SMC.ImportDataSet "SMC_CAL","POWER_STEP" 'Omit the isolation part of the
2-port cal (default behavior). SMC.OmitIsolation = 1 'Turn on auto orientation
for the ECal (default behavior). SMC.AutoOrient = 1 Dim steps steps =
SMC.GenerateSteps For i = 1 To steps MsgBox SMC.GetStepDescription(i)
SMC.AcquireStep i Next Dim calset calset = SMC.GenerateErrorTerms Msgbox("SMC
Cal Complete!")  
---  
  
* * *

