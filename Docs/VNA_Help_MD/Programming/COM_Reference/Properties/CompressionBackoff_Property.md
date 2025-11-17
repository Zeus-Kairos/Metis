##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## CompressionBackoff Property

* * *

#### Description

|  Set and read value for the BackOff compression algorithm.  
---|---  
  
####  VB Syntax

|  gca.CompressionBackoff = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double)  Backoff value in dB. Choose from 30 to (-30)  
  
#### Return Type

|  Double  
  
#### Default

|  10  
  
#### Examples

|  gca.CompressionBackoff = 7 'Write  
acqMode = gca.CompressionBackoff 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionBackoff(double* pValue) HRESULT
put_CompressionBackoff(double newValue)  
  
#### Interface

|  IGainCompression  
  
* * *

