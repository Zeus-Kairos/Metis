##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## SourceAttenuator (Cal All) Property

* * *

#### Description

|  Sets and returns the Source Attenuator setting for a Cal All calibration.  
---|---  
  
####  VB Syntax

|  calAll.SourceAttenuator (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAllSourceAttenuator](../Objects/CalibrateAllChannels_Object.md) (object)  
port |  (Long) Source port number.  
value |  (Double) Attenuation value in dB for a Cal All calibration. Choose a valid value for the VNA model. [See valid settings](../../../Support/Configurations.md).  
  
#### Return Type

|  Double  
  
#### Default

|  0 (zero dB)  
  
#### Examples

|  calAll.SourceAttenuator = 0 'Set value value = calAll.SourceAttenuator
'Return value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourceAttenuator (long port, double val); HRESULT
put_SourceAttenuator long port, double* newVal);  
  
#### Interface

|  ICalibrateAll  
  
* * *

* * *

