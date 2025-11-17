##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## PowerOffset (Cal All) Property

* * *

#### Description

|  Sets and returns the power offset value for a Cal All calibration. Power
Offset provides a method of compensating port power for added attenuation or
amplification in the source path. The result is that power at the specified
port reflects the added components.  
---|---  
  
####  VB Syntax

|  calAll.PowerOffset (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
port |  (Long) Source port number.  
value |  (Double) Power offset value in dB for a Cal All calibration.

  * For amplification, use positive offset.
  * For attenuation, use negative offset.

  
  
#### Return Type

|  Double  
  
#### Default

|  0 (zero dB)  
  
#### Examples

|  calAll.PowerOffset = 0 'Power Level of cal value = calAll.PowerOffset
'returns the power offset of the cal  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerOffset (long port, double val); HRESULT put_PowerOffset
long port, double* newVal);  
  
#### Interface

|  CalibrateAllChannels  
  
* * *

* * *

