##### Read-only

|

##### [About FIFO](../../../IFAccess/FIFO_and_other_Antenna_Features.md)  
  
---|---  
  
## DataInCompactForm Property

* * *

#### Description

|  Reads FIFO data the same as [Data Property](Data_Property.md) but returns
the data in a more compact form of SAFEARRAY. This is significantly faster but
it is not supported in all client environments.  
---|---  
  
####  VB Syntax

|  array = fifo.DataInCompactForm (count)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
array |  (Variant) Variable to store the returned data  
fifo |  A [FIFO](../Objects/FIFO_Object.md) Object  
count |  (Long Integer) Number of data points to read.  
  
#### Return Type

|  Returns an array of 4 byte floating point numbers.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = fifo.DataInCompactForm(500) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DataInCompactForm(long count,VARIANT * data);  
  
#### Interface

|  IFIFO  
  
* * *

