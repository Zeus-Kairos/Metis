##### Write-only

|

##### [About Arrange
Windows](../../../S0_Start/Traces_Channels_and_Windows.htm#Window_Layout)  
  
---|---  
  
## ArrangeWindows Property

* * *

#### Description

| Sets the arrangement of all the windows. Overlay, Stack2, Split3 and Quad4
will create windows. To control the state of one window, use
[app.WindowState.](Window_State_Property.md)  
---|---  
  
####  VB Syntax

| app.ArrangeWindows = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | An [Application](../Objects/Application_Object.md) (object)  
value | (enum NAWindowModes) - Choose from: 0 \- naTile  
1 - naCascade  
2 - naOverlay  
3 - naStack2  
4 - naSplit3  
5 - naQuad4  
6 - naTracePerWindow  
7 - naChannelPerWindow  
8 - naLtoR  
  
#### Return Type

| Not Applicable  
  
#### Default

| naTile  
  
#### Examples

| app.ArrangeWindow = naTile 'Write  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT put_ArrangeWindows(tagNAWindowModes newVal)  
  
#### Interface

| IApplication

