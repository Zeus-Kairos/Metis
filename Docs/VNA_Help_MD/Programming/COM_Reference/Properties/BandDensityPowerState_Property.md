##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityPowerState Property

* * *

#### Description

| Sets and reads the band power density state.  
---|---  
  
####  VB Syntax

| mkr.BandDensityPowerState = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Enum as NAStates) Choose from: naOFF (or 0) - Turn band power density marker OFF naON (or 1) - Turn band power density marker ON  
  
#### Return Type

| Boolean  
  
#### Default

| naOFF  
  
#### Examples

| mkr.BandDensityPowerState = 0  Write value = mkr.BandDensityPowerState 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityPowerState(tagNAStates* pState) HRESULT
put_BandDensityPowerState(tagNAStates pState)  
  
#### Interface

| IMarker8  
  
* * *

