##### Write/Read

|

##### [About Spectrum Analyzer
Markers](../../../Applications/Spectrum_Analyzer.htm#SA_Markers)  
  
---|---  
  
## BandnoiseSpan Property

* * *

#### Description

|  Sets and reads the frequency span of the band noise marker. This area is
marked by two vertical dotted lines on the screen and the marker's y-axis
value is set to the measured power value. Noise and power on the same marker
share the same span.  
---|---  
  
####  VB Syntax

|  mkr.BandnoiseSpan = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mkr |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (Double) Choose a frequency span within the frequency range of the analyzer.  
  
#### Return Type

|  Double  
  
#### Default

|  1 MHz  
  
#### Examples

|  [See example program](../../COM_Example_Programs/Spectrum_Analyzer.md)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_BandnoiseSpan(double* pVal) HRESULT put_BandnoiseSpan(double
newVal)  
  
#### Interface

|  IMarker6  
  
* * *

