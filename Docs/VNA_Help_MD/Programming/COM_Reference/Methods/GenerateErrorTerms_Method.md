##### Write-only

|

#####  
  
---|---  
  
## GenerateErrorTerms Method

* * *

#### Description

|  Generates the error terms for the specified calibration type, stores the
error terms in a Cal Set, saves the Cal Set, and returns the Cal Set GUID. If
ALL the data for the cal type has NOT been acquired an error message is
returned. Note: The manner in which the calibration is assigned to a Cal Set
(Cal Register or User Cal Set) is determined by the setting of
[RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md).  
---|---  
  
####  VB Syntax

|  value = obj.GenerateErrorTerms  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) - Variable to store the returned GUID or error message.  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  string = SMC.GenerateErrorTerms  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GenerateErrorTerms(BSTR* calsetGUID);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *

