# PortExtension Object Superseded

* * *

ALL methods and properties on the PortExtension Object are Superseded with the
[Fixturing Object](Fixturing_Object.md).

### Description

Contains the methods and properties that control Port Extensions.

### Accessing a PortExtension object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim PortExt As PortExtension  
Set PortExt = app.PortExtension

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

### Methods

|

###  
  
---|---  
None |   
  
### Property

|

### Description  
  
[Input A](../Properties/Input_A_Property.md) |  Sets the Input A extension value.  
[Input B](../Properties/Input_B_Property.md) |  Sets the Input B extension value.  
[Input C](../Properties/Input_C_Property.md) |  Sets the Input C extension value.  
[Port 1](../Properties/Port_1_Property.md) |  Sets the Port 1 extension value.  
[Port 2](../Properties/Port_2_Property.md) |  Sets the Port 2 extension value.  
[Port 3](../Properties/Port_3_Property.md) |  Sets the Port 3 extension value.  
[State](../Properties/State_Property.md) |  Turns Port Extensions ON and OFF.  
  
###  IPort Extension History

Interface |  Introduced with VNA Rev:  
---|---  
IPort Extension |  1.0

