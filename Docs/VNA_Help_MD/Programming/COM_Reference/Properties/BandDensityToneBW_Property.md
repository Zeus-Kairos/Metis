##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityToneBW Property

* * *

#### Description

| Sets and reads the bandwidth of the band tone density marker.  
---|---  
  
####  VB Syntax

| mkr.BandDensityToneBW = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Double) Choose a bandwidth  
  
#### Return Type

| Double  
  
#### Default

| 1 MHz  
  
#### Examples

| mkr.BandDensityToneBW = 1e6 'Write value = mkr.BandDensityToneBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityToneBW(double* pVal) HRESULT
put_BandDensityToneBW(double newVal)  
  
#### Interface

| IMarker8  
  
* * *

