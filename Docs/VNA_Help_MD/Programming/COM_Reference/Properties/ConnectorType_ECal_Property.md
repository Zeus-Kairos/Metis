##### Read / Write

|

##### [About User
Characterization](../../../S3_Cals/ECal_User_Characterization.htm)  
  
---|---  
  
## ConnectorType Property

* * *

#### Description

|  Sets or queries the connector type for the specified port.  
---|---  
  
#### VB Syntax

|  ecalUser.ConnectorType (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
ecalUser |  An [ECalUserCharacterizer](../Objects/ECalUserCharacterizer_Object.md) (object)  
port |  (Enum) ECal port for which connector type is to be set. Choose from: 1 or naECalPort_A 2 or naECalPort_B 3 or naECalPort_C 4 or naECalPort_D  
  
#### value

|  (String) - Connector type. When the User Characterization is to be stored
in the ECal module, then the connector type is limited to a Factory-defined
connector type. [See the
list](../../../S3_Cals/Connectors_Tab.htm#Connectors). When the User
Characterization is to be stored in VNA disk memory, then the connector type
can also be a User-defined connector type.  
  
#### Return Type

|  String  
  
#### Default

|  "" (Empty String)  
  
#### Examples

|  ecalUser.ConnectorType(naECalPort_B) = "APC 3.5 male" ' Write  
Value = ecalUser.ConnectorType(naECalPort_B)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ConnectorType(NAECalPort port, BSTR *connector); HRESULT
put_ConnectorType(NAECalPort port, BSTR connector);  
  
#### Interface

|  IECalUserCharacterizer  
  
* * *

