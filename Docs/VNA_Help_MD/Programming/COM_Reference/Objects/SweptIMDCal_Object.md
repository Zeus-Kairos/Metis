# SweptIMDCal Object

* * *

### Description

Sets properties that are unique to a Swept IMD Cal (opt S93087A/B).

Use the [Guided Calibration commands](GuidedCalibration_Object.md) for the
remaining commands to perform a Swept IMD Cal

### Accessing the SweptIMDCal object

Dim app as AgilentPNA835x.Application Set IMDcal =
pna.GetCalmanager.[CreateCustomCalEx(channelNum)](../Methods/CreateCustomCalEx_Method.md)
Set IMDCalExtension =
IMDcal.[CustomCalConfiguration](../Properties/CustomCalConfiguration_Property.md)
IMDCalExtension.PowerLevel = 5  
---  
  
### See Also:

  * Example Program [Create and Cal a Swept IMD Measurement](../../COM_Example_Programs/Create_and_Cal_a_Swept_IMD_Measurement.md)

  * [SweptIMD Object](SweptIMD_Object.md)

  * [About Swept IMD measurements](../../../Applications/Swept_IMD.md)

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
  
[CalibrationFrequencies](../Properties/CalibrationFrequencies_Property.md) | ISweptIMDCal | Perform the source power cal at the center frequencies or at all main tone frequencies.  
[CalMethod](../Properties/CalMethod_imd_Property.md) | ISweptIMDCal | Sets the method by which the match-correction portion of an IMD cal is performed  
[EnableLOPowerCal](../Properties/EnableLOPowerCal_Property.md) | ISweptIMDCal2 | Enable or disable an LO power cal with an IMDx calibration.  
[Include2ndOrderProduct](../Properties/Include2ndOrderProduct_Property.md) | ISweptIMDCal | Include the second order products in the calibration.  
[MaxProduct](../Properties/MaxProduct_Property.md) | ISweptIMDCal | Sets and returns the maximum intermod product frequencies to be calibrated.  
[PowerLevel](../Properties/PowerLevel_Property.md) | ISweptIMDCal | Set and read the power level of the source power cal.  
[PowerSensorCalKitType](../Properties/PowerSensorCalKitType_Property.md) | ISweptIMDCal | Set and read the cal kit to be used for port 1 adapter compensation.  
[PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Property.md) | ISweptIMDCal | Superseded Use GuidedCal.[PowerSensorConnectorType](../Properties/PowerSensorConnectorType_Property.md)  
  
###  ISweptIMD History

Interface | Introduced with VNA Rev:  
---|---  
ISweptIMDCal | 8.33  
ISweptIMDCal2 | 8.55  
  
* * *

