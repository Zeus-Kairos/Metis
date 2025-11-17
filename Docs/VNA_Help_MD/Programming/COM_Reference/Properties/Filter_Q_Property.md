##### Read-only

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## FilterQ Property

* * *

#### Description

|  Returns the Q (quality factor) result of the SearchBandwidth method. The Q
factor is the ratio of Center Frequency to Bandwidth (Center Frequency /
Bandwidth).  
---|---  
  
####  VB Syntax

|  filtQ = meas.FilterQ  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
filtQ |  (single) - Variable to store bandwidth Q data  
meas |  A Measurement (object)  
  
#### Return Type

|  Single  
  
#### Default

|  Not applicable  
  
#### Examples

|  filtQ = meas.FilterQ 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_FilterQ(float* quality)  
  
#### Interface

|  IMeasurement

