##### Write / Read

|

##### [About Port Extensions](../../../S3_Cals/Port_Extensions.md)  
  
---|---  
  
## PortNADistanceUnit Property

* * *

#### Description

| Sets and returns the units for specifying port extension delay in physical
length (distance).  
---|---  
  
####  VB Syntax

| fixture.PortNADistanceUnit = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture | A [Fixturing](../Objects/Fixturing_Object.md) Object  
value | (enum naDistanceUnit) Choose from: 0  naDistanceUnit_Meter 1  naDistanceUnit_Feet 2  naDistanceUnit_Inch  
  
#### Return Type

| Enum  
  
#### Default

| naDistanceUnit_Meter  
  
#### Examples

| fixture.PortNADistanceUnit(2)= naDistanceUnit_Meter 'Write value =
fixture.PortNADistanceUnit(2) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_PortNADistanceUnit(short portNum, tagNADistanceUnit* *pVal);
HRESULT put_PortNADistanceUnit(short portNum, tagNADistanceUnit newVal);  
  
#### Interface

| IFixturing4  
  
* * *

