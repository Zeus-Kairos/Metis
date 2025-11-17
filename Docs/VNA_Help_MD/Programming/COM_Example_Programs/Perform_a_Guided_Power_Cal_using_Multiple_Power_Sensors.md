# Perform a Guided Power Cal using Multiple Power Sensors

* * *

This example uses the following interfaces to perform a power calibration
using two power sensors.

  * [GuidedCalibration](../COM_Reference/Objects/GuidedCalibration_Object.md)

  * [GuidedCalibrationPowerSensors](../COM_Reference/Objects/GuidedCalibrationPowerSensors_Collection.md)

  * [GuidedCalibrationPowerSensor](../COM_Reference/Objects/GuidedCalibrationPowerSensor_Object.md)

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Calibrate.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See Other COM Example Programs](COM_Example_Intro.md)

set app = CreateObject("Agilentpna835x.application") app.Reset
app.CreateMeasurement 1, "S11", 0, -1 ' create default S11 parameter
app.ActiveChannel.StartFrequency = 1e9 app.ActiveChannel.StopFrequency = 2e9
set calMgr = app.GetCalManager() set guidedCal = calMgr.GuidedCalibration
guidedCal.Initialize 1, false guidedCal.ConnectorType(1)="APC 3.5 male"
guidedCal.ConnectorType(2)= "APC 3.5 female" guidedCal.CalKitType(1)=
"N4691-60004 ECal" guidedCal.CalKitType(2)="N4691-60004 ECal"
guidedCal.PerformPowerCalibration(2)= true set sensors =
guidedCal.GuidedCalibrationPowerSensors(2) sensors.UseMultipleSensors = true
sensors.Item(1).Name = "pmar1" sensors.Item(1).StartFrequency = 1e9
sensors.Item(1).StopFrequency = 1.5e9 sensors.Add "pmar2"
sensors.Item(2).StartFrequency = 1.5e9 sensors.Item(2).StopFrequency = 2e9
numSteps = guidedCal.GenerateSteps() for i = 0 to numSteps-1 desc =
guidedCal.GetStepDescription(i + 1) msgbox desc guidedCal.AcquireStep(i + 1)
next guidedCal.GenerateErrorTerms()  
---

