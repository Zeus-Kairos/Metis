# PowerSensor Object

* * *

### Description

Each power sensor connected to the power meter associated with Source Power
Calibration will have a PowerSensor object created to represent it. These
PowerSensor objects reside in the [PowerSensors](PowerSensors_Collection.md)
collection within the SourcePowerCalibrator object. You cannot directly create
PowerSensor objects, but can only retrieve existing ones from the PowerSensors
collection.

The PowerSensorCalFactorSegment object is also accessed through the
PowerSensor object. These are accessed through the CalFactorSegments
collection in the PowerSensor object.

### Accessing a PowerSensor object

Dim pna As AgilentPNA835x.Application  
Set pna = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim powerCalibrator as SourcePowerCalibrator  
Dim powerSensor as PowerSensor  
Dim calFactorSegment as PowerSensorCalFactorSegment  
  
Set powerCalibrator = pna.SourcePowerCalibrator  
  
' Specify GPIB address of the power meter.  
powerCalibrator.PowerMeterGPIBAddress = 13  
  
' Each time the PowerSensors collection is accessed, the power meter is
queried to determine which channels have sensors attached. The collection is
updated accordingly.  
  
If powerCalibrator.PowerSensors.Count > 0 Then  
' If channel B of the meter has a sensor attached but channel A does not, then
element 1 of the  
' collection is sensor B. Whenever channel A has a sensor, sensor A will be
element 1.  
Set powerSensor = powerCalibrator.PowerSensors(1)  
' Insert one new PowerSensorCalFactorSegment at the beginning of the
collection (index 1).  
  
powerSensor.CalFactorSegments.Add(1)  
' Assign our variable to refer to that object.  
Set calFactorSegment = powerSensor.CalFactorSegments(1)  
  
' Set property values for that object.  
calFactorSegment.Frequency = 300000  
' frequency in Hz  
calFactorSegment.CalFactor = 98  
' cal factor in percent  
  
End If

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

|

### Description  
  
[CalFactorSegments](CalFactorSegments_Collection.md) | IPowerSensor | Collection for iterating through the segments of a power sensor cal factor table.  
[LimitFrequency](../Properties/LimitFrequency_Property.md) | IPowerSensor2 | Enable or disable the use of the power meter min and max frequencies.  
[MaximumFrequency](../Properties/MaximiumFrequency_sourceCal_Property.md) | IPowerSensor | Maximum usable frequency (Hz) specified for this power sensor.  
[MinimumFrequency](../Properties/MinimumFrequency_sourceCal_Property.md) | IPowerSensor | Minimum usable frequency (Hz) specified for this power sensor.  
[PowerLossSegments](PowerLossSegments_Collection.md) | IPowerSensor2 | Collection for iterating through the segments of the power loss table used in source power calibration.  
[PowerMeterChannel](../Properties/PowerMeterChannel_Property.md) | IPowerSensor | Identifies which power sensor this object corresponds to ( or which channel of the power meter the sensor is connected to).  
[PowerSensorUncertainty](PowerSensorUncertainty_Object.md) | IPowerSensor4 | Provides access to the PowerSensorUncertainty object.  
[ReadingsPerPoint](../Properties/ReadingsPerPoint_Property.md) | IPowerSensor2 | Allows for settling of the power sensor READINGS.  
[ReadingsTolerance](../Properties/ReadingsTolerance_Property.md) | IPowerSensor2 | Allows for settling of the power sensor READINGS.  
[ReferenceCalFactor](../Properties/ReferenceCalFactor_Property.md) | IPowerSensor | Reference cal factor (%) associated with this power sensor.  
[SensorIndex](../Properties/SensorIndex_Property.md) | IPowerSensor2 | Sets the power sensor channel (1 or 2) to be used.  
[UseInternalCalFactors](PowerSensorAsReceiver_Object.md#UseInternalCalFactors) | IPowerSensor3 | Provides access to the PowerSensorAsReceiver object.  
[UsePowerLossSegments](../Properties/UsePowerLossSegments_Property.md) | IPowerSensor2 | Specifies if subsequent power readings will use of the loss table.  
  
###  IPowerSensor History

Interface | Introduced with VNA Rev:  
---|---  
IPowerSensor | 2.0  
IPowerSensor2 | 13.50  
IPowerSensor3 | 13.50  
IPowerSensor4 | 13.50

