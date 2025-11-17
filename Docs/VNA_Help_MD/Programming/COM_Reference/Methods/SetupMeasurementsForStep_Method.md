##### Write-only

|

##### [About Cal Window](../../../S3_Cals/Calibration_Wizard.md#CalWindow)  
  
---|---  
  
## SetupMeasurementsForStep Method

* * *

#### Description

|  Show the Cal Window, and optionally one or more other specific windows,
before acquiring a Cal standard. This command will cause the Cal Window to
display the specific measurements that are to be made for that particular Cal
standard. [See custom Cal window commands.](../../CalTopic.md#CustomWindow)  
---|---  
  
####  VB Syntax

|  guidedCal.SetupMeasurementsForStep (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
n |  Step number in the calibration process. Use [GenerateSteps](GenerateSteps_Method.md) to determine the total number of steps. Use [GetStepDescription](Get_StepDescription_Method.md) to read the description of each step.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  guidedCal.SetupMeasurementsForStep 3 [See example using this
command](../../COM_Example_Programs/Show_Custom_Window_during_Calibration.htm)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetupMeasurementsForStep(long step);  
  
#### Interface

|  IGuidedCalibration4  
  
* * *

