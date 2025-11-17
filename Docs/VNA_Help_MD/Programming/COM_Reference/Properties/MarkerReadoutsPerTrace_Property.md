##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerReadoutsPerTrace Property

* * *

#### Description

|  Sets the number of marker readouts to display per trace. Display up to 20
marker readouts per window.  
---|---  
  
####  VB Syntax

|  win.MarkerReadoutsPerTrace = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Long Integer) Number of marker readouts to display. Choose a value between 1 and 10.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  5  
  
#### Examples

|  win.MarkerReadoutsPerTrace = 3 'Write value =
app.ActiveNAWindow.MarkerReadoutsPerTrace 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutsPerTrace(long *pVal) HRESULT
put_MarkerReadoutsPerTrace(long newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

