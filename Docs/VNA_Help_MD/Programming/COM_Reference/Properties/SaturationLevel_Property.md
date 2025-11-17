##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## SaturationLevel Property

* * *

#### Description

|  Set and read the deviation dB from the maximum Pout. This is the point of
saturation. This value is used for [Compression
Method](CompressionAlgorithm_Property.htm): Compression from Saturation.  
---|---  
  
####  VB Syntax

|  gca.SaturationLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double) - Saturation level in dB. Choose a value greater than 0.01 dB.  
  
#### Return Type

|  Double  
  
#### Default

|  .1 dB  
  
#### Examples

|  gca.SaturationLevel = .5 'Write  
satLevel = gca.SaturationLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SaturationLevel(double* pVal) HRESULT
put_SaturationLevel(double newVal)  
  
#### Interface

|  IGainCompression3  
  
* * *

