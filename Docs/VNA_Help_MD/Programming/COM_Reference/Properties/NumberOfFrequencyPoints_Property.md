##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## NumberOfFrequencyPoints Property

* * *

#### Description

|  Set and read the number of frequency points for a Gain Compression channel.
Applies to all acquisition modes.  
---|---  
  
####  VB Syntax

|  gca.NumberOfFrequencyPoints = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (integer) - Frequency points. Do not exceed the max number of points. [Learn more.](../../../Applications/Gain_Compression_Application.md#PointsLimit)  
  
#### Return Type

|  Integer  
  
#### Default

|  201  
  
#### Examples

|  gca.NumberOfFrequencyPoints = 101 'Write  
freqPts = gca.NumberOfFrequencyPoints 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NumberOfFrequencyPoints(int* pVal) HRESULT
put_NumberOfFrequencyPoints(int newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

