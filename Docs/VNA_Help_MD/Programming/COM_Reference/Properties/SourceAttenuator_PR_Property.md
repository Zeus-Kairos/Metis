##### Write/Read

|

##### [About Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## SourceAttenuator Property

* * *

#### Description

|  Sets and returns the Source Attenuator setting for the Phase Reference
calibration. Note: This setting MUST match the source attenuator setting at
the mixer input port for subsequent SMC+Phase measurements.  
---|---  
  
####  VB Syntax

|  phasRef.SourceAttenuator = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phasRef |  A [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) Object  
  
#### value

|  Attenuation value in dB. Choose a valid value for the VNA model. [See valid
settings](../../../Support/Configurations.htm).  
  
#### Return Type

|  Double  
  
#### Default

|  10 dB  
  
#### Examples

|  phase.SourceAttenuator = 0 [See example
program](../../COM_Example_Programs/Perform_an_SMC_Phase_Reference_Cal.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SourceAttenuator(Double* pVals); HRESULT
put_SourceAttenuator(Double pVals);  
  
#### Interface

|  IPhaseReferenceCalibration  
  
* * *

