##### Write/Read

|

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## SensorIndex Property

* * *

#### Description

| For dual sensor power meters, sets and returns the power sensor channel (1
or 2) to be used.  
---|---  
  
####  VB Syntax

| pwrSensor.SensorIndex = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensor](../Objects/PowerSensor_Object.md) (Object) or a [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
value | (Long) \- Power Meter channel. Choose from: 1 \- Sensor A 2 \- Sensor B  
  
#### Return Type

| Long  
  
#### Default

| 1  
  
#### Examples

| pwrSensor.SensorIndex = False 'Write sensor = pwrSensor.SensorIndex 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_SensorIndex(long newVal); HRESULT get_SensorIndex(long* pVal);  
  
#### Interface

| IPowerSensor IPowerSensorAsReceiver  
  
* * *

