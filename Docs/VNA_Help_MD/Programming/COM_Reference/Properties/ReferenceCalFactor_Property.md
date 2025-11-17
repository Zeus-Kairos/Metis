##### Write/Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## ReferenceCalFactor Property

* * *

#### Description

|  Sets and returns the Cal Factor (%) for the 50 MHz reference signal
associated with this power sensor. Use this property only if the power sensor
does not contain cal factors in EPROM (for example, HP/Keysight 848x sensors).  
---|---  
  
####  VB Syntax

|  pwrSensor.ReferenceCalFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor |  A [PowerSensor](../Objects/PowerSensor_Object.md) (Object) A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value |  (double)  Cal factor in units of percent. This can be any value between 1 and 150.  
  
#### Return Type

|  Double  
  
#### Default

|  100  
  
#### Examples

|  pwrSensor.ReferenceCalFactor = 98 'R RefFact = pwrSensor.ReferenceCalFactor
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ReferenceCalFactor(double newVal); HRESULT
get_ReferenceCalFactor(double *pVal);  
  
#### Interface

|  IPowerSensor IPowerSensorAsReceiver  
  
* * *

