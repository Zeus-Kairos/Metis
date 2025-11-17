##### Write/Read

|

##### [About
Title](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#title_bars)  
  
---|---  
  
## Title Property

* * *

#### Description

| Writes or reads a custom title for the window. Newer entries replace (not
append) older entries. Turn the title ON and OFF with
[TitleState](Title_State_Property.md)  
---|---  
  
####  VB Syntax

| win.Title = string  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win | A NaWindow (object)  
string | (long) - Title limited to 50 characters.  
  
#### Return Type

| String  
  
#### Default

| Null  
  
#### Examples

| win.Title = "Hello World" 'Write  
titl = win.Title 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_Title(BSTR *title)  
HRESULT put_Title(BSTR title)  
  
#### Interface

| INAWindow

