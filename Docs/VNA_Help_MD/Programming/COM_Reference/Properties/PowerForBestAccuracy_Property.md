##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
# PowerForBestAccuracy Property

* * *

#### Description

| Returns the power level associated with the best accuracy for a specific
power meter.  
---|---  
  
####  VB Syntax

| plevel = pwrSensor.PowerForBestAccuracy  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
plevel | (Double) -Frequency in Hertz.  
pwrSensor | A [PowerSensorUncertainty](../Objects/PowerSensorUncertainty_Object.md) (Object)  
  
#### Return Type

| (Double) Power in dBm.  
  
#### Default

| Not Applicable  
  
#### Examples

| plevel = pwrSensor.PowerForBestAccuracy  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT PowerForBestAccuracy(double *plevel);  
  
#### Interface

| IPowerSensorUncertainty

