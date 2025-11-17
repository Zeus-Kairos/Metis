##### Read-only

|

##### [About Cal All](../../../S3_Cals/Calibrate_All_Channels.md)  
  
---|---  
  
## SParameterCalPorts Property

* * *

#### Description

|  Read the final list of ports that will be fully calibrated by Calibrate All
Channels. For the returned list of ports, specify connectors and cal kits for
the calibration using the [GuidedCal](../Objects/GuidedCalibration_Object.md)
commands. Ports to received ONLY a power cal (such as mixer LO ports) will NOT
be on the returned list. For each channel, specify the ports to be calibrated
using [CalibrationPorts Property](CalibrationPorts_Property.md)  
---|---  
  
####  VB Syntax

|  ports = calAll.SParameterCalPorts  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ports |  (Variant Array) Ports to be calibrated.  
calAll |  A [CalibrateAllChannels](../Objects/CalibrateAllChannels_Object.md) (object)  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ports = calAll.SParameterCalPorts 'returns the ports to be cal'd  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SParameterCalPorts([out,retval] VARIANT* calports);  
  
#### Interface

|  ICalibrateAllChannels  
  
* * *

