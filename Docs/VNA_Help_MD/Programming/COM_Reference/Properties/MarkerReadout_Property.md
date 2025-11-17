##### Write/Read

|

##### [About Marker Readout](../../../Support/Configurations.md)  
  
---|---  
  
## MarkerReadout Property

* * *

#### Description

|  Enables or disables the readout of markers in the window. To show the
marker on the screen use ShowMarkerReadout Method.  
---|---  
  
####  VB Syntax

|  win.MarkerReadout = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NAWindow (object)  
state |  (boolean) True \- enables marker readout  
False \- disables marker readout  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  win.MarkerReadout = True 'Write State = app.ActiveNAWindow.MarkerReadout
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadout(VARIANT_BOOL *pVal)  
HRESULT put_MarkerReadout(VARIANT_BOOL newVal)  
  
#### Interface

|  INAWindow

