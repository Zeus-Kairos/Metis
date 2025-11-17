##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
## BandpowerState Property

* * *

#### Description

|  Sets and reads the state of the band noise marker. This command makes a
band noise marker from a generic marker. First turn a marker ON with the
[meas.MarkerState](MarkerState_Property.md) command. Then use this command to
make it a bandpower marker.  
---|---  
  
####  VB Syntax

|  mkr.BandpowerState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Enum as NAStates) Choose from: naOFF (or 0) - Turn band noise marker OFF naON (or 1) - Turn band noise marker ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  naOFF  
  
#### Examples

|  [See example program](../../COM_Example_Programs/Spectrum_Analyzer.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BandpowerState(VARIANT_BOOL* bState) HRESULT
put_BandpowerState(VARIANT_BOOL bState)  
  
#### Interface

|  IMarker6  
  
* * *

