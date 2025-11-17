##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerReadoutResponsePlaces Property

* * *

#### Description

|  For the Y-axis (response), sets the number digits to display after the
decimal point in marker readouts.  
---|---  
  
####  VB Syntax

|  win.MarkerReadoutResponsePlaces = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Long Integer) Number of digits to display. Choose a value between 1 and 4.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  2  
  
#### Examples

|  win.MarkerReadoutResponsePlaces = 3 'Write value =
app.ActiveNAWindow.MarkerReadoutResponsePlaces 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutResponsePlaces(long *pVal) HRESULT
put_MarkerReadoutResponsePlaces(long newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

