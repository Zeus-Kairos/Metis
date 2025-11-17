##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CTBXMODNumCarriers Property

* * *

#### Description

|  Sets the N = Total number of carriers value used in the calculation of
the XMOD and CTB parameter. [Learn
more.](../../../Applications/Swept_IMD_and_IM_Spectrum_Concepts.htm#XModulation)  
---|---  
  
####  VB Syntax

|  imd.CTBXMODNumCarriers = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Long Integer) Number of carriers.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  40  
  
#### Examples

|  imd.CTBXMODNumCarriers = 15 'Write  
value = imd.CTBXMODNumCarriers 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CTBXMODNumCarriers(double *pVal)  
HRESULT put_CTBXMODNumCarriers(double *pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

