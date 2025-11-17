##### Read-only

|

##### [About the ExtTestSetIO connector](../../TestSetIO_Connector.md)  
  
---|---  
  
## SweepHoldOff Property

* * *

#### Description

|  Returns a boolean that represents the state of SweepHoldoff line (pin2) of
the External Test Set connector.  
---|---  
  
####  VB Syntax

|  value = ExtIO.SweepHoldOff  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (boolean) \- Variable to store the returned data  
ExtIO |  (object) - An External IO object  
  
#### Return Type

|  Boolean False \- indicates the line is being held at a TTL Low True \-
indicates the line is being held at a TTL High  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = ExtIO.SweepHoldOff  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_SweepHoldOff( VARIANT_BOOL* bValue);  
  
#### Interface

|  IHWExternaTestSetIO

