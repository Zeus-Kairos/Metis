# DIQMeasurement Object

* * *

### Description

Controls the Differential I/Q application settings.

Note: There are TWO objects for making Differential IQ settings.

See the [DIQ Object](DIQ_Object.md)

### Accessing the Diff IQ and Diff IQMeas objects

Dim app as AgilentPNA835x.Application app.CreateCustomMeasurementEx 2,
"Differential I/Q", "IPwrF1" Dim DIQ Set DIQ =
app.ActiveChannel.[CustomChannelConfiguration](../Properties/CustomChannelConfiguration_Property.md)
Dim DiqMeas Set DiqMeas = app.ActiveMeasurement.CustomMeasurementConfiguration  
---  
  
### See Also:

  * Example program

  * [Differential I/Q application](../../../Applications/Differential_IQ.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

DIQ Select X-Axis |   
---|---  
![](../../../assets/images/DIQSelectXaxis.gif) |  [ActiveXAxis Property](../Properties/ActiveXAxis_Property.md)  
[XAxisDomain Property](../Properties/XAxisDomain_Property.md)  
[XAxisSource Property](../Properties/XAxisSource_Property.md)  
  
###  DIQMeas History

Interface |  Introduced with VNA Rev:  
---|---  
IDIQMeas |  10.25  
  
* * *

