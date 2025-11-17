##### Write/Read

## LocalLockoutState Property

* * *

#### Description

|  Prevents use of the mouse, keyboard, and front panel while your program is
running. Use of these controls while this property is set TRUE causes an error
message on the VNA display. To prevent these messages, see [About Error
Messages](../../../Support/About_Error_Messages.htm).  
---|---  
  
####  VB Syntax

|  app.LocalLockoutState = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
bool |  (boolean) -Choose either: False - User Interface is NOT locked out. True - User Interface IS locked out.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  app.LocalLockoutState = True 'Write  
block = app.LocalLockoutState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LocalLockoutState(VARIANT_BOOL *State);  
HRESULT put_LocalLockoutState(VARIANT_BOOL *State);  
  
#### Interface

|  IApplication4

