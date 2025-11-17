##### Write/Read

|

##### [About Meas Class](../../../S1_Settings/Measurement_Classes.md)  
  
---|---  
  
## RoleDevice Property

* * *

#### Description

|  This command replaces [AssignSourceToRole
Method](../Methods/AssignSourceToRole_Method.htm) and [GetSourceByRole
Method](../Methods/GetSourceByRole_Method.htm). Set and return the source to
be used in the specified role. For example, use this command to set a source
name to be used as the RF2 tone for a Swept IMD channel.  
---|---  
  
####  VB Syntax

|  chan.RoleDevice(role) = source  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  A [Channel](../Objects/Channel_Object.md) (object)  
role |  (String) Role of the source. Not context-sensitive. Use [DefinedRoles](DefinedRoles_Property.md) to read the valid roles for the channel.  
source |  (String) Source name to be used in the specified role. Use [extDevices.Items](Items_Property.md) to read a list of configured sources.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.RoleDevice("RF2") = "MyEsg" 'Write  
source = chan.RoleDevice("RF2") 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_RoleDevice(BSTR role BSTR *source); HRESULT put_RoleDevice(BSTR
role BSTR source);  
  
#### Interface

|  IChannel22  
  
* * *

* * *

