##### Read-only

|

##### [About FIFO](../../../IFAccess/FIFO_and_other_Antenna_Features.md)  
  
---|---  
  
# DataAsInt16 Property

* * *

#### Description

|  Reads the FIFO buffer data as a Variant of a specified array size
(SafeArray) of 16-bit integers.  
---|---  
  
####  VB Syntax

|  varray = fifo.DataAsInt16(int16count)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
varray |  (Variant) Variable to store the returned data.  
fifo |  A [FIFO](../Objects/FIFO_Object.md) Object  
int16count |  (Long Integer) Number of data points to read.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = fifo.DataAsInt16(4096) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DataAsInt16(long int16count, VARIANT* varray);  
  
#### Interface

|  IFIFO2  
  
* * *

