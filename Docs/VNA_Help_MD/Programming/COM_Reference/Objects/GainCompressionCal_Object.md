# Gain CompressionCal Object

* * *

### Description

Sets properties that are unique to a Gain Compression Cal (opt S93086A/B).

The remaining commands to perform a GCA Cal use the [Guided Calibration
commands](GuidedCalibration_Object.htm).

### Accessing the GainCompressionCal object

Dim app as AgilentPNA835x.Application Set GCAcal =
pna.GetCalmanager.[CreateCustomCalEx(channelNum)](../Methods/CreateCustomCalEx_Method.md)
Set GCACalExtension =
GCAcal.[CustomCalConfiguration](../Properties/CustomCalConfiguration_Property.md)
GCACalExtension.PowerLevel = 5  
---  
  
### See Also:

  * Example Program [Create and Cal a Gain Compression Measurement](../../COM_Example_Programs/Create_and_Cal_a_Gain_Compression_Measurement.md)

  * [GainCompression Object](GainCompression_Object.md)

  * [About Gain Compression Application](../../../Applications/Gain_Compression_Application.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[PowerLevel](../Properties/PowerLevel_Property.md) | IGainCompressionCal | Set and read the power level at which to perform the Source Power Cal.  
[PowerSensorCalKitType](../Properties/PowerSensorCalKitType_Property.md) | IGainCompressionCal2 | Set and read the cal kit to be used for calibrating at the port 1 reference plane.  
[PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Property.md) | IGainCompressionCal2 | Superseded by [PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Property.md) on the GuidedCal Object.  
  
###  IGainCompressionCal History

Interface | Introduced with VNA Rev:  
---|---  
IGainCompressionCal | 8.0  
IGainCompressionCal2 | 8.04  
  
* * *

