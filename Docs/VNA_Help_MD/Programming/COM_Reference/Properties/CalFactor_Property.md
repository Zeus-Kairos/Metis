##### Write / Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## CalFactor Property

* * *

#### Description

| Sets or returns the cal factor value associated with a power sensor cal
factor segment.  
---|---  
  
#### VB Syntax

| calFactSeg.CalFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calFactSeg | A [PowerSensorCalFactorSegment](../Objects/PowerSensorCalFactorSegment_Object.md) (Object) or A [PowerSensorCalFactorSegmentPMAR](../Objects/PowerSensorCalFactorSegmentPMAR_Object.md) (Object)  
value | (double)  Cal factor in percent. Choose any value between 1 and 150  
  
#### Return Type

| Double  
  
#### Default

| 0  
  
#### Examples

| calFactSeg.CalFactor = 98 'Write  
factor = calFactSeg.CalFactor 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_CalFactor(Double newVal); HRESULT get_CalFactor(Double *pVal);  
  
#### Interface

| IPowerSensorCalFactorSegment  
  
* * *

Last Modified:

  

