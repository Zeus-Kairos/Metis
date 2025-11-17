##### Write/Read

|

##### [About Phase Reference
Cals](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## UnknownMixerLOPower Property

* * *

#### Description

|  Sets and returns the LO power level to the unknown mixer.  
---|---  
  
####  VB Syntax

|  phaseRef.UnknownMixerLOPower = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) (object)  
value |  (Double) LO power level in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  10 dBm  
  
#### Examples

|  phaseRef.UnknownMixerLOPower = 10  
value = phaseRef.UnknownMixerLOPower 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UnknownMixerLOPower(double *value) HRESULT
put_UnknownMixerLOPower(double value)  
  
#### Interface

|  IPhaseReference2  
  
* * *

