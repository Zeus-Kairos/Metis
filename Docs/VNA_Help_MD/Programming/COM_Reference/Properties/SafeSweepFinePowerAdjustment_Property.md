##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
## SafeSweepFinePowerAdjustment Property

* * *

#### Description

|  Set and read the Safe Sweep FINE power adjustment.  
---|---  
  
####  VB Syntax

|  gca.SafeSweepFinePowerAdjustment = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double)  Fine power adjustment setting in dBm. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  1.0  
  
#### Examples

|  gca.SafeSweepFinePowerAdjustment = 0.1 'Write  
SSfine = gca.SafeSweepFinePowerAdjustment 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SafeSweepFinePowerAdjustment(double* value) HRESULT
put_SafeSweepFinePowerAdjustment(double value)  
  
#### Interface

|  IGainCompression  
  
* * *

