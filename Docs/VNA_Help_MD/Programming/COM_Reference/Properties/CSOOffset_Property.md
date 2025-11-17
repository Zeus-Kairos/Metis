##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CSOOffset Property

* * *

#### Description

|  Sets and returns the offset that is applied to CSO measurements. Valid only
with measurement parameters: CSO2Lo and CSO2Hi.  
---|---  
  
####  VB Syntax

|  imd.CSOOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Offset value in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  imd.CSOOffset = 2 'Write  
value = imd.CSOOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CSOOffset(double *pVal)  
HRESULT put_CSOOffset(double pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

