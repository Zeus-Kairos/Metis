##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerSymbol Property

* * *

#### Description

|  Sets the symbol to display for marker position.  
---|---  
  
####  VB Syntax

|  win.MarkerSymbol = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Enum as naMarkerSymbol) Choose from: 0 - naMarkerSymbolTriangle 1 - naMarkerSymbolFlag 2 \- naMarkerSymbolLine [See pictures of symbols](../../../S4_Collect/Markers.md#DisplayDiag)  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naMarkerSymbolTriangle  
  
#### Examples

|  win.MarkerSymbol = naMarkerSymbolLine 'Write value =
app.ActiveNAWindow.MarkerSymbol 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerSymbol(double *pVal) HRESULT put_MarkerSymbol(double
newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

