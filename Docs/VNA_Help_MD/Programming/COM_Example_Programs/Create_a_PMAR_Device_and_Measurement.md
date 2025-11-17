# Create a PMAR Device and Measurement

* * *

The following program creates a new External Device: a Power Meter as
Receiver, makes several power meter settings, and then creates a PMAR
measurement.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as PMAR.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

[ExternalDevices
Collection](../COM_Reference/Objects/ExternalDevices_Collection.htm)

[ExternalDevice Object](../COM_Reference/Objects/ExternalDevice_Object.md)

[PowerSensorAsReceiver
Object](../COM_Reference/Objects/PowerSensorAsReceiver_Object.htm)

[PowerSensorCalFactorSegmentPMAR
Object](../COM_Reference/Objects/PowerSensorCalFactorSegmentPMAR_Object.htm)

[PowerLossSegmentsPMAR_Collection](../COM_Reference/Objects/PowerLossSegmentsPMAR_Collection.md)

[PowerLossSegmentPMAR
Object](../COM_Reference/Objects/PowerLossSegmentPMAR_Object.htm)

dim app Set app = CreateObject("AgilentPNA835x.Application") dim
externalDevices Set externalDevices = app.ExternalDevices dim devicecount
devicecount = externalDevices.count externalDevices.Add "NewPMAR" dim
newExternalDevice Set newExternalDevice = externalDevices.Item("NewPMAR")
newExternalDevice.DeviceType = "Power Meter"
newExternalDevice.IOConfiguration= "GPIB0::14::INSTR"
'newExternalDevice.IOConfiguration = "USB0::2391::4865::GB45100278::0::INSTR"
newExternalDevice.IOEnable = true dim PMAR Set PMAR =
newExternalDevice.ExtendedProperties PMAR.SensorIndex = 1
PMAR.ReadingsPerPoint = 10 dim avr avr = PMAR.ReadingsPerPoint
PMAR.ReadingsTolerance = 0.1 dim tole tole = PMAR.ReadingsTolerance
PMAR.MinimumFrequency = 100000000 PMAR.MaximumFrequency = 10000000000
PMAR.LimitFrequency = false PMAR.referenceCalFactor = 99 Set
powerCalFactorSegments = PMAR.CalFactorSegments powerCalFactorSegments.Add
1,10 Set calpair = powerCalFactorSegments(1) calpair.Frequency = 1e9
calpair.CalFactor = 99 Set calpair = powerCalFactorSegments(2)
calpair.Frequency = 2e9 calpair.CalFactor = 98 powerCalFactorSegments.Remove
3,8 PMAR.UsePowerLossSegments = true Set pls = PMAR.PowerLossSegments pls.Add
1,5 Set pl = pls(1) pl.Loss = -1 pl.Frequency = 1e9 Set pl = pls(2) pl.Loss =
-2 pl.Frequency = 2e9 pls.Remove 3,3 newExternalDevice.active = true 'Create a
PMAR trace with power meter connected to port 3 app.CreateMeasurement
1,"NewPMAR",3,1  
---  
  
* * *

