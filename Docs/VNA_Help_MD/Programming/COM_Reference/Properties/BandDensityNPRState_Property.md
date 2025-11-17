##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityNPRState Property

* * *

#### Description

| Sets and reads the NPR density marker.  
---|---  
  
####  VB Syntax

| mkr.BandDensityNPRState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Enum as NAStates) Choose from: naOFF (or 0) - Turn NPR density marker OFF naON (or 1) - Turn NPR density marker ON  
  
#### Return Type

| Boolean  
  
#### Default

| naOFF  
  
#### Examples

| mkr.BandDensityNPRState = 0  Write value = mkr.BandDensityNPRState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityNPRState(tagNAStates* pState) HRESULT
put_BandDensityNPRState(tagNAStates pState)  
  
#### Interface

| IMarker9  
  
* * *

