# Gating Object

* * *

Description

Contains the methods and properties that control Time Domain Gating.

### Accessing the Gating Object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim gate As Gating  
Set gate = app.ActiveMeasurement.Gating

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Time Domain Topics](../../../Time/TimeDomain.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|  | 

###  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[(see History)](Gating_Object.md#history) | 

### Description  
  
[Center](../Properties/Center_Property.md) |  IGating |  Sets or returns the Center time. Shared with the Transform Object  
[CoupledParameters](../Properties/CoupledParameters_Gate_Property.md) |  IGating2 |  Select Gating parameters to couple  
[Shape](../Properties/Shape_Property.md) |  IGating |  Specifies the shape of the gate filter.  
[Span](../Properties/Span_Property.md) |  IGating |  Sets or returns the Span time. Shared with the Transform Object  
[Start](../Properties/Start_Property.md) |  IGating |  Sets or returns the Start time. Shared with the Transform Object  
[State](../Properties/State_Property.md) |  IGating |  Turns an Object ON and OFF.  
[Stop](../Properties/Stop_Property.md) |  IGating |  Sets or returns the Stop time. Shared with the Transform Object  
[Type](../Properties/Type_Gate_Property.md) |  IGating |  Specifies the type of gate filter used.  
  
###  History

Interface |  Introduced with VNA Rev:  
---|---  
IGating |  1.0  
IGating2 |  4.2

