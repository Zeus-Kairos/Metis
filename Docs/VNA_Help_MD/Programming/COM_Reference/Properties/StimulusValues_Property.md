#####  Read-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## StimulusValues Property

* * *

#### Description

|  Returns the specified X-axis FOM frequency range. The array contains one
frequency value for each data point.  
---|---  
  
#### VB Syntax

|  value = calSet.StimulusValues (range)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calSet |  [CalSet](../Objects/CalSet_Object.md) (object) - Read-only property  
range |  (Long) FOM frequency range to read. 0 - returns source frequencies. 1 - returns response frequencies. 2 \- returns primary frequencies.  
  
#### Return Type

|  1-dimensional variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  array = CalSet.StimulusValues 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StimulusValues (long range, VARIANT* vals)  
  
#### Interface

|  ICalSet3  
  
* * *

