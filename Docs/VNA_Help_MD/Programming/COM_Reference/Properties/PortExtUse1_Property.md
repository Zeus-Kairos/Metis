##### Write/Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md#PortDiag)  
  
---|---  
  
## PortExtUse1 Property

* * *

#### Description

|  Sets and returns the Use1 ON/OFF state for the use of the
[PortLoss1](PortLoss1_Property.md) and [PortFreq1](PortFreq1_Property.md)
values for the specified port number. Note: This command affects ALL
measurements on the channel.  
---|---  
  
####  VB Syntax

|  fixture.PortExtUse1(port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture |  A [Fixturing](../Objects/Fixturing_Object.md) (object)  
port |  (Integer) Port number to receive Use1 ON / OFF state.  
value |  (Boolean) False - Turns Use1 OFF True - Turns Use1 ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  fixture.PortExtUse1(2) = False 'Write  
value = fixture.PortExtUse1(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PortExtUse1(short port VARIANT_BOOL *pVal)  
HRESULT put_PortExtUse1(short port VARIANT_BOOL newVal)  
  
#### Interface

|  IFixturing

