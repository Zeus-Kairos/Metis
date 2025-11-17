##### Read-only

|  
---|---  
  
## GetStepDescription Method

* * *

#### Description

|  Returns the description of the specified step in the calibration process.
For an ECal User Characterization this returns the description of the
specified step in the ECal User Characterization process.  
---|---  
  
####  VB Syntax

|  value = obj.GetStepDescription (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (string) - Variable to store the returned number of steps.  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object) [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
  
#### n

|  (Long) Step in the process. Use [GenerateSteps](GenerateSteps_Method.md)
to determine the total number of steps.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = SMC.GetStepDescription(5)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_GetStepDescription(long step, BSTR* str);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType IECalUserCharacterizer  
  
* * *

