##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## InputLinearPowerLevel Property

* * *

#### Description

|  Set and read the input power at which Linear Gain and all S-parameters are
measured.  
---|---  
  
####  VB Syntax

|  gca.InputLinearPowerLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double)  Linear input power level in dBm. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  \- 25 dBm  
  
#### Examples

|  gca.InputLinearPowerLevel = -10 'Write  
LinPwr = gca.InputLinearPowerLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_InputLinearPowerLevel(double* pVal) HRESULT
put_InputLinearPowerLevel(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

