# PowerSensorAsReceiver Object

* * *

### Description

Provides the settings for configuring a Power Meter to be used as a VNA
Receiver (PMAR).

### Accessing a PowerSensorAsReceiver object

This object is accessed through ExternalDevice.ExtendedProperties. When an
external device is added to the [ExternalDevices
collection](ExternalDevices_Collection.htm), and the DeviceType property is
set to Power Meter, then ExtendedProperties is used to get a handle to this
object.

externalDevices.Add "NewPMAR" dim newExternalDevice Set newExternalDevice =
externalDevices.Item("NewPMAR") newExternalDevice.DeviceType = "Power Meter"
dim PMAR Set PMAR = newExternalDevice.ExtendedProperties PMAR.ReadingsPerPoint
= 10  
---  
  
### See Also:

  * Example: [Create a PMAR Device and Measurement](../../COM_Example_Programs/Create_a_PMAR_Device_and_Measurement.md)

  * [Configure an External Device](../../../System/Configure_an_External_Device.md)

  * [ExternalDevice Object](ExternalDevice_Object.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

(Bold Methods or Properties provide access to a child object)

### Methods

|

### Description  
  
---|---  
None |   
  
### Properties

|

### Description  
  
[CalFactorSegments](CalFactorSegmentsPMAR_Collection.md) | Provides access to the collection of segments of a power sensor cal factor table.  
[LimitFrequency](../Properties/LimitFrequency_Property.md) | Enable or disable the use of the power meter min and max frequencies.  
[MaximumFrequency](../Properties/MaximiumFrequency_sourceCal_Property.md) | Maximum usable frequency (Hz) specified for this power sensor.  
[MinimumFrequency](../Properties/MinimumFrequency_sourceCal_Property.md) | Minimum usable frequency (Hz) specified for this power sensor.  
[PowerLossSegments](PowerLossSegmentsPMAR_Collection.md) | Provides access to the collection of segments of the power loss table.  
[PowerMeterChannel](../Properties/PowerMeterChannel_Property.md) | Identifies which power sensor this object corresponds to (or which channel of the power meter the sensor is connected to).  
[ReadingsPerPoint](../Properties/ReadingsPerPoint_Property.md) | Allows for settling of the power sensor READINGS.  
[ReadingsTolerance](../Properties/ReadingsTolerance_Property.md) | Allows for settling of the power sensor READINGS.  
[ReferenceCalFactor](../Properties/ReferenceCalFactor_Property.md) | Reference cal factor (%) associated with this power sensor.   
[SensorIndex](../Properties/SensorIndex_Property.md) | Sets the power sensor channel (1 or 2) to be used.  
[UseInternalCalFactors](../Properties/UseInternalCalFactors_Property.md) | Enables/disables use of internal calibration factors for power sensors with built-in calibration factors.  
[UsePowerLossSegments](../Properties/UsePowerLossSegments_Property.md) | Specifies if subsequent power readings will use the loss table.  
  
###  IPowerSensorAsReceiver History

Interface | Introduced with VNA Rev:  
---|---  
IPowerSensorAsReceiver | 9.0

