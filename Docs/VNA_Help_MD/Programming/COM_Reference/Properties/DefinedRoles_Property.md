##### Read only

|

##### [About Meas Class](../../../S1_Settings/Measurement_Classes.md)  
  
---|---  
  
## DefinedRoles Property

* * *

#### Description

|  This command replaces [GetSourceRoles
Method](../Methods/GetSourceRoles_Method.htm). Returns the roles for which
sources can be used for the channel. Use [RoleDevice](RoleDevice_Property.md)
to assign a source to a role.  
---|---  
  
####  VB Syntax

|  value = chan.DefinedRoles  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned channel roles.  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  vRoles = chan.DefinedRoles 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_DefinedRoles(Variant* roles);  
  
#### Interface

|  IChannel22  
  
* * *

* * *

