##### Write/Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
# UncertaintyModel Property

* * *

#### Description

| Sets and returns the name assigned to a specific power meter model among
those available for uncertainty (see
[UncertaintyModelCatalog](UncertaintyModelCatalog_Property.md)).  
---|---  
  
####  VB Syntax

| pwrSensor.UncertaintyModel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensorUncertainty](../Objects/PowerSensorUncertainty_Object.md) (Object)   
value | (String) -Name of power meter model.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| pwrSensor.UncertaintyModel = "N8488A" 'Write value =
pwrSensor.UncertaintyModel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_UncertaintyModel(BSTR pVal); HRESULT get_UncertaintyModel(BSTR
*pVal);  
  
#### Interface

| IPowerSensorUncertainty

