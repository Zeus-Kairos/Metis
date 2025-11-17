##### Read-only

|

##### [About Cal sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## StopFrequency (Cal Set) Property

* * *

#### Description

|  Returns the stop frequency that is stored in the Cal Set.  
---|---  
  
####  VB Syntax

|  value = CalSet.StopFrequency (range)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (double) \- returned Stop frequency in Hertz.  
CalSet |  [CalSet](../Objects/CalSet_Object.md) (object)  
range |  (Long) Choose: 0 (Source and receiver frequency)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  stop = calset.StopFrequency(0)'Reads the stop frequency stored in the cal
set.  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StopFrequency(long range, double *pVal)  
  
#### Interface

|  |CalSet3  
  
* * *

