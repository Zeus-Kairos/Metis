##### Write/Read

|

##### About Pulse Measurements  
  
---|---  
  
# PulseProfileStart Property

* * *

#### Description

|  Sets and returns the start time of the pulse. Pulse profile measurements
provide a time domain (CW frequency) view of the pulse envelope. Profiling is
performed using a measurement technique that "walks" a narrow receiver
"snapshot" across the width of the pulse. This is analogous to using a camera
to take many small snapshots of a wide image, then piecing them together to
form a single, panoramic view.  
---|---  
  
####  VB Syntax

|  pulseMeas.PulseProfileStart = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pulseMeas |  A [PulseMeasurementControl](../Objects/PulseMeasControl_Object.md) (object)  
value |  (double) - Start time in seconds. Note: The start value cannot be negative.  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  pulseMeas.PulseProfileStart = 3e-3 'Write  
startprofile = pulseMeas.PulseProfileStart 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PulseProfileStart(double *pVal)  
HRESULT put_PulseProfileStart(double pVal)  
  
#### Interface

|  IPulseMeasControl3  
  
* * *

