##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# BandDensityEQSPan Property

* * *

#### Description

| Sets and reads the frequency span used by Power Density to normalize the
power.  
---|---  
  
####  VB Syntax

| mkr.BandDensityEQSPan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr | A [Marker](../Objects/Marker_Object.md) (object)  
value | (Double) Choose a span  
  
#### Return Type

| Double  
  
#### Default

| 1 MHz  
  
#### Examples

| mkr.BandDensityEQSPan = 1e6 'Write value = mkr.BandDensityEQSPan 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_BandDensityEQSPan(double* pVal) HRESULT
put_BandDensityEQSPan(double newVal)  
  
#### Interface

| IMarker8  
  
* * *

