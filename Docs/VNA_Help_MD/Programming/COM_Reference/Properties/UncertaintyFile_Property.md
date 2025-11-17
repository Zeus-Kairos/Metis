##### Write/Read

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)

##### [About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
  
---|---  
  
# UncertaintyFile Property

* * *

#### Description

| Sets and returns a custom model uncertainty file containing all of the power
meter uncertainty properties. When this command is executed, the model name is
automatically set to "CustomFile".  
---|---  
  
####  VB Syntax

| pwrSensor.UncertaintyFile = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor | A [PowerSensorUncertainty](../Objects/PowerSensorUncertainty_Object.md) (Object)   
value | (String) -Custom file name.  
  
#### Return Type

| String  
  
#### Default

| Not Applicable  
  
#### Examples

| pwrSensor.UncertaintyFile = "C:\U8485A_MY55140018.dat" 'Write value =
pwrSensor.UncertaintyFile 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_UncertaintyFile(BSTR *pVal); HRESULT get_UncertaintyFile(BSTR
pVal);  
  
#### Interface

| IPowerSensorUncertainty

