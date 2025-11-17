##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## UsePowerLossSegments Property

* * *

#### Description

| Specifies if subsequent power readings will use of the loss table.
(PowerLossSegments).  
---|---  
  
####  VB Syntax

| pwrCal.UsePowerLossSegments = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal | A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object) A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object) A [PowerSensor](../Objects/PowerSensor_Object.md) (Object)  
value | (boolean) False  Do not use loss table True  Use loss table  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| pwrSens.UsePowerLossSegments = True 'Write  
lossTableState = pwrSens.UsePowerLossSegments 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_UsePowerLossSegments(VARIANT_BOOL bState); HRESULT
get_UsePowerLossSegments(VARIANT_BOOL *bState);  
  
#### Interface

| ISourcePowerCalibrator IPowerSensorAsReceiver IPowerSensor  
  
* * *

