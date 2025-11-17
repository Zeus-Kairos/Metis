##### Write/Read

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## CalibrationPorts Property

* * *

#### Description

|  For each channel to be calibrated, sets and returns the ports to be
calibrated. The port numbers need to be specified only for standard channels.
Apps channels have designated input/output/LO ports.  Select any of the native
VNA ports.  
---|---  
  
####  VB Syntax

|  calAll.CalibrationPorts (chan) = ports  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calAll |  A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
chan |  Channel to be calibrated with a Calibrate All Channels calibration.  
port |  (Variant Array) Ports to be calibrated for the specified channel.  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Standard channels - ports 1 and 2 Apps channels - the designated input and
output ports.  
  
#### Examples

|  calAll.CalibrationPorts(2) = 0 'Ports to calibrate for channel 2 value =
calAll.CalibrationPorts(2) 'returns the ports for channel 2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalibrationPorts (long channel, Variant ports); HRESULT
put_CalibrationPorts (long channel, Variant* ports);  
  
#### Interface

|  ICalibrateAllChannels  
  
* * *

