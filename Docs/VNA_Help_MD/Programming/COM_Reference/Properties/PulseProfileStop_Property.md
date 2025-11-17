##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
# PulseProfileStop Property

* * *

#### Description

|  Sets and returns the stop time of the pulse. Pulse profile measurements
provide a time domain (CW frequency) view of the pulse envelope. Profiling is
performed using a measurement technique that "walks" a narrow receiver
"snapshot" across the width of the pulse. This is analogous to using a camera
to take many small snapshots of a wide image, then piecing them together to
form a single, panoramic view.  
---|---  
  
####  VB Syntax

|  pulseMeas.PulseProfileStop = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
value |  (double) - Stop time in seconds. Note: The stop value cannot be negative.  
  
#### Return Type

|  Double  
  
#### Default

|  N/A  
  
#### Examples

|  pulseMeas.PulseProfileStop = 3e-3 'Write  
startprofile = pulseMeas.PulseProfileStop 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PulseProfileStop(double *pVal)  
HRESULT put_PulseProfileStop(double pVal)  
  
#### Interface

|  IPulseMeasControl3  
  
* * *

