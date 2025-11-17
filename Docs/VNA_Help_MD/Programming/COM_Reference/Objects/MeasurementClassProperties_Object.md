# MeasurementClassProperties Object

* * *

### Description

These properties return properties of specific measurement classes.

### Accessing the MeasurementClassProperties object

Set app = CreateObject("AgilentPNA835x.Application") Set cap =
app.Capabilities 'Access the MeasurmentClassProperties Object Set measProps =
cap.MeasurmentClassProperties ("Swept IMD") list=measProps.SupportedParameters  
---  
  
### See Also

  * [MeasurementClassProperties Property](../Properties/MeasurementClassProperties_Property.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](MeasurementClassProperties_Object.md#History) | 

###  
  
---|---|---  
None |  |   
  
### Properties

|

###

|

### Description  
  
[SupportedParameters](../Properties/SupportedParameters_Property.md) | MeasurementClassProperties |   
  
### IMeasurementClassProperties History

Interface | Introduced with VNA Rev:  
---|---  
IMeasurementClassProperties | 9.40  
  
* * *

