##### Write/Read

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## ReverseLinearPowerLevel Property

* * *

#### Description

|  Set and read the reverse power level to the DUT. This is applied to the DUT
output port when making reverse measurements like S22.  
---|---  
  
####  VB Syntax

|  gca.ReverseLinearPowerLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (double) Reverse power level in dBm. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  -5  
  
#### Examples

|  gca.ReverseLinearPowerLevel = -10 'Write  
LinPwr = gca.ReverseLinearPowerLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReverseLinearPowerLevel(double* pVal) HRESULT
put_ReverseLinearPowerLevel(double newVal)  
  
#### Interface

|  IGainCompression  
  
* * *

