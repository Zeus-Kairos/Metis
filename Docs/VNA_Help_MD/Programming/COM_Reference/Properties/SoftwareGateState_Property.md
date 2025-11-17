##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## SoftwareGateState Property

* * *

#### Description

|  When set to OFF, the improved software gating sensitivity is turned OFF and
all data outside the measurement band is zeroed. This setting is used for
troubleshooting purposes. There is NO user-interface control for this setting.  
---|---  
  
####  VB Syntax

|  pulseMeas.SoftwareGateState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  True \- Turn ON software gating. False \- Turn OFF software gating.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.SoftwareGateState = True 'Write  
value = pulse.SoftwareGateState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SoftwareGateState(VARIANT_BOOL *pVal); HRESULT
put_SoftwareGateState(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl2  
  
* * *

* * *

