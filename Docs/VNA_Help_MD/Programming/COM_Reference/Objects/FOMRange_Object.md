# FOMRange Object

* * *

### Description

The FOM Range object provides access to the properties and methods for
configuring a specific Range for frequency offset measurements.

### Accessing an FOMRange object

Get a handle to a FOM Range by specifying an item in the [FOM
collection.](FOM_Collection.htm)

The FOM range items are typically numbered as follows:

  1. Primary

  2. Source

  3. Receivers

  4. Source2 (if present)

  5. Source3 (if present)

External devices can appear in the list of range names. [Learn
more.](../../../System/Configure_an_External_Device.htm)

Dim app as AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim ranges as FOM  
Set ranges = app.ActiveChannel.FOM  
ranges.item(2).Coupled = False

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
None |  |   
  
### Property

|

### Interface

|

### Description  
  
[Coupled](../Properties/Coupled_Property.md) | IFOMRange | Sets and returns the state of coupling (ON or OFF) of this range to the primary range.  
[CWFrequency](../Properties/CW_Frequency_Property.md) | IFOMRange | Set the Continuous Wave (CW) frequency.  
[Divisor](../Properties/Divisor_Property.md) | IFOMRange | Sets and returns the Divisor value to be used when coupling this range to the primary range.  
[Multiplier](../Properties/Multiplier_Property.md) | IFOMRange | Sets and returns the Multiplier value to be used when coupling this range to the primary range.  
[Name](../Properties/Name_FOMRange_Property.md) | IFOMRange | Returns the name of this FOM range object.  
[Offset](../Properties/Offset_Property.md) | IFOMRange | Sets and returns the offset value to be used when coupling this range to the primary range.  
[rangeNumber](../Properties/rangeNumber.md) | IFOMRange | Returns the index number of the range within the [FOM collection.](FOM_Collection.md)  
[Segments](Segments_Collection.md) | IFOMRange | Collection \- Used to add segment sweep capability to a range.  
[StartFrequency](../Properties/Start_Frequency_Property.md) | IFOMRange | Sets or returns the start frequency of this FOM Range.  
[StopFrequency](../Properties/Stop_Frequency_Property.md) | IFOMRange | Sets or returns the stop frequency of this FOM Range.  
[Sweep Type](../Properties/Sweep_Type_Property.md) | IFOMRange | Sets the type of range sweep.  
  
Note: Use the [Start Power](../Properties/Start_Power_Property.md) and [Stop
Power](../Properties/Stop_Power_Property.htm) settings from the [channel
object](Channel_Object.htm).

###  FOM History

Interface | Introduced with VNA Rev:  
---|---  
IFOM | 7.10  
  
* * *

