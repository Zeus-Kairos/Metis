##### Write-only

|

#####  
  
---|---  
  
## AcquireStep Method

* * *

#### Description

|  Acquire the measurement data for the specified step in the calibration
process. For an ECal User characterization this measures the ECal module.
Note: Guided Cal allows you to measure standards in any order. [See an
example.](../../COM_Example_Programs/Perform_a_Guided_Cal_using_COM.htm)  
---|---  
  
####  VB Syntax

|  obj.AcquireStep (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object) [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object) - Currently, only ONE step is required to measure the ECal module.  
n |  Step number in the calibration process. Use [GenerateSteps](GenerateSteps_Method.md) to determine the total number of steps. Use [GetStepDescription](Get_StepDescription_Method.md) to read the description of each step.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  VMC.AcquireStep (3)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_AcquireStep(long step);  
  
#### Interface

|  SMCType VMCType IGuidedCalibration IECalUserCharacterizer  
  
* * *

