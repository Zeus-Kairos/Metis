##### Write/Read

|

##### [About Marker Search](../../../S4_Collect/Markers.md#Searching)  
  
---|---  
  
## PeakExcursion Property

* * *

#### Description

|  Sets and reads the peak excursion value for the specified marker. The
Excursion value determines what is considered a "peak".  
---|---  
  
####  VB Syntax

|  mark.PeakExcursion = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (single) - Peak Excursion. Choose any number between -500 and 500  
  
#### Return Type

|  Single  
  
#### Default

|  3  
  
#### Examples

|  mark.PeakExcursion = 1 'Write  
PkExcur = mark.PeakExcursion 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_PeakExcursion(float *pVal)  
HRESULT put_PeakExcursion(float newVal)  
  
#### Interface

|  IMarker

