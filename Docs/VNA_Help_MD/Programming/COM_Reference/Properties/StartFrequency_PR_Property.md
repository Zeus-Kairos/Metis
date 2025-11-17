##### Write/Read

|

##### [About Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm)  
  
---|---  
  
## StartFrequency Property

* * *

#### Description

|  Sets and returns the phase reference cal start frequency.  
---|---  
  
####  VB Syntax

|  phasRef.StartFrequency = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
phasRef |  A [PhaseReferenceCalibration](../Objects/PhaseReferenceCalibration_Object.md) Object  
  
#### value

|  Start frequency in Hz. Choose any frequency from 17.5 MHz to the stop
frequency of the VNA.  
  
#### Return Type

|  Double  
  
#### Default

|  17.5e6  
  
#### Examples

|  phase.StartFrequency = 20e6 [See example
program](../../COM_Example_Programs/Perform_an_SMC_Phase_Reference_Cal.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_StartFrequency(Double* pVals); HRESULT
put_StartFrequency(Double pVals);  
  
#### Interface

|  IPhaseReferenceCalibration  
  
* * *

