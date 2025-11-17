##### Read-only

## ECALCharacterizationIndexList Property

* * *

#### Description

|  Returns a list of characterizations stored in the specified ECal module.
Learn more about [ECal](../../../S3_Cals/ECal_User_Characterization.md) User
characterization.  
---|---  
  
####  VB Syntax

|  clist = cal.ECALCharacterizationIndexList (moduleNum)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
clist |  Variable to store the returned list of characterization index numbers.  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
module |  ECal module from which to read user characterization numbers.  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Module 1 contains User Characterizations 1 and 3.  
clist = cal.ECALCharacterizationIndexList(1)  
'Returns the following (0 always indicates the factory characterization):  
0,1,3  
  
#### C++ Syntax

|  HRESULT get_ECALCharacterizationIndexList( long moduleNumber, VARIANT
*characterizations);  
  
#### Interface

|  ICalibrator6

