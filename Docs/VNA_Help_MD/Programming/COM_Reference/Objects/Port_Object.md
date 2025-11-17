# Port Object

* * *

### Description

Provides access to the properties and methods that are used to assign a cable
to the port and reset noise data.

### Accessing the Port object

Get a handle to the Port object through the Ports Collection.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oPorts as UncertaintyManager  
Set oPorts = app.UncertaintyManager.Ports  
  
Dim oPort1 as Ports(1)

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [Superseded commands](../../Replacement_Commands.md)

### Methods

|

### Interface

[See History](CalManager_Object.md#Interface1) | 

### Description  
  
---|---|---  
[ResetNoise Method](../Methods/ResetNoise_Method.md) |  IUncertaintyPort |  Resets (clears) the characterized noise data for the VNA port.  
  
### Properties

|

###

|

###  
  
[Cable](../Properties/Cable_Property.md) |  IUncertaintyPort |  Set and return the cable name that is assigned to the port.  
[Number](../Properties/Number_ports_Property.md) |  IUncertaintyPort |  Returns the VNA port number.  
  
###  IUncertaintyPort History

Interface |  Introduced with VNA Rev:  
---|---  
IUncertaintyPort |  10.40

