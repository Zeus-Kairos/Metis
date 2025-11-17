##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## CompressionDeltaY

* * *

#### Description

|  Set and read the 'Y" value in the delta X/Y compression algorithm.  
---|---  
  
####  VB Syntax

|  gca.CompressionDeltaY = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double) -  
  
#### Return Type

|  Double  
  
#### Default

|  9  
  
#### Examples

|  gca.CompressionDeltaY = 7 'Write  
xDelta = gca.CompressionDeltaY 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionDeltaY(double* pVal) HRESULT
put_CompressionDeltaY(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

