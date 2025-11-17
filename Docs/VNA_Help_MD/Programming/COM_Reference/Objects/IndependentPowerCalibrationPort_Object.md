# IndependentPowerCalibrationPort Object

* * *

Description

Contains the methods and properties used to perform an independent power
calibration on a specific source port.

### Accessing the IndependentPowerCalibrationPort object

Dim app as AgilentPNA835x.Application  
Dim CalMgr  
Set CalMgr = App.GetCalManager  
Dim CalAll  
Set CalAll = CalMgr.CalibrateAllChannels  
  
Dim IndependentPwrCalPort  
Set IndependentPwrCalPort = CalAll.IndependentPowerCalibrationPort

### See Also:

  * [Collections in the Analyzer](../../Learning_about_COM/Collections_in_the_Analyzer.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[AddPowerCalRange](../Methods/AddPowerCalRange_Method.md) | IIndependentPowerCalibrationPort | Adds a power cal range for a specific port <n>.  
[Reset](../Methods/Reset_\(Independent_CalAll\)_Method.md) | IIndependentPowerCalibrationPort | Resets all ranges for the given source port <n>.  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[PowerCalRange](../Properties/PowerCalRange_Property.md) | IIndependentPowerCalibrationPort | Returns a handle to the PowerCalRange object.  
[RangeCount](../Properties/RangeCount_\(Independent_Power_Cal\)_Property.md) | IIndependentPowerCalibrationPort | Queries how many ranges are included in the calibration for source port <n>.  
  
* * *

### IIndependentPowerCalibrationPort History

Interface | Introduced with VNA Rev:  
---|---  
IIndependentPowerCalibrationPort | 12.90  
|

