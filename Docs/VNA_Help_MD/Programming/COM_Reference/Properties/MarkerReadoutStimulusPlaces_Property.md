##### Write/Read

|

##### [About Marker Readout](../../../S4_Collect/Markers.md#Display)  
  
---|---  
  
## MarkerReadoutStimulusPlaces Property

* * *

#### Description

|  For the X-axis (stimulus), sets the number digits to display after the
decimal point in marker readouts.  
---|---  
  
####  VB Syntax

|  win.MarkerReadoutStimulusPlaces = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A [NAWindow](../Objects/NAWindow_Object.md) (object)  
value |  (Long Integer) Number of digits to display. Choose a value between 2 and 6.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  3  
  
#### Examples

|  win.MarkerReadoutStimulusPlaces = 2 'Write value =
app.ActiveNAWindow.MarkerReadoutStimulusPlaces 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MarkerReadoutStimulusPlaces(long *pVal) HRESULT
put_MarkerReadoutStimulusPlaces(long newVal)  
  
#### Interface

|  INAWindow3  
  
* * *

