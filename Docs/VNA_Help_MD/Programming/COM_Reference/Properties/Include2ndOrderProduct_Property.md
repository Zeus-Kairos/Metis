##### Write/Read

|

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## Include2ndOrderProduct Property

* * *

#### Description

|  Sets and returns whether to include the second order products in the
calibration. These frequencies of these products can be far from the main
tones.  
---|---  
  
####  VB Syntax

|  imd.Include2ndOrderProduct = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object)  
value |  (Boolean) Choose from: False - Do NOT include 2nd order products True - Include 2nd order products  
  
#### Return Type

|  Boolean  
  
#### Default

|  False - Do NOT include 2nd order products  
  
#### Examples

|  imd.Include2ndOrderProduct = true 'Write  
incl = imd.Include2ndOrderProduct 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Include2ndOrderProduct(VARIANT_BOOL * Val) HRESULT
put_Include2ndOrderProduct(VARIANT_BOOL newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

