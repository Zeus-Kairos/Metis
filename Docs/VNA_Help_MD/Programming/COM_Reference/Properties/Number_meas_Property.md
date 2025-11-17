##### Read-only

|

##### [About
Measurements](../../../S0_Start/Traces_Channels_and_Windows.htm#trace)  
  
---|---  
  
## Number (Measurement) Property

* * *

#### Description

|  Returns the Number of the measurement. Measurement numbers are assigned
internally. Note: Measurement numbers are NOT the same as their number in the
Measurements collection. Measurement number is used to identify the
measurement associated with an event. This property is used to identify
measurements when events occur through the
[OnMeasurementEvent](../Events/OnMeasurementEvent.md) callback. For example:
OnMeasurementEvent (naEventId_MSG_LIMIT_FAILED, 3)  
---|---  
  
####  VB Syntax

|  measNum = meas.Number  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measNum |  (long) \- variable to store the measurement number  
meas |  A Measurement (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  "1" \- number of the default measurement  
  
#### Examples

|  measNum = meas.Number  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Number(long *MeasurementNumber)  
  
#### Interface

|  IMeasurement

