##### Read/Write

|

##### [About Guided Power Cal](../../../S3_Cals/Guided_Power_Calibration.md)  
  
---|---  
  
## PerformPowerCalibration Property

* * *

#### Description

|  Enables Guided Power Cal and sets the source port to be calibrated.  
---|---  
  
#### VB Syntax

|  guidedCal.PerformPowerCalibration (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
port |  (Long integer) Source port to be calibrated. ONLY one port may be calibrated with a Guided Power Cal.  
value |  (Boolean) True Perform a Guided Power Calibration. False Do NOT perform a Guided Power Calibration  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Example

|  guided.PerformPowerCalibration(1) = True [See example
program](../../COM_Example_Programs/Perform_a_Comprehensive_Guided_2-Port_Cal.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PerformPowerCalibration(long port,VARIANT_BOOL* val); HRESULT
put_PerformPowerCalibration(long port,VARIANT_BOOL newVal);  
  
#### Interface

|  IGuidedCalibration7  
  
* * *

