##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CompositeNormalizationMode Property

* * *

#### Description

|  Sets and returns the method by which CTB and CSO calculations are
performed.  
---|---  
  
####  VB Syntax

|  imd.CompositeNormalizationMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Enum) 0 - naNone \- the normalized power is not used in calculation 1 - naNumberOfCarriers \- CTB and CSO is corrected by subtracting 10*log(N/2), where

  * N = # of carriers for CTB
  * N = # of distortion products for CSO

2 - naPdBm \- the composited normalized power for CTB or CSO is treated as a
dBm value 3 - naPdBmV \- the composited normalized power for CTB or CSO is
treated as a dBmV value. Note: Power values are stored using the currently-set
units. Therefore, first set units with this command, then set power values
using: [CompositeNormalizedCSOPower](CompositeNormalizedCSOPower_Property.md)
[CompositeNormalizedCTBPower](CompositeNormalizedCTBPower_Property.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  naNumberOfCarriers  
  
#### Examples

|  imd.CompositeNormalizationMode = naNone 'Write  
value = imd.CompositeNormalizationMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompositeNormalizationMode(tagNAIMDCompositeNormalizationMode
*pVal) HRESULT
put_CompositeNormalizationMode(tagNAIMDCompositeNormalizationMode pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

  

