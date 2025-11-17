##### Read/Write

|

#####  
  
---|---  
  
## UseCalWindow Property - Obsolete

* * *

#### Description

|  Replaced with [Custom Cal Window](../../CalTopic.md#CustomWindow)
commands. Turns Calibration window ON or OFF during a calibration. [Learn
more.](../../../S3_Cals/Calibration_Wizard.htm#CalWindow)  
---|---  
  
#### VB Syntax

|  guidedCal.UseCalWindow = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
value |  (Boolean) True Show calibration window False Hide calibration window  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Example

|  guided.UseCalWindow = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UseCalWindow(VARIANT_BOOL* val); HRESULT
put_UseCalWindow(VARIANT_BOOL newVal);  
  
#### Interface

|  IGuidedCalibration  
  
* * *

  

