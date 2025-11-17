##### Write/Read

|

##### [About Safe
Sweep](../../../Applications/Gain_Compression_Application.htm#Safe)  
  
---|---  
  
## SafeSweepCoarsePowerAdjustment Property

* * *

#### Description

|  Set and read the Safe Sweep COARSE power adjustment.  
---|---  
  
####  VB Syntax

|  gca.SafeSweepCoarsePowerAdjustment = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (Double)  Coarse power adjustment setting in dBm. Choose a value from +30 to (-30).  
  
#### Return Type

|  Double  
  
#### Default

|  3.0  
  
#### Examples

|  gca.SafeSweepCoarsePowerAdjustment = 2.0 'Write  
SSCourse = gca.SafeSweepCoarsePowerAdjustment 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SafeSweepCoarsePowerAdjustment(double* value) HRESULT
put_SafeSweepCoarsePowerAdjustment(double value)  
  
#### Interface

|  IGainCompression  
  
* * *

