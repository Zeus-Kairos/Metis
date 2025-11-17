# HWAuxIO Object

* * *

Description

Contains the methods and properties that control the rear panel Material
Handler I/O and Power I/O connector.

Note: The Aux I/O connector is mentioned in these topics, but NO VNA models
supported by this VNA firmware have that connector.

### Accessing the HWAuxIO object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim AuxIO As HWAuxIO  
Set AuxIO = app.GetAuxIO

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

### Interface

[See History](HWauxIO_Object.md#history) | 

### Description  
  
---|---|---  
[get_InputVoltage](../Methods/get_InputVoltage_Method.md) |  IHWAuxIO |  Superseded by [get InputVoltageEX](../Properties/InputVoltageEX_Property.md)  
[get_OutputVoltage](../Methods/get_OutputVoltage_Method.md) |  IHWAuxIO |  Reads ADC output voltages.  
[get_OutputVoltageMode](../Methods/get_OutputVoltageMode_Method.md) |  IHWAuxIO2 |  Reads mode setting for either DAC output.  
[get_PortCData](../Methods/get_PortCData_Method.md) |  IHWAuxIO |  Reads a 4-bit value from Port C  
[put_OutputVoltage](../Methods/put_OutputVoltage_Method.md) |  IHWAuxIO |  Writes voltages to the DAC/Analog Output 1 and Output 2  
[put_OutputVoltageMode](../Methods/put_OutputVoltageMode_Method.md) |  IHWAuxIO2 |  Writes the mode setting for either DAC output.  
[put_PortCData](../Methods/put_PortCData_Method.md) |  IHWAuxIO |  Writes a 4-bit value to Port C  
  
### Properties

|

###

|

### Description  
  
FootSwitch |  IHWAuxIO |  Obsolete - Reads the Footswitch Input  
FootswitchMode |  IHWAuxIO3 |  Obsolete -Determines the action that occurs when the footswitch is pressed.  
[InputVoltageEX](../Properties/InputVoltageEX_Property.md) |  IHWAuxIO5 |  Reads the ADC input voltage  
[PassFailLogic](../Properties/PassFailLogic_Property.md) |  IHWAuxIO |  Sets and reads the logic of the PassFail line Shared with the HWMaterialHandler Object  
[PassFailMode](../Properties/PassFailMode_Property.md) |  IHWAuxIO |  Sets and reads the mode of the PassFail line Shared with the HWMaterialHandler Object  
[PassFailPolicy](../Properties/PassFailPolicy_Property.md) |  IHWAuxIO4 |  Sets the policy used to determine how global pass/fail is computed. Shared with the HWMaterialHandler Object  
[PassFailScope](../Properties/PassFailScope_Property.md) |  IHWAuxIO |  Sets and reads the scope of the PassFail line Shared with the HWMaterialHandler Object  
[PassFailStatus](../Properties/PassFailStatus_Property.md) |  IHWAuxIO4 |  Returns the most recent pass/fail status value. Shared with the HWMaterialHandler Object  
[PortCLogic](../Properties/PortCLogic_Property.md) |  HWAuxIO |  Sets and reads the logic mode of Port C  
[PortCMode](../Properties/PortCMode_Property.md) |  HWAuxIO |  Sets and reads the mode of Port C  
[SweepEndMode](../Properties/SweepEndMode_Property.md) |  HWAuxIO |  Sets and reads the event that causes the Sweep End line to go to a false state. Shared with the HWMaterialHandler Object  
  
###  IHWAuxIO History

Interface |  Introduced with VNA Rev:  
---|---  
IHWAuxIO |  2.0  
IHWAuxIO2 |  3.0  
IHWAuxIO3 |  3.0  
IHWAuxIO4 |  5.0  
IHWAuxIO5 |  7.5  
  
* * *

