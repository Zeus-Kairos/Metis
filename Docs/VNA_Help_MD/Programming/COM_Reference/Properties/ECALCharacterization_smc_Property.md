##### Write/Read

## ECALCharacterization Property - Superseded

* * *

#### Description

|  Note: This command is replaced with
[CalKitType](CalKitType_fca_Property.md) which sets the ECal module and User
Characterization. Specifies the characterization data within an ECal module to
be used for the SMC calibration. Learn more about [ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm).  
---|---  
  
####  VB Syntax

|  SMC.ECALCharacterization(mod) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
SMC |  [SMCType](../Objects/SMC_Type_Object.md) (object)  
module |  1- ECal module  
value |  (Long)  Characterization data within the ECal module to be used for ECal operations. Choose from: 0  Factory Characterization 1  UserCharacterization1 2  UserCharacterization2 3  UserCharacterization3 4  UserCharacterization4 5  UserCharacterization5  
  
#### Return Type

|  Long  
  
#### Default

|  0 \- Factory Characterization  
  
#### Examples

|  SMC.ECALCharacterization(1)= 2  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ECALCharacterization( long moduleNumber, long
characterization); HRESULT get_ECALCharacterization( long moduleNumber, long*
characterization);  
  
#### Interface

|  ISMCType

