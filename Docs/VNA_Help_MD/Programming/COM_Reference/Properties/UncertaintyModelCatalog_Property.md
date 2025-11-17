##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
# UncertaintyModelCatalog Property

* * *

#### Description

| Returns a list of available power meters that have power uncertainty.  
---|---  
  
####  VB Syntax

| pwrMtrs = pwrSensor.UncertaintyModelCatalog  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrMtrs | (Variant) Variable to store the returned power meters.   
pwrSensor | A [PowerSensorUncertainty](../Objects/PowerSensorUncertainty_Object.md) (Object)   
  
#### Return Type

| Array of strings  
  
#### Default

| Not Applicable  
  
#### Examples

| pwrMtrs = pwrSensor.UncertaintyModelCatalog  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT UncertaintyModelCatalog(VARIANT *pwrMtrs);  
  
#### Interface

| IPowerSensorUncertainty

