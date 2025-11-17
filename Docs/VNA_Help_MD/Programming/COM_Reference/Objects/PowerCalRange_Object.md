# PowerCalRange Object

* * *

### Description

Contains the methods and properties used to set start and stop frequency, and
number of points for an independent power calibration.

### Accessing the IndependentPowerCalibration object

For standard S-parameter channels:

Dim app as AgilentPNA835x.Application  
Dim CalMgr  
Set CalMgr = App.GetCalManager  
Dim CalAll  
Set CalAll = CalMgr.CalibrateAllChannels  
  
Dim IndependentPwrCal  
Set IndependentPwrCal = CalAll.IndependentPowerCalibration

To calibrate an [Application](../../../Applications/Applications.md) channel,
see [CreateCustomCalEx](../Methods/CreateCustomCalEx_Method.md) Method.

### See Also:

  * [PNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The PNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[NumberOfPoints](../Properties/NumberOfPoints_\(PowerCalRange\)_Property.md) |  IPowerCalRange |  Sets and gets the number of points for range <m> for source port<n>.  
[StartFrequency](../Properties/StartFrequency_\(PowerCalRange\)_Property.md) |  IPowerCalRange |  Sets and gets the start frequency for range <m> for source port<n>.  
[StopFrequency](../Properties/StopFrequency_\(PowerCalRange\)_Property.md) |  IPowerCalRange |  Sets and gets the stop frequency for range <m> for source port<n>.  
  
###  IIndependentPowerCalibration History

Interface |  Introduced with PNA Rev:  
---|---  
IPowerCalRange |  10.60  
  
* * *

