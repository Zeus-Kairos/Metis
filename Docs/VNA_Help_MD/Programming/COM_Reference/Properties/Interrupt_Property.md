##### Read-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## Interrupt Property

* * *

#### Description

|  Reads the boolean that represents the state of the Interrupt In line (pin
13) on the external test set connector.  
---|---  
  
####  VB Syntax

|  value = ExtIO.Interrupt  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) \- Variable to store the returned data  
ExtIO |  (object) - An ExternalTestSetIO object  
  
#### Return Type

|  Boolean False \- indicates the line is being held at a TTL High True \-
indicates the line is being held at a TTL Low  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = ExtIO.Interrupt  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Interrupt( VARIANT_BOOL* bValue);  
  
#### Interface

|  IHWExternalTestSetIO

