# FIFO Object

* * *

### Description

These properties control the First IN, First OUT (FIFO) buffer settings for
the PNA-X and N5264B.

The 4 GB FIFO data buffer is available with Option S93118A/B on the
[PNA-X](../../../Support/Configurations.md#PNAX) and
[N5264B](../../../Support/Configurations.md#N5264).

### Accessing the FIFO object

Dim app as AgilentPNA835x.Application  
Dim fifo as FIFO  
Set fifo = app.FIFO

### See Also:

  * [About FIFO](../../../IFAccess/FIFO_and_other_Antenna_Features.md#FIFO)

  * [FIFO example program](../../COM_Example_Programs/Setup_FastCW_and_FIFO.md)

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

### Methods

|

###

|

### Description  
  
---|---|---  
[Clear](../Methods/Clear_fifo_Method.md) | IFIFO | Clears the FIFO buffer  
  
### Properties

|

### Interface

[See History](IIFConfiguration_Object.md#history) | 

### Description  
  
[Data Property](../Properties/Data_Property.md) | IFIFO | Reads the next specified number of data points from the FIFO buffer.  
[DataByteCount](../Properties/DataByteCount_Property.md) | IFIFO2 | Reads the FIFO data byte count.  
[DataCount Property](../Properties/DataCount_Property.md) | IFIFO | Returns the total number of data points in the FIFO buffer.  
[DataAsBytes](../Properties/DataInBytes_Property.md) | IFIFO2 | Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of bytes.  
[DataInCompactForm](../Properties/DataInCompactForm_Property.md) | IFIFO | Reads data from the FIFO buffer. Same as Data but in a compact form.  
[DataAsFloat32](../Properties/DataInFloat32_Property.md) | IFIFO2 | Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 32-bit floating point (Float32) numbers.  
[DataAsInt16](../Properties/DataInInt16_Property.md) | IFIFO2 | Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 16-bit integers.  
[DataAsInt32](../Properties/DataInInt32_Property.md) | IFIFO2 | Reads the FIFO buffer data as a Variant of a specified array size (SafeArray) of 32-bit integers.  
[State](../Properties/State_Property.md) | IFIFO | Turns FIFO ON and OFF  
  
###  IFIFO History

Interface | Introduced with VNA Rev:  
---|---  
IFIFO | 8.35  
IFIFO2 | 12.80  
  
* * *

  

