##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## OutputSNPFromECal Method

* * *

#### Description

|  Read S parameter of ECal Thru from the ECal memory and save it as s2p file.  
---|---  
  
####  VB Syntax

|  ecalMdls.OutputSNPFromECal (kit, ecalstate, snpfile)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ecalMdls |  (object) - A [ECalModules](../Objects/ECalModules_Collection.md) correction  
kit |  (String) ECal Model, User char name + " ECal", and serial number of the ECal module used for the characterization, separated by spaces. See examples below.  
ecalstate |  (String) ECal transmission path. Choose from AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB or DC.  
snpfile |  (String) Path and filename of the output s2p file name.  
  
#### Return Type

|  IECalModules Set Interface  
  
#### Default

|  Not Applicable  
  
#### Example

|  ecalMdls.OutputSNPFromECal ("N4433A ECal 00001", "BC", "D:\ecalthru.s2p")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT OutputSNPFromECal (BSTRkit, BSTR ecalstate, BSTR snpfile);  
  
#### Interface

|  IECalModules2

