##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerReadoutYPosition Property

* * *

#### Description

|  Sets the Y-axis position of marker readouts. Readouts are right-justified
at the specified position.  
---|---  
  
####  VB Syntax

|  win.MarkerReadoutYPosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Double) Y-axis position. Choose a value between 1 (bottom) and 10 (top).  
  
#### Return Type

|  Double  
  
#### Default

|  10  
  
#### Examples

|  win.MarkerReadoutYPosition = 3 'Write value =
app.ActiveNAWindow.MarkerReadoutYPosition 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutYPosition(double *pVal) HRESULT
put_MarkerReadoutYPosition(double newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

