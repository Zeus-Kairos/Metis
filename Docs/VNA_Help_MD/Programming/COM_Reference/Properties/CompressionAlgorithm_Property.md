##### Write/Read

|

##### [About Compression
Algorithm](../../../Applications/Gain_Compression_Application.htm#CompressionMethods)  
  
---|---  
  
## CompressionAlgorithm Property

* * *

#### Description

|  Set and read the algorithm method used to compute gain compression.  
---|---  
  
####  VB Syntax

|  gca.CompressionAlgorithm = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (tagNAGCACompressionAlgorithm) - Algorithm method. Choose from:

  * naCompressionFromLinearGain (0)
  * naCompressionFromMaximumGain (1)
  * naBackoffCompression (2)
  * naXYCompression (3)
  * naSaturation (4)

  
  
#### Return Type

|  Enum  
  
#### Default

|  naCompressionFromLinearGain (0)  
  
#### Examples

|  gca.CompressionAlgorithm = naXYCompression 'Write  
compAlg = gca.CompressionAlgorithm 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionAlgorithm(tagNAGCACompressionAlgorithm* pVal)
HRESULT put_CompressionAlgorithm(tagNAGCACompressionAlgorithm newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

