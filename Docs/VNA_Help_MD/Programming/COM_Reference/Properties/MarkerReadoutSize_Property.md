##### Write/Read

|

##### [About Marker Readout](../../../Support/Configurations.md)  
  
---|---  
  
## MarkerReadoutSize Property

* * *

#### Description

|  Specifies the size of font used when displaying Marker Readout in the
selected window.  
---|---  
  
####  VB Syntax

|  _win_.**MarkerReadoutSize** = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NAWindow (object)  
value |  (enum NAFontSize) 0 - naDefault \- marker readout appears in default font size 1 - naLarge \- marker readout appears in large font size  
  
#### Return Type

|  Long Integer  
  
#### Default

|  naDefault  
  
#### Examples

|  win.MarkerReadoutSize = naDefault 'write default size for marker readout
Dim Size As NAFontSize  
Size = app.ActiveNAWindow.MarkerReadoutSize 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutSize(tagNAFontSize *pVal) HRESULT
put_MarkerReadoutSize(tagNAFontSize newVal)  
  
#### Interface

|  INAWindow

