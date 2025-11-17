##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## WideBandDectionState Property

* * *

#### Description

|  Set and read the pulse mode detection method.  
---|---  
  
####  VB Syntax

|  pulseMeas.WideBandDectionState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Narrowband mode. True \-  Wideband mode  
  
#### Return Type

|  Boolean  
  
#### Default

|  Based on pulse width.  
  
#### Examples

|  pulse.WideBandDectionState = True 'Write  
value = pulse.WideBandDectionState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_WideBandDectionState(VARIANT_BOOL *pVal); HRESULT
put_WideBandDectionState(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

