##### Read/Write

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# StandardDefinitionsEnabled Property

* * *

#### Description

|  Sets and returns the ON/OFF state of allowing the uncertainty associated
with the standard definitions in the cal kits to contribute to the uncertainty
of a calibration performed using Dynamic Uncertainty. The uncertainty data for
the Cal standards must also be present at the time the calibration is
performed.  
---|---  
  
#### VB Syntax

|  uncertMan.StandardDefinitionsEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncertMan |  An [UncertaintyManager](../Objects/UncertaintyManager_Object.md) Object  
value |  (Boolean) Enable state. Choose from: True \- Standard definition uncertainty ON. False \- Standard definition uncertainty OFF.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncertMan.StandardDefinitionsEnabled = True [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StandardDefinitionsEnabled([out,retval] VARIANT_BOOL* pState);
HRESULT put_StandardDefinitionsEnabled([in] VARIANT_BOOL state);  
  
#### Interface

|  IUncertaintyManager  
  
* * *

