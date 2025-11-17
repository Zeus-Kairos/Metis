##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CTBOffset Property

* * *

#### Description

|  Sets and returns the offset that is applied to CTB measurements. Valid only
with measurement parameters: CTB, CTBLo, CTBHi, CTBE, CTBELo, and CTBEHi.  
---|---  
  
####  VB Syntax

|  imd.CTBOffset = value  
  
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

|  imd.CTBOffset = 2 'Write  
value = imd.CTBOffset 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CTBOffset(double *pVal)  
HRESULT put_CTBOffset(double pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

