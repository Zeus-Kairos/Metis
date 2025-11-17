# GlobalPowerLimit Object

* * *

### Description

Provides access to the properties and methods for setting power limits for VNA
ports.

### Accessing the GlobalPowerLimit object

Dim app as AgilentPNA835x.Application  
Dim gpl as IGlobalPowerLimit  
Set gpl = app.GlobalPowerLimit

### See Also:

  * [About GlobalPowerLimit](../../../System/Power_Limit_and_Power_Offset.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

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
  
[Limit](../Properties/Limit_Property.md) |  IGlobalPowerLimit |  Sets and returns the power limit for the specified port.  
[Lock](../Properties/Lock_Property.md) |  IGlobalPowerLimit |  Enables or disables the ability to change the power limit values through the user interface.  
[State](../Properties/State_GPL_Property.md) |  IGlobalPowerLimit |  Turns GlobalPowerLimit ON and OFF  
  
###  IGlobalPowerLimit History

Interface |  Introduced with VNA Rev:  
---|---  
IGlobalPowerLimit |  9.0  
|  
  
* * *

