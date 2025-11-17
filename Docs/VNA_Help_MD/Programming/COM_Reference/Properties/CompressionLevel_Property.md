##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## CompressionLevel Property

* * *

#### Description

|  Set and read the desired gain reduction (from reference gain). This value
is used for [Compression Methods](CompressionAlgorithm_Property.md):
Compression from Linear Gain and Compression from Maximum Gain.  
---|---  
  
####  VB Syntax

|  gca.CompressionLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double) - Compression level in dB. Choose a value greater than 0.1 dB.  
  
#### Return Type

|  Double  
  
#### Default

|  1  
  
#### Examples

|  gca.CompressionLevel = 1.5 'Write  
compLevel = gca.CompressionLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionLevel(double* pVal) HRESULT
put_CompressionLevel(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

