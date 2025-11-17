##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CompositeNormalizedCTBPower Property

* * *

#### Description

|  Sets and returns the CSO Power. Valid only with measurement parameters:
CTBLo and CTBHi and for Normalization Modes dBm and dBmV.  
---|---  
  
####  VB Syntax

|  imd.CompositeNormalizedCTBPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) Power level. The units are determined by [CompositeNormalizationMode Property](CompositeNormalizationMode_Property.md), which must be set first.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  imd.CompositeNormalizedCTBPower = -5 'Write  
value = imd.CompositeNormalizedCTBPower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompositeNormalizedCTBPower(double *pVal)  
HRESULT put_CompositeNormalizedCTBPower(double pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

