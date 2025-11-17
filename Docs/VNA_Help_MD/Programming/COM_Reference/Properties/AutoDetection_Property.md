##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoDetection Property

* * *

#### Description

|  Choose to automatically or manually set pulse mode (Narrowband or Wideband)
for the channel.  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoDetection = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Manually set the pulse mode. Use  [WideBandDectionState](WideBandDectionState_Property.md) to set the pulse mode. True \-  Automatically set the pulse mode.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoDetection = True 'Write  
value = pulse.AutoDetection 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoDetection(VARIANT_BOOL *pVal); HRESULT
put_AutoDetection(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

