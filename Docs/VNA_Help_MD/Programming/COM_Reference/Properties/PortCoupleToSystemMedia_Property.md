##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortCoupleToSystemMedia Property

* * *

#### Description

| Sets and returns the state of coupling with the system Media type.  
---|---  
  
####  VB Syntax

| fixture.PortCoupleToSystemMedia (port)= value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture | A [Fixturing](../Objects/Fixturing_Object.md) Object  
value | (Boolean) Coupling state. Choose from:

  * True \- Media type is coupled with the system setting.
  * False \- Media type is NOT coupled with the system setting.

  
  
#### Return Type

| Boolean  
  
#### Default

| True  
  
#### Examples

| fixture.PortCoupleToSystemMedia= True  
bool = fixture.PortCoupleToSystemMedia  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_PortCoupleToSystemMedia(VARIANT_BOOL *pVal); HRESULT
put_PortCoupleToSystemMedia(VARIANT_BOOL newVal);  
  
#### Interface

| IFixturing4  
  
* * *

