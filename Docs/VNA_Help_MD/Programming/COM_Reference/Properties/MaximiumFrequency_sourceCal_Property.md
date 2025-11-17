##### Write/Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## MaximumFrequency Property

* * *

#### Description

| Set and returns the maximum usable frequency specified for the power sensor.  
---|---  
  
####  VB Syntax

| pwrSensor.MaximumFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensor](../Objects/PowerSensor_Object.md) (Object) or a [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value | (double) -Frequency in Hertz.  
  
#### Return Type

| Double  
  
#### Default

| Device dependent  
  
#### Examples

| pwrSensor.MaximumFrequency = 6e9 'Write MaxFreq = pwrSensor.MaximumFrequency
'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_MaximumFrequency(double newVal); HRESULT
get_MaximumFrequency(double *pVal);  
  
#### Interface

| IPowerSensor IPowerSensorAsReceiver  
  
* * *

