##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CSONumDistortionProducts Property

* * *

#### Description

|  Sets and returns the N = number of distortion products value for the
calculation of the CSO parameter. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#CSO)  
---|---  
  
####  VB Syntax

|  imd.CSONumDistortionProducts = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Long Integer) Number of distortion products  
  
#### Return Type

|  Long Integer  
  
#### Default

|  40  
  
#### Examples

|  imd.CSONumDistortionProducts = True 'Write  
value = imd.CSONumDistortionProducts 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CSONumDistortionProducts(long *pVal)  
HRESULT put_CSONumDistortionProducts(long *pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

