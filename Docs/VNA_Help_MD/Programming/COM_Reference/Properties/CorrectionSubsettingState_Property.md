##### Read/Write

|

#####  
  
---|---  
  
## CorrectionSubsettingState Property

* * *

#### Description

| Set and return the ON/OFF subset correction state. [Learn
more](../../../S3_Cals/Guided_Power_Calibration.htm#MatchingDialog).  
---|---  
  
####  VB Syntax

| corrMethods.CorrectionSubsettingState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
corrMethods | [CorrectionMethods](../Objects/CorrectionMethods_Object.md) (object)  
value | (Boolean) True Turns subset correction ON False Turns subset correction OFF  
  
#### Return Type

| Boolean  
  
#### Default

| True (-1)  
  
#### Example

| corrMethods.CorrectionSubsettingState = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_CorrectionSubsettingState(BOOL *state); HRESULT
put_CorrectionSubsettingState(BOOL state);  
  
#### Interface

| ICorrectionMethods2  
  
* * *

