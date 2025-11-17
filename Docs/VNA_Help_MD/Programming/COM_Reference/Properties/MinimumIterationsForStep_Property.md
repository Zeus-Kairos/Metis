##### Read-only  
  
---  
  
## MinimumIterationsForStep Property

* * *

#### Description

|  Designed to be used for an iterative cal standard such as a sliding load,
this command returns the minimum number of required iterative measurement
acquisitions for the specified step. For most connection steps this will
return 1, but for an iterative cal standard such as a sliding load, it will
return a number such as 5. To count acquisition steps, set
[SlidingLoadAcquisitionBehavior](SlidingLoadAcquisitionBehavior_Property.md).  
---|---  
  
####  VB Syntax

|  value = guided.MinimumIterationsForStep (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) Variable to store the returned number of minimum iterations for the step.  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
n |  Guided Cal step number for which to return the number of iterative measurement acquisitions that have been made. Use [GenerateSteps Method](../Methods/GenerateSteps_Method.md) to read the number of steps in the calibration.  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = obj.MinimumIterationsForStep(4)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MinimumIterationsForStep (long step, long *iterations);  
  
#### Interface

|  IGuidedCalibration10  
  
* * *

