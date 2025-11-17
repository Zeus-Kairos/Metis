##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityACPRState Property

* * *

#### Description

| Sets and reads the ACPR density marker.  
---|---  
  
####  VB Syntax

| mkr.BandDensityACPRState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Enum as NAStates) Choose from: naOFF (or 0) - Turn ACPR density marker OFF naON (or 1) - Turn ACPR density marker ON  
  
#### Return Type

| Boolean  
  
#### Default

| naOFF  
  
#### Examples

| mkr.BandDensityACPRState = 0  Write value = mkr.BandDensityACPRState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityACPRState(tagNAStates* pState) HRESULT
put_BandDensityACPRState(tagNAStates pState)  
  
#### Interface

| IMarker9  
  
* * *

