##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerReadoutXPosition Property

* * *

#### Description

|  Sets the X-axis position of marker readouts. Readouts are right-justified
at the specified position.  
---|---  
  
####  VB Syntax

|  win.MarkerReadoutXPosition = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Double) X-axis position. Choose a value between 1 (far left) and 10 (far right).  
  
#### Return Type

|  Double  
  
#### Default

|  10  
  
#### Examples

|  win.MarkerReadoutXPosition = 3 'Write value =
app.ActiveNAWindow.MarkerReadoutXPosition 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutXPosition(double *pVal) HRESULT
put_MarkerReadoutXPosition(double newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

