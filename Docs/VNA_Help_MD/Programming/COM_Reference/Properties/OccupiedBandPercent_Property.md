##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
# OccupiedBandPercent Property

* * *

#### Description

|  Set and return the percentage of the band power to search for.  
---|---  
  
#### VB Syntax

|  mkr.OccupiedBandPercent = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  99.0  
  
#### Examples

|  mkr.OccupiedBandPercent = 99  'Write  
value = mkr.OccupiedBandPercent 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_OccupiedBandPercent(double pVal); HRESULT
get_OccupiedBandPercent(double* pVal);  
  
#### Interface

|  IMarker7  
  
* * *

