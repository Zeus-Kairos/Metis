##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## CompositeNormalizedCSOPower Property

* * *

#### Description

|  Sets and returns the CSO Power for POWER [normalization
mode](CompositeNormalizationMode_Property.htm). Valid only with measurement
parameters: CSO2Lo and CSO2Hi and for Normalization Modes dBm and dBmV.  
---|---  
  
####  VB Syntax

|  imd.CompositeNormalizedCSOPower = value  
  
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

|  imd.CompositeNormalizedCSOPower = -5 'Write  
value = imd.CompositeNormalizedCSOPower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompositeNormalizedCSOPower(double *pVal)  
HRESULT put_CompositeNormalizedCSOPower(double pVal)  
  
#### Interface

|  ISweptIMD  
  
* * *

