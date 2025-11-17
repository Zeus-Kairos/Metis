##### Write/Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## MinimumFrequency Property

* * *

#### Description

| Sets and returns the minimum usable frequency specified for the power
sensor.  
---|---  
  
####  VB Syntax

| pwrSensor.MinimumFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensor](../Objects/PowerSensor_Object.md) (Object) or A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value | (double) -Frequency in Hertz.  
  
#### Return Type

| Double  
  
#### Default

| Device dependent  
  
#### Examples

| pwrSensor.MinimumFrequency = 300e3 'Write MinFreq =
pwrSensor).MinimumFrequency 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_MinimumFrequency(double newVal); HRESULT
get_MinimumFrequency(double *pVal);  
  
#### Interface

| IPowerSensor IPowerSensorAsReceiver  
  
* * *

