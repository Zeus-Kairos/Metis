##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerSymbolsAboveTrace Property

* * *

#### Description

|  Specifies whether or not to force marker symbols to be displayed above the
trace. When ON, all marker symbols will be displayed above the trace and the
active marker will be filled solid.  
---|---  
  
####  VB Syntax

|  win.MarkerSymbolsAboveTrace = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Boolean) False \- ONLY the active marker is displayed above the trace. Inactive markers are displayed below the trace. True \- ALL marker symbols are displayed above the trace. The active marker is always filled solid.  
  
#### Return Type

|  Boolean  
  
#### Default

|  OFF (ON in IM Spectrum and SA measurement classes)  
  
#### Examples

|  win.MarkerSymbolsAboveTrace = True 'Write value =
app.ActiveNAWindow.MarkerSymbolsAboveTrace 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerSymbolsAboveTrace(VARIANT_BOOL* pbState) HRESULT
put_MarkerSymbolsAboveTrace(VARIANT_BOOL bState)  
  
#### Interface

|  INAWindow4  
  
* * *

