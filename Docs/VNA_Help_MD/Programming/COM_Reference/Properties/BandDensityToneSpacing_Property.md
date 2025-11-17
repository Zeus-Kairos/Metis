##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityToneSpacing Property

* * *

#### Description

| Sets and reads the tone density tone spacing.  
---|---  
  
####  VB Syntax

| mkr.BandDensityToneSpacing = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Double) Choose a spacing value.  
  
#### Return Type

| Double  
  
#### Default

| 1 MHz  
  
#### Examples

| mkr.BandDensityToneSpacing = 1e6 'Write value = mkr.BandDensityToneSpacing
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityToneSpacing(double* pVal) HRESULT
put_BandDensityToneSpacing(double newVal)  
  
#### Interface

| IMarker8  
  
* * *

