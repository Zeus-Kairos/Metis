##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityPowerBW Property

* * *

#### Description

| Sets and reads the band power density bandwidth.  
---|---  
  
####  VB Syntax

| mkr.BandDensityPowerBW = value  
  
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

| mkr.BandDensityPowerBW = 1e6 'Write value = mkr.BandDensityPowerBW 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityPowerBW(double* pVal) HRESULT
put_BandDensityPowerBW(double newVal)  
  
#### Interface

| IMarker8  
  
* * *

