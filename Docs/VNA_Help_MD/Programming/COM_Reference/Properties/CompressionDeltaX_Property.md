##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## CompressionDeltaX Property

* * *

#### Description

|  Set and read the 'X" value in the delta X/Y compression algorithm.  
---|---  
  
####  VB Syntax

|  gca.CompressionDeltaX = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double) X value in dB. Choose from 30 to (-30)  
  
#### Return Type

|  Double  
  
#### Default

|  10  
  
#### Examples

|  gca.CompressionDeltaX = 'Write  
xDelta = gca.CompressionDeltaX 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionDeltaX(double* pVal) HRESULT
put_CompressionDeltaX(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

