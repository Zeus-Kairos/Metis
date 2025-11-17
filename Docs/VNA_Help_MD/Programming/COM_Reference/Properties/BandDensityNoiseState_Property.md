##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityNoiseState Property

* * *

#### Description

| Sets and reads the band noise density marker state.  
---|---  
  
####  VB Syntax

| mkr.BandDensityNoiseState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Enum as NAStates) Choose from: naOFF (or 0) - Turn band noise density marker OFF naON (or 1) - Turn band noise density marker ON  
  
#### Return Type

| Boolean  
  
#### Default

| naOFF  
  
#### Examples

| mkr.BandDensityNoiseState = 0  Write value = mkr.BandDensityNoiseState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityNoiseState(tagNAStates* pState) HRESULT
put_BandDensityNoiseState(tagNAStates pState)  
  
#### Interface

| IMarker8  
  
* * *

