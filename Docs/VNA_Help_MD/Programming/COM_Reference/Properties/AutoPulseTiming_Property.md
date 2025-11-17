##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoPulseTiming Property

* * *

#### Description

|  In Narrowband pulse mode, choose to set the delay and width automatically
or manually. This is labeled "Autoselect Width and Delay" on the user-
interface.  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoPulseTiming = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Manually set the delay and width for the measurement. True \-  Automatically set the delay and width for the measurement.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoPulseTiming = True 'Write  
value = pulse.AutoPulseTiming 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoPulseTiming(VARIANT_BOOL *pVal); HRESULT
put_AutoPulseTiming(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

