#### Write-only

|

#####  
  
---|---  
  
## CreateCustomCal Method

* * *

#### Description

|  Creates a custom cal object.  
---|---  
  
#### VB Syntax

|  calmgr.CreateCustomCal(CalType)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  [Cal Manager](../Objects/CalManager_Object.md) (Object)  
CalType |  (String) Name of the calibration. Choose from: "VMC" or "VectorMixerCal.VMCType" "SMC" or "ScalarMixerCal.SMCType" See Also [SMCType](../Objects/SMC_Type_Object.md) Object [VMCType](../Objects/VMC_Type_Object.md) Object  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim CalMgr As ICalManager2  
Dim SMC As ISMCType  
Set SMC = CreateCustomCal("SMC") See
[SMC](../../COM_Example_Programs/Create_and_Cal_an_SMC_Measurement.md) and
[VMC](../../COM_Example_Programs/Create_and_Cal_a_VMC_Measurement.md)
examples using this command.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CreateCustomCal( BSTR CustomCal)  
  
#### Interface

|  ICalManager2

