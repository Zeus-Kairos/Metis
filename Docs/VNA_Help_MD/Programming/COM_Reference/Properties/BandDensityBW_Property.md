##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityBW Property

* * *

#### Description

| Sets and reads the bandwidth of the band density marker.  
---|---  
  
####  VB Syntax

| mkr.BandDensityBW = value  
  
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

| mkr.BandDensityBW = 1e6 'Write value = mkr.BandDensityBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityBW(double* pVal) HRESULT put_BandDensityBW(double
newVal)  
  
#### Interface

| IMarker8  
  
* * *

