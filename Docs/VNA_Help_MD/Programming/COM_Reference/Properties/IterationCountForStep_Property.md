##### Read-only  
  
---  
  
## IterationCountForStep Property

* * *

#### Description

|  Designed to be used for an iterative cal standard such as a sliding load,
this command returns the number of iterative measurement acquisitions that has
been made for the specified step. Zero (0) is returned if the step has not yet
been measured. For most cal steps that have already been measured, this
command returns 1. To count acquisition steps, set
[SlidingLoadAcquisitionBehavior](SlidingLoadAcquisitionBehavior_Property.md).  
---|---  
  
####  VB Syntax

|  value = guided.IterationCountForStep (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) Variable to store the returned number of iterations that have been measured for the step.  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
n |  Guided Cal step number for which the acquisition number will be returned. Use [GenerateSteps Method](../Methods/GenerateSteps_Method.md) to read the number of steps in the calibration.  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = obj.IterationCountForStep(4)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IterationCountForStep (long step, long *iterations);  
  
#### Interface

|  IGuidedCalibration10  
  
* * *

