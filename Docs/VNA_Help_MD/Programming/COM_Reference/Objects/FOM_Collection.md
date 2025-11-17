# FOM Collection

* * *

### Description

The FOM collection provides access to the source and receiver range objects
which are used for configuring frequency offset measurements.

The FOM range items are typically numbered as follows:

  1. Primary

  2. Source

  3. Receivers

  4. Source2 (if present)

  5. Source3 (if present)

External devices can appear in the list of range names. [Learn
more.](../../../System/Configure_an_External_Device.htm)

### Accessing the FOM Collection and [FOMRange](FOMRange_Object.md) objects

Dim app as AgilentPNA835x.Application  
Dim chan as Channel  
Set chan = app.ActiveChannel  
  
Dim ifom as FOM  
Set ifom = chan.FOM  
  
ifom.item(2).Coupled = false

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

### Method

|

### Interface

### [See History](IIFConfiguration_Object.md#history)

|

### Description  
  
---|---|---  
[Item](../Methods/Item_Method.md) | IFOM |   
  
### Property

|

### Interface

|

### Description  
  
[DisplayRange](../Properties/DisplayRange_Property.md) | IFOM | Sets the range to be displayed on the VNA x-axis.  
[FOMRange](FOMRange_Object.md) | IFOM | Object  
[RangeCount](../Properties/RangeCount_Property.md) | IFOM | Returns the number of FOM ranges available on the VNA.  
[State](../Properties/State_Property.md) | IFOM | Turns Frequency Offset ON and OFF.  
  
###  FOM History

Interface | Introduced with VNA Rev:  
---|---  
IFOM | 7.10  
  
* * *

