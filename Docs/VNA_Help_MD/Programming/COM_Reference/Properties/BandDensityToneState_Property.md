##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityToneState Property

* * *

#### Description

| Sets and reads the band tone density state.  
---|---  
  
####  VB Syntax

| mkr.BandDensityToneState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Enum as NAStates) Choose from: naOFF (or 0) - Turn band tone density marker OFF naON (or 1) - Turn band tone density marker ON  
  
#### Return Type

| Boolean  
  
#### Default

| naOFF  
  
#### Examples

| mkr.BandDensityToneState = 0  Write value = mkr.BandDensityToneState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityToneState(tagNAStates* pState) HRESULT
put_BandDensityToneState(tagNAStates pState)  
  
#### Interface

| IMarker8  
  
* * *

