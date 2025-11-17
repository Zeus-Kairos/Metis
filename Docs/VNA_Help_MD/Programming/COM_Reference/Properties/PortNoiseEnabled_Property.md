##### Read/Write

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# PortNoiseEnabled Property

* * *

#### Description

|  Sets and returns the ON/OFF state of allowing noise data to contribute to
the uncertainty of a calibration performed using Dynamic Uncertainty. Noise
data must also be present for the ports at the time the calibration is
performed.  
---|---  
  
#### VB Syntax

|  uncertMan.PortNoiseEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncertMan |  An [UncertaintyManager](../Objects/UncertaintyManager_Object.md) Object  
value |  (Boolean) Noise contribution state. Choose from: True \- Noise uncertainty ON. False \- Noise uncertainty OFF.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  uncertMan.PortNoiseEnabled = True [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PortNoiseEnabled([out,retval] VARIANT_BOOL* pState); HRESULT
put_PortNoiseEnabled([in] VARIANT_BOOL state);  
  
#### Interface

|  IUncertaintyManager  
  
* * *

