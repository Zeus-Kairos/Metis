##### Write/Read

|

##### [About
Titles](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#title_bars)  
  
---|---  
  
## TitleState Property

* * *

#### Description

|  Turns ON and OFF the window title. Write a window title with
[Title](Title_Property.md)  
---|---  
  
####  VB Syntax

|  win.TitleState = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NaWindow (object)  
state |  (boolean) True \- Title ON False \- Title OFF  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  win.TitleState = True 'Write  
titlestate = win.TitleState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_TitleState(VARIANT_BOOL* bState)  
HRESULT put_TitleState(VARIANT_BOOL bState)  
  
#### Interface

|  INAWindow

