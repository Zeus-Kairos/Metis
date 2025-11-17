##### Read-Write

|

#####  
  
---|---  
  
## Do2PortEcal Property - Superseded

* * *

#### Description

|  Note: This command is replaced with
[CalKitType](CalKitType_fca_Property.md) which sets the ECal module or
mechanical cal kit. Specify ECAL or Mechanical calibration. For VMC, this
selection only applies to the 2-port calibration portion. For mixer
characterization (VMC), use [Do1PortEcal Property](Do1PortEcal_Property.md)  
---|---  
  
#### VB Syntax

|  object.Do2PortEcal = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  [SMCType](../Objects/SMC_Type_Object.md) (object) or [VMCType](../Objects/VMC_Type_Object.md) (object)  
bool |  (Boolean) True \- ECAL False \- Mechanical  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  value = VMC.Do2PortECal  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Do2PortEcal(VARIANT_BOOL bDoEcal); HRESULT
get_Do2PortEcal(VARIANT_BOOL *bDoEcal);  
  
#### Interface

|  SMCType VMCType

