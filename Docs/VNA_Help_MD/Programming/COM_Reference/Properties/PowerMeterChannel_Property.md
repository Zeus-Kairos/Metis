##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
## PowerMeterChannel Property

* * *

#### Description

|  Identifies which channel of the power meter the power sensor is connected
to.  
---|---  
  
####  VB Syntax

|  chan = powerSensor.PowerMeterChannel  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (enum NAPowerAcquisitionDevice)  Power meter channel identifier for sensor. Choose from: 0  naPowerSensor_A 1  naPowerSensor_B  
pwrSensor |  A [PowerSensor](../Objects/PowerSensor_Object.md) (Object) or A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (Object)  
  
#### Return Type

|  NAPowerAcquisitionDevice  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meterChannel = pwrSensor.PowerMeterChannel  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT PowerMeterChannel(tagNAPowerAcquisitionDevice *pSensor);  
  
#### Interface

|  IPowerSensor IPowerSensorAsReceiver  
  
* * *

