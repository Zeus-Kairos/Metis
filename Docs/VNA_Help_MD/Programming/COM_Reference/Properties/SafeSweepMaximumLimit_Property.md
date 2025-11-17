##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
## SafeSweepMaximumLimit Property

* * *

#### Description

|  When the VNA port that is connected to the DUT Output measures the
specified value, the input power to the DUT is no longer incremented at that
frequency.  
---|---  
  
####  VB Syntax

|  gca.SafeSweepMaximumLimit = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double)  Maximum power level in dBm. Choose a value from -100 to +100.  
  
#### Return Type

|  Double  
  
#### Default

|  100  
  
#### Examples

|  gca.SafeSweepMaximumLimit = 23 'Write  
maxPwr = gca.SafeSweepMaximumLimit 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SafeSweepMaximumLimit(double* value) HRESULT
put_SafeSweepMaximumLimit(double value)  
  
#### Interface

|  IGainCompression  
  
* * *

  

