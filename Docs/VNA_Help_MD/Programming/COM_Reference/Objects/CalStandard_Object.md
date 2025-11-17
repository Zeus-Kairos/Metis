# CalStandard Object

* * *

### Description

Contains all of the settings that are required to modify a calibration
standard.

For more information, read [Specifying Calibration Standards and Kits for
Keysight Vector Network Analyzers (Application Note
1287-11](http://literature.cdn.Keysight.com/litweb/pdf/5989-4840EN.pdf))

### Accessing the CalStandard object

Get a handle to a standard with the
calkit.[GetCalStandard](../Methods/Get_Cal_Standard_Method.md) Method.

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim std As ICalStandard  
Set std = app.ActiveCalKit.GetCalStandard(1)  
std.Delay = 0.00000003

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Reading and Writing Calibration data](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Methods

|

###

|

###  
  
---|---|---  
None |  |   
  
### Properties

|

### Interface

[See History](CalStandard_Object.md#Interface1) | 

### Description  
  
[C0](../Properties/C0_Property.md) |  ICalStandard |  Sets and Returns the C0 (C-zero) value (the first capacitance value) for the calibration standard, when the Type is set to "naOpen".  
[C1](../Properties/C1_Property.md) |  ICalStandard |  Sets and Returns the C1 value (the second capacitance value) for the calibration standard, when the Type is set to "naOpen".  
[C2](../Properties/C2_Property.md) |  ICalStandard |  Sets and Returns the C2 value (the third capacitance value) for the calibration standard, when the Type is set to "naOpen".  
[C3](../Properties/C3_Property.md) |  ICalStandard |  Sets and Returns the C3 value (the fourth capacitance value) for the calibration standard, when the Type is set to "naOpen".  
[Delay](../Properties/Delay_Property.md) |  ICalStandard |  Sets and Returns the electrical delay value for the calibration standard.  
[L0](../Properties/L0_Property.md) |  ICalStandard |  Sets and Returns the L0 (L-zero) value (the first inductance value) for the calibration standard, when the Type is set to "naShort".  
[L1](../Properties/L1_Property.md) |  ICalStandard |  Sets and Returns the L1 value (the second inductance value) for the calibration standard, when the Type is set to "naShort"..  
[L2](../Properties/L2_Property.md) |  ICalStandard |  Sets and Returns the L2 value (the third inductance value) for the calibration standard, when the Type is set to "naShort"..  
[L3](../Properties/L3_Property.md) |  ICalStandard |  Sets and Returns the L3 value (the third inductance value) for the calibration standard, when the Type is set to "naShort"..  
[Label](../Properties/Label_Property.md) |  ICalStandard |  Sets and Returns the label for the calibration standard.  
[loss](../Properties/Loss_Property.md) |  ICalStandard |  Sets and Returns the insertion loss for the calibration standard.  
[Maximum  
Frequency](../Properties/MaximumFrequency_Property.htm) |  ICalStandard |  Sets and Returns the maximum frequency for the calibration standard.  
[Medium](../Properties/Medium_Property.md) |  ICalStandard |  Sets and Returns the media type of the calibration standard.  
[Minimum  
Frequency](../Properties/MinimumFrequency_Property.htm) |  ICalStandard |  Sets and Returns the minumum frequency for the calibration standard.  
[Type](../Properties/Type_calstd_Property.md) |  ICalStandard |  Sets and Returns the type of calibration standard. Selections are: naOpen, naShort, naLoad, naThru, naArbitraryImpedance and naSliding.  
[TZReal](../Properties/TZReal_Property.md) |  ICalStandard2 |  Sets and Returns the TZReal value (the Real Terminal Impedance value) for the calibration standard, when the Type is set to "naArbitraryImpedance".  
[TZImag](../Properties/TZImag_Property.md) |  ICalStandard2 |  Sets and Returns the TZImag value (the Imaginary Terminal Impedance value) for the calibration standard, when the Type is set to "naArbitraryImpedance".  
[Z0](../Properties/Z0_Property.md) |  ICalStandard |  Sets and Returns the characteristic impedance for the calibration standard.  
  
###  ICalStandard History

Interface |  Introduced with VNA Rev:  
---|---  
CalStandard |  1.0  
CalStandard2 |  3.0

