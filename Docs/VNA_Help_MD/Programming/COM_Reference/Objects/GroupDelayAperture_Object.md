# GroupDelayAperture Object

* * *

### Description

Contains the methods and properties that set Group Delay Aperture.

### Accessing the GroupDelayAperture Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application")  
  
Dim GDAperture As GroupDelayAperture  
Set GDAperture = app.ActiveMeasurement.GroupDelayAperture

### See Also:

  * [Group Delay Measurements](../../../Tutorials/Group_Delay6_5.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[Frequency](../Properties/Frequency_GD_Property.md) |  IGroupDelayAperture |  Sets group delay aperture using a fixed frequency range.  
[Percent](../Properties/Percent_Property.md) |  IGroupDelayAperture |  Sets group delay aperture using a percent of the channel frequency span.  
[Points](../Properties/Points_Property.md) |  IGroupDelayAperture |  Sets group delay aperture using a fixed number of data points.  
  
###  IGroupDelayAperture History

Interface |  Introduced with VNA Rev:  
---|---  
IGroupDelayAperture |  A.09.20  
  
* * *

