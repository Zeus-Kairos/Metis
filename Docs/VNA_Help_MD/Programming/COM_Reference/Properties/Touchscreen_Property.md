##### Write/Read

|

##### [About PNA-X Touchscreen](../../../Front_Panel/XScreen.md)  
  
---|---  
  
## Touchscreen Property

* * *

#### Description

|  Sets and reads the state of the PNA-X Touchscreen (ON and OFF). This
setting remains until changed again from the front-panel or remote command.  
---|---  
  
####  VB Syntax

|  app.Touchscreen = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) False (0) \- Disables use of Touchscreen True (1) \- Enables use of Touchscreen  
  
#### Return Type

|  Boolean False \- OFF True \- ON  
  
#### Default

|  TRUE when shipped from factory.  
  
#### Examples

|  app.Touchscreen = True 'Write  
coupl = app.Touchscreen 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_Touchscreen(VARIANT_BOOL bState) HRESULT
get_Touchscreen(VARIANT_BOOL *bState)  
  
#### Interface

|  IApplication12  
  
* * *

