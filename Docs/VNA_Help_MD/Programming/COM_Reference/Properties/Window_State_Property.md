##### Write/Read

|

##### [About Arranging
Windows](../../../S0_Start/Traces_Channels_and_Windows.htm#Window_Layout)  
  
---|---  
  
## WindowState Property

* * *

#### Description

|  Sets or returns the window setting of Maximized, Minimized, or Normal. To
arrange all of the windows, use
app.[ArrangeWindows.](Arrange_Windows_Property.md)  
---|---  
  
####  VB Syntax

|  object.WindowState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [Application](../Objects/Application_Object.md) (object) - main window  
or  
A NaWindow (object) \- data windows  
value |  (enum NAWindowStates) \- The window state. Choose from:  
0 - naMinimized \- Minimizes the window to an Icon on the lower toolbar  
1 - naMaximized \- Maximizes the window  
2 - naNormal \- changes the window size to the user defined setting (between
Max and Min).  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naMaximized  
  
#### Examples

|  app.WindowState = naMinimized 'changes the Network Analyzer application
window to an icon. -Write  
win.WindowState = naNormal 'changes the window defined by the win object
variable to user defined settings. -Write  
winstate = app.WindowState 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_WindowState(tagNAWindowStates *pVal)  
HRESULT put_WindowState(tagNAWindowStates newVal)  
  
#### Interface

|  INAWindow  
IApplication

