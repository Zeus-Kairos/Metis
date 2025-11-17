##### Read-only

|

##### [About Cal sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## CWFrequency (Cal Set) Property

* * *

#### Description

|  Returns the CW frequency that is stored in the Cal Set.  
---|---  
  
####  VB Syntax

|  value = CalSet.CWFrequency (range)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (double) \- returned CW frequency in Hertz.  
CalSet |  [CalSet](../Objects/CalSet_Object.md) (object)  
range |  (Long) Choose: 0  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  cw = calset.CWFrequency(0)'Reads the CW frequency stored in the cal set.  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CWFrequency(long range, double *pVal)  
  
#### Interface

|  |CalSet3  
  
* * *

