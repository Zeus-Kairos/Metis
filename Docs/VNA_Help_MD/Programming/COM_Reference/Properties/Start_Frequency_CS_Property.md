##### Read-only

|

##### [About Cal sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## StartFrequency (Cal Set) Property

* * *

#### Description

|  Returns the start frequency that is stored in the Cal Set.  
---|---  
  
####  VB Syntax

|  value = CalSet.StartFrequency (range)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (double) \- returned Start frequency in Hertz.  
CalSet |  [CalSet](../Objects/CalSet_Object.md) (object)  
range |  (Long) Choose: 0 ( Source and receiver frequency)  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  start = calset.StartFrequency(0)'Reads the start frequency stored in the
cal set.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_StartFrequency(long range, *pVal)  
  
#### Interface

|  |CalSet3  
  
* * *

