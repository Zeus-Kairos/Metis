##### Write/Read

|

##### [About Marker Format](../../../S4_Collect/Markers.md#marker_format)  
  
---|---  
  
## Format Property (marker)

* * *

#### Description

|  Sets (or returns) the format of the marker.  
---|---  
  
####  VB Syntax

|  mark.Format = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
value |  (enum NAMarkerFormat) - Choose from: 0 - naMarkerFormat_LinMag 1 - naMarkerFormat_LogMag 2 - naMarkerFormat_Phase 3 - naMarkerFormat_Delay 4 - naMarkerFormat_Real 5 - naMarkerFormat_Imaginary 6 - naMarkerFormat_SWR 7 - naMarkerFormat_LinMagPhase 8 - naMarkerFormat_LogMagPhase 9 - naMarkerFormat_RealImaginary 10 - naMarkerFormat_ComplexImpedance 11 - naMarkerFormat_ComplexAdmittance 12 - naMarkerFormat_Kelvin 13 - naMarkerFormat_Fahrenheit 14 - naMarkerFormat_Celsius 15 - naMarkerFormat_Default - the same format as the trace. 16 - naMarkerFormat_Noise - Available ONLY in IM Spectrum and SA measurement classes.  
  
#### Return Type

|  NAMarkerFormat  
  
#### Default

|  15 -naMarkerFormat_Default  
  
#### Examples

|  mark.Format = naMarkerFormat_SWR 'Write  
fmt = mark.Format 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Format(tagNAMarkerFormat *pVal) HRESULT
put_Format(tagNAMarkerFormat newVal)  
  
#### Interface

|  IMarker  
  
* * *

