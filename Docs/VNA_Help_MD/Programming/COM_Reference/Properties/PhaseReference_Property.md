##### Write/Read

|

##### [About Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## PhaseReference Property

* * *

#### Description

|  Sets and returns the Phase Reference ID to be used for the Phase Reference
calibration. Use
[GetConnectedPhaseReferences](../Methods/GetConnectedPhaseReferences_Method.md)
to read the phase references currently connected to the VNA USB.  
---|---  
  
####  VB Syntax

|  phasRef.PhaseReference = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phasRef |  A [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) Object  
  
#### value

|  (String) Phase Reference ID name.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  phase.PhaseReference = "MYPRT0001" [See example
program](../../COM_Example_Programs/Perform_an_SMC_Phase_Reference_Cal.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PhaseReference(BSTR PhaseReference* pVals); HRESULT
put_PhaseReference(BSTR PhaseReference newVals);  
  
#### Interface

|  IPhaseReferenceCalibration  
  
* * *

