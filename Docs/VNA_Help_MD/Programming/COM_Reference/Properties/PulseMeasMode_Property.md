##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
## PulseMeasMode Property

* * *

#### Description

|  Sets the pulse measurement state for the channel.  
---|---  
  
####  VB Syntax

|  pulseMeas.PulseMeasMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
value |  (Enum as NAPulseMeasurementMode) Choose from: (0) naPulseMeasurementOff - Turn OFF pulse measurements. (1) naPulseStandardMeasurement \- Turn ON standard pulse measurements. (2) naPulseProfileMeasurement \- Turn ON pulse profile measurements.   
  
#### Return Type

|  Enum  
  
#### Default

|  (0) naPulseMeasurementOff  
  
#### Examples

|  pulse.PulseMeasMode = naPulseProfileMeasurement 'Write  
value = pulse.PulseMeasMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PulseMeasMode(tagNAPulseMeasurementMode* pVal); HRESULT
put_PulseMeasMode(tagNAPulseMeasurementMode newVal);  
  
#### Interface

|  IPulseMeasurementControl  
  
* * *

