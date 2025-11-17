##### Read-Write

|

#####  
  
---|---  
  
## Do1PortEcal Property - Superseded

* * *

#### Description

|  Note: This command is replaced with
[CalKitType](CalKitType_fca_Property.md) which sets the ECal module or
mechanical cal kit. Specify ECAL or Mechanical calibration for the mixer
characterization portion of a VMC calibration.  
---|---  
  
#### VB Syntax

|  VMC.Do1PortEcal = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) True \- ECAL False \- Mechanical  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  value = VMC.Do1PortECal  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Do1PortEcal(VARIANT_BOOL bDoEcal); HRESULT
get_Do1PortEcal(VARIANT_BOOL *bDoEcal);  
  
#### Interface

|  VMCType

