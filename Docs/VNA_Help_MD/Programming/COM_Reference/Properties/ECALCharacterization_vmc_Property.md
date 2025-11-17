##### Write/Read

## ECALCharacterization Property - Superseded

* * *

#### Description

|  Note: This command is replaced with
[CalKitType](CalKitType_fca_Property.md) which sets the ECal module and User
Characterization. Specifies the characterization data within an ECal module to
be used, and the portion of the VMC calibration. Learn more about [ECal User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm).  
---|---  
  
####  VB Syntax

|  VMC.ECALCharacterization (module,port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
module |  (long integer)  1 \- ECAL module  
port |  (boolean) True \- 2-port calibration portion of the VMC False \- 1-port (mixer characterization portion of the VMC cal)  
value |  (Long)  Characterization data within the ECal module to be used for ECal operations. Choose from: 0  Factory Characterization 1  UserCharacterization1 2  UserCharacterization2 3  UserCharacterization3 4  UserCharacterization4 5  UserCharacterization5  
  
#### Return Type

|  Long  
  
#### Default

|  0 \- Factory Characterization  
  
#### Examples

|  VMC.ECALCharacterization (1,True) = 4  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ECALCharacterization( long moduleNumber, long
characterization); HRESULT get_ECALCharacterization( long moduleNumber, long*
characterization);  
  
#### Interface

|  IVMCType

