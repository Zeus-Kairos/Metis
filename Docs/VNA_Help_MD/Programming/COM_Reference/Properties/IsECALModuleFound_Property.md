##### Read only

|

##### [About ECAL](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## IsECALModuleFound Property - Superseded

* * *

#### Description

|  Note: This property is replaced by [IsECALModuleFoundEx
Property](IsECALModuleFoundEx_Property.htm). Tests communication between the
VNA and the specified ECal module.  
---|---  
  
####  VB Syntax

|  modFound = cal.IsECALModuleFound (module)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
modFound |  (boolean) - Variable to store the returned test result. True - The VNA identified the presence of the specified ECal module. False \- The VNA did NOT identify the presence of the specified ECal module.  
cal |  (object) - A Calibrator object  
module |  (enum NAECALModule)  ECAL module. Choose from: 0 \- naECALModule_A 1 - naECALModule_B  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not applicable  
  
#### Examples

|  Set cal = pna.ActiveChannel.Calibrator moduleFound =
cal.IsECALModuleFound(naECALModule_A)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsECALModuleFound(tagNAECALModule moduleNumber, VARIANT_BOOL
*bModuleFound);  
  
#### Interface

|  Calibrator

