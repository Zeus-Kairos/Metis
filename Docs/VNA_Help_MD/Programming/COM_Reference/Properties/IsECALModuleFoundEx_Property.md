##### Read only

|

##### [About ECAL](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## IsECALModuleFoundEx Property

* * *

#### Description

|  This property replaces [IsECALModuleFound
Property](IsECALModuleFound_Property.htm). Returns true or false depending on
whether communication was established between the VNA and the specified ECal
module.  
---|---  
  
####  VB Syntax

|  modFound = cal.IsECALModuleFoundEx (module)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
modFound |  (boolean) - Variable to store the returned test result. True - The VNA identified the presence of the specified ECal module. False \- The VNA did NOT identify the presence of the specified ECal module.  
cal |  (object) - A Calibrator object  
module |  (long integer)  ECal module. Choose from modules 1 through 8 Use [GetECALModuleInfoEx](../Methods/Get_ECALModuleInfoEx_Method.md) to return the model and serial number of each module.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not applicable  
  
#### Examples

|  Set cal = pna.ActiveChannel.Calibrator moduleFound =
cal.IsECALModuleFoundEx(1)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IsECALModuleFoundEx( long moduleNumber, VARIANT_BOOL
*bModuleFound);  
  
#### Interface

|  ICalibrator4

