# HWMaterialHandlerIO Object

* * *

Description

Contains the methods and properties that control the rear panel Material
Handler Input / Output connector.

### Accessing the HWMaterialHandlerIO object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim MatHdlr As HWMaterialHandlerIO  
Set MatHdlr = app.GetMaterialHandlerIO

### See Also:

  * [Pinout for the Material HandlerIO Connector](../../HandlerIO_Connector.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[get_Input1](../Methods/get_Input1_Method.md) |  HWMaterialHandlerIO |  Reads a hardware latch that captures low to high transition on Input1  
[get_Output](../Methods/get_Output_Method.md) |  HWMaterialHandlerIO |  Returns the last value written to the selected output pin.  
[get_Port](../Methods/get_Port_Method.md) |  HWMaterialHandlerIO |  Returns the value from the specified "readable" port.  
[put_Output](../Methods/put_Output_Method.md) |  HWMaterialHandlerIO |  Writes a TTL HI or TTL Low to output pins 3 or 4.  
[put_Port](../Methods/put_Port_Method.md) |  HWMaterialHandlerIO |  Writes a value to the specified port.  
  
### Properties

|

###

|

### Description  
  
[IndexState](../Properties/IndexState_Property.md) |  HWMaterialHandlerIO2 |  Determines the control of Material Handler connector Pin 20  
[ReadyForTriggerState](../Properties/ReadyForTriggerState_Property.md) |  HWMaterialHandlerIO2 |  Determines the control of Material Handler connector Pin 21  
[PassFailLogic](../Properties/PassFailLogic_Property.md) |  HWMaterialHandlerIO |  Sets and reads the logic of the PassFail line Shared with the HWAuxIO Object  
[PassFailMode](../Properties/PassFailMode_Property.md) |  HWMaterialHandlerIO |  Sets and reads the mode for the PassFail line Shared with the HWAuxIO Object  
[PassFailPolicy](../Properties/PassFailPolicy_Property.md) |  HWMaterialHandlerIO2 |  Sets the policy used to determine how global pass/fail is computed. Shared with the HWAuxIO Object  
[PassFailScope](../Properties/PassFailScope_Property.md) |  HWMaterialHandlerIO |  Sets and reads the scope for the PassFail line Shared with the HWAuxIO Object  
[PassFailStatus](../Properties/PassFailStatus_Property.md) |  HWMaterialHandlerIO2 |  Returns the most recent pass/fail status value. Shared with the HWAuxIO Object  
[PortLogic](../Properties/PortLogic_Property.md) |  HWMaterialHandlerIO |  Sets and returns the logic mode of data ports A-H  
[PortMode](../Properties/PortMode_Property.md) |  HWMaterialHandlerIO |  Sets and returns whether Port C or Port D is used for writing or reading data  
[SweepEndMode](../Properties/SweepEndMode_Property.md) |  HWMaterialHandlerIO |  Sets and reads the event that cause the Sweep End line to go to a low state. Shared with the HWAuxIO Object  
  
###  HWMaterialHandlerIO History

Interface |  Introduced with VNA Rev:  
---|---  
HWMaterialHandlerIO |  2.0  
HWMaterialHandlerIO2 |  5.0

