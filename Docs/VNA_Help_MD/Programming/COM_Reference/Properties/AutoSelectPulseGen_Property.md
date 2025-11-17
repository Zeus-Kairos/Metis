##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## AutoSelectPulseGen Property

* * *

#### Description

|  In Narrowband pulse mode, choose to set the pulse generator used to drive
the source modulation automatically or manually.  
---|---  
  
####  VB Syntax

|  pulseMeas.AutoSelectPulseGen = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
bool |  False \- Manually set source modulation drive for the measurement. True \-  Automatically set source modulation drive for the measurement.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  pulse.AutoSelectPulseGen = True 'Write  
value = pulse.AutoSelectPulseGen 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AutoSelectPulseGen(VARIANT_BOOL *pVal); HRESULT
put_AutoSelectPulseGen(VARIANT_BOOL newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

