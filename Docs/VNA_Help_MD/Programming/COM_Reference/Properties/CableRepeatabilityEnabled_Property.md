##### Read/Write

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# CableRepeatabilityEnabled Property

* * *

#### Description

|  Sets and returns the ON/OFF state of allowing cable repeatability data to
contribute to the uncertainty of a calibration performed using Dynamic
Uncertainty. Repeatability data must also be present for the ports at the time
the calibration is performed.  
---|---  
  
#### VB Syntax

|  uncertMan.CableRepeatabilityEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncertMan |  An [UncertaintyManager](../Objects/UncertaintyManager_Object.md) Object  
value |  (Boolean) Enable state. Choose from: True \- Cable repeatability uncertainty ON. False \- Cable repeatability uncertainty OFF.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncertMan.CableRepeatabilityEnabled = True [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CableRepeatabilityEnabled([out,retval] VARIANT_BOOL* pState);
HRESULT put_CableRepeatabilityEnabled([in] VARIANT_BOOL state);  
  
#### Interface

|  IUncertaintyManager  
  
* * *

