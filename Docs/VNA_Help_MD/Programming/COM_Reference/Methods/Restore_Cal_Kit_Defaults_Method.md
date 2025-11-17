##### Write-only

|

##### [About Modifying Cal Kits](../../../S3_Cals/ModifyCalKits.md#calkitmod)  
  
---|---  
  
## RestoreCalKitDefaults Method

* * *

#### Description

|  Restores the original properties of the specified Cal Kit, overwritting the
last definition with the factory defaults. NOTE: ONLY works with VNA releases
1.0 through 1.6.  
---|---  
  
####  VB Syntax

|  app.RestoreCalKitDefaults (calKit)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
calKit |  (enum NACalKit) - Calibration Kit to restore. Choose from: 1 - naCalKit_85032F_N50  
2 - naCalKit_85033E_3_5  
3 - naCalKit_85032B_N50  
4 - naCalKit_85033D_3_5  
5 - naCalKit_85038A_7_16  
6 - naCalKit_85052C_3_5_TRL  
7 - naCalKit_User7  
8 - naCalKit_User8  
9 - naCalKit_User9  
10 - naCalKit_User10  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.RestoreCalKitDefaults naCalKit_MechKit10  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT RestoreCalKitDefaults/(tagNACalKit kit)  
  
#### Interface

|  IApplication

