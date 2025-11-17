##### Write-only

|

##### [About Modifying Cal Kits](../../../S2_Opt/Trce_Noise.md#averaging)  
  
---|---  
  
## BuildHybridKit Method

* * *

#### Description

|  Use this method when you have different port connectors. This is a
convenient way to combine two kits that match the connectors on your DUT.  
---|---  
  
####  VB Syntax

|  app.BuildHybridKit port1Kit,p1sex,port2Kit,p2sex,adapter,user kit  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
port1Kit  
port2Kit |  (enum NACalKit) - Specifies the two kits to be used to build the hybrid kit. Choose from: naCalKit_85032F_N50  
naCalKit_85033E_3_5  
naCalKit_85032B_N50  
naCalKit_85033D_3_5  
naCalKit_85038A_7_16  
naCalKit_85052C_3_5_TRL  
naCalKit_User7  
naCalKit_User8  
naCalKit_User9  
naCalKit_User10  
p1sex  
p2sex |  (enum NAPortSex) - Specifies the sex of the connector at that port. Choose from:  
naMale  
naFemale  
naDon'tCare  
adapter |  (enum NAAdapter) -Choose from:  
naUserkit - the electrical length of the adapter in the userKit specifications  
naZeroLength \- no adapter  
userKit |  (enum NACalKit) \- The Hybrid kit - Choose from the previous list of kits  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.BuildHybridKit naCalKit_85033E_3_5,naMale,naCalKit_85038A_7_16  
,naFemale,naUserkit,naCalKit_User8  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT BuildHybridKit/(tagNACalKit port1Kit, tagNAPortSex port1Sex,
tagNACalKit port2Kit, tagNAPortSex port2Sex, tagNAAdapter adapter, tagNACalKit
userKit)  
  
#### Interface

|  IApplication

