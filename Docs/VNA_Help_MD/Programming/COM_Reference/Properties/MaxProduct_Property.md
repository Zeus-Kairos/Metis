##### Write/Read

|

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## MaxProduct Property

* * *

#### Description

|  Sets and returns the maximum intermod product frequencies to be calibrated.  
---|---  
  
####  VB Syntax

|  imd.MaxProduct = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object)  
value |  Maximum IM products to calibrate. Choose from: 2 \- second order products 3 \- third order products 5 \- fifth order products 7 \- seventh order products 9 \- ninth order products  
  
#### Return Type

|  Long Integer  
  
#### Default

|  3  
  
#### Examples

|  imd.MaxProduct = 7 'Write  
mprod = imd.MaxProduct 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaxProduct(long * Val) HRESULT put_MaxProduct(long newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

