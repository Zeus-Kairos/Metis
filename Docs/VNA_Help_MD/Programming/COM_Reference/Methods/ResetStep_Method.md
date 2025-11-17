##### Write-only  
  
---  
  
## ResetStep Method

* * *

#### Description

|  Resets the specified guided cal connection step as unmeasured. This clears
all previous measurements made for that step.  
---|---  
  
####  VB Syntax

|  guided.ResetStep (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
n |  Guided Cal step number to reset as unmeasured. Use [GenerateSteps Method](GenerateSteps_Method.md) to read the number of steps in the calibration.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  obj.ResetStep(4)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ResetStep(long step);  
  
#### Interface

|  IGuidedCalibration10  
  
* * *

