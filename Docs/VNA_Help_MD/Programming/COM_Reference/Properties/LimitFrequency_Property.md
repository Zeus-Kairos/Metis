##### Write/Read

|

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## LimitFrequency Property

* * *

#### Description

| Enable or disable the use of the power meter min and max frequencies.  
---|---  
  
####  VB Syntax

| pwrSensor.LimitFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object) or a [PowerSensor](../Objects/PowerSensor_Object.md) (Object)  
value | (Boolean) \- State of min and max frequency use. Choose from: False \- Min and max frequencies disabled. True \- Min and max frequencies enabled.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| pwrSensor.LimitFrequency = False 'Write limit = pwrSensor.LimitFrequency
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_LimitFrequency(VARIANT_BOOL newVal); HRESULT
get_LimitFrequency(VARIANT_BOOL* pVal);  
  
#### Interface

| IPowerSensorAsReceiver IPowerSensor  
  
* * *

