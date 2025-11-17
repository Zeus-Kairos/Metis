##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# OccupiedBandState Property

* * *

#### Description

|  Sets and returns the occupied bandwidth on/off state.  
---|---  
  
####  VB Syntax

|  mkr.OccupiedBandState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Enum as NaStates) \- Choose from: naOFF (0) - Turns occupied bandwidth OFF. naON (1) - Turns occupied bandwidth ON.  
  
#### Return Type

|  Enum  
  
#### Default

|  naOFF (0)  
  
#### Examples

|  mkr.OccupiedBandState = naON 'Write  
obwstate = mkr.OccupiedBandState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT OccupiedBandState(tag NAStates* pState);  
HRESULT OccupiedBandState(tag NAStates pState)  
  
#### Interface

|  IMarker7 Note: If occupied band state is turned ON, then Band Power or Band
Noise is turned OFF.  
  
* * *

