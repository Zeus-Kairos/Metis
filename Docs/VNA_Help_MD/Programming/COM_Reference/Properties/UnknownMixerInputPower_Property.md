##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## UnknownMixerInputPower Property

* * *

#### Description

|  Sets and returns the input power level to the unknown mixer.  
---|---  
  
####  VB Syntax

|  phaseRef.UnknownMixerInputPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (Double) Input power level in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -15 dBm  
  
#### Examples

|  phaseRef.UnknownMixerInputPower = 0  
value = phaseRef.UnknownMixerInputPower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UnknownMixerInputPower(double *value) HRESULT
put_UnknownMixerInputPower(double value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

