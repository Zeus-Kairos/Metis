##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoOptimizePRF Property

* * *

#### Description

|  In Narrowband pulse mode, choose to set the Pulse Repetition Frequency
automatically or manually. This is labeled "Optimize Pulse Frequency" on the
user-interface. To make changes manually, use [MasterFrequency
Property](MasterFrequency_Property.htm) or [MasterPeriod
Property](MasterPeriod_Property.htm).  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoOptimizePRF = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Manually set the PRF for the measurement. True \-  Automatically set the PRF for the measurement.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoOptimizePRF = True 'Write  
value = pulse.AutoOptimizePRF 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoOptimizePRF(VARIANT_BOOL *pVal); HRESULT
put_AutoOptimizePRF(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

