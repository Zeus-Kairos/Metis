##### Read-only

|

##### [About FIFO](../../../IFAccess/FIFO_and_other_Antenna_Features.md)  
  
---|---  
  
## Data Property

* * *

#### Description

|  Reads the next specified number of data points from the FIFO buffer. The
data is returned in 32 bit real/imaginary pair. Data is cleared as it is read.
Note: This method is the slowest way to transfer data using COM. However, it
is supported by all COM client programming languages. For better performance,
try using [DataInCompactForm](DataInCompactForm_Property.md).  
---|---  
  
####  VB Syntax

|  array = fifo.Data (count)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
array |  (Variant) Variable to store the returned data.  
fifo |  A [FIFO](../Objects/FIFO_Object.md) Object  
count |  (Long Integer) Number of data points to read.  
  
#### Return Type

|  Variant array. Each VARIANT is typed as a 4-byte floating point number.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = fifo.Data(500) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Data(long count,VARIANT * data);  
  
#### Interface

|  IFIFO  
  
* * *

