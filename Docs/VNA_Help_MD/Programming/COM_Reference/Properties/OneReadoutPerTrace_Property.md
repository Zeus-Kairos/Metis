##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#DisplayDiag)  
  
---|---  
  
## OneMarkerReadoutPerTrace Property - Superseded

* * *

#### Description

|  Either show marker readout of only the active trace or all of the traces
simultaneously. Note: This method is replaced by [MarkerReadoutsPerTrace
Property](MarkerReadoutsPerTrace_Property.htm)  
---|---  
  
####  VB Syntax

|  win.OneReadoutPerTrace = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (boolean) True \- Shows the readout of only the active marker for each trace. False \- Shows up to 5 marker readouts per trace, up to 20 total readouts.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  win.OneMarkerReadoutPerTrace = True 'Write State =
app.ActiveNAWindow.OneMarkerReadoutPerTrace 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_OneMarkerReadoutPerTrace(VARIANT_BOOL *pVal) HRESULT
put_OneMarkerReadoutPerTrace(VARIANT_BOOL newVal)  
  
#### Interface

|  INAWindow

