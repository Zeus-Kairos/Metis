##### Read/Write

|

#####  
  
---|---  
  
## MatchCorrectPower Property

* * *

#### Description

|  Turns match-correction ON or OFF. Use this command AFTER performing a
Guided Power Cal. [Learn
more.](../../../S3_Cals/Guided_Power_Calibration.htm#Matching)  
---|---  
  
#### VB Syntax

|  corrMethods.MatchCorrectPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
corrMethods |  [CorrectionMethods](../Objects/CorrectionMethods_Object.md) (object)  
value |  (Boolean) True Turns match-correction ON False Turns match-correction OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Example

|  corrMethods.MatchCorrectPower = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MatchCorrectPower(VARIANT_BOOL* val); HRESULT
put_MatchCorrectPower(VARIANT_BOOL newVal);  
  
#### Interface

|  ICorrectionMethods  
  
* * *

