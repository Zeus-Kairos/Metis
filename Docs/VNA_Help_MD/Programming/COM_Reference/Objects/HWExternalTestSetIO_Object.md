# HWExternalTestSetIO Object

* * *

Description

Contains the methods and properties that control the rear panel External Test
Set Input / Output connector

### Accessing the HWExternalTestSetIO object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim ExtTS As HWExternalTestSetIO  
Set ExtTS = app.GetExternalTestSetIO

### See Also:

  * [Pinout for the External Test Set Connector](../../TestSetIO_Connector.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Description  
  
---|---  
[ReadData](../Methods/ReadData_Method.md) |  Reads data and generates the appropriate timing signals  
[ReadRaw](../Methods/ReadRaw_Method.md) |  Reads data, but does NOT generate appropriate timing signals  
[WriteData](../Methods/WriteData_Method.md) |  Writes data and generates the appropriate timing signals  
[WriteRaw](../Methods/WriteRaw_Method.md) |  Writes data, but does NOT generate the appropriate timing signals  
  
### Properties

|

### Description  
  
[Interrupt](../Properties/Interrupt_Property.md) |  Returns the state of the Interrupt line  
[SweepHoldOff](../Properties/SweepHoldOff_Property.md) |  Returns the state of the Sweep Holdoff line  
  
###  IHWExternalTestSetIO History

Interface |  Introduced with VNA Rev:  
---|---  
HWExternalTestSetIO |  2.0

