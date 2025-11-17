##### Write/Read

|

##### [About Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## CalSet Property

* * *

#### Description

|  Set and read the Cal Set name into which the calibration will be saved. The
phase reference cal can NOT be saved to a cal register. The Cal Set is saved
by calling [GenerateErrorTerms](../Methods/GenerateErrorTerms_Method.md) at
the conclusion of the Guided Cal.  
---|---  
  
####  VB Syntax

|  phasRef.CalSet = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phasRef |  A [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) Object  
  
#### value

|  (String) Cal Set name.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  phase.CalSet = "PhaseRefCal" [See example
program](../../COM_Example_Programs/Perform_an_SMC_Phase_Reference_Cal.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalSet(BSTR CalSet* pVals); HRESULT put_CalSet(BSTR CalSet
newVals);  
  
#### Interface

|  IPhaseReferenceCalibration  
  
* * *

