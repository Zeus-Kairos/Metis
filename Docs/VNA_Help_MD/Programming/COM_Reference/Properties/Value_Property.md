##### Read-only

|

##### [About Markers](../../../S4_Collect/Markers.md)  
  
---|---  
  
## Value Property

* * *

#### Description

|  Reads the Y-axis value of the marker. You cannot set the Y-axis value of a
marker. The marker remains at the position at the time you set
[marker.Type](Type_Marker_Property.md). If the marker is a delta marker, the
value will be relative to the reference marker. See Reference marker example
below. See Also: [Set and Read X-axis value](Stimulus_Property.md). Note: To
accurately read the marker Y-axis value with [trace
smoothing](../../../S2_Opt/Trce_Noise.htm#Smoothing) applied, the requested
format must match the [displayed
format](../../../S1_Settings/Data_Format.htm#FormatDiag). Otherwise, the
returned value is un-smoothed data. For example, to read the smoothed marker
value when measuring group delay, both the display format and the marker
format must be set to (Group) Delay.  
---|---  
  
#### VB Syntax

|  YValue = mark.Value (format)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
YValue |  A variable to store the Y-axis value  
mark |  A [Marker](../Objects/Marker_Object.md) (object)  
format |  (enum NAMarkerFormat) - The format in which to return the marker's Y-axis value. The number in parenthesis following the format is the number of values that are returned in a variant array. Choose from: 0 - naMarkerFormat_LinMag (1) 1 - naMarkerFormat_LogMag (1) 2 - naMarkerFormat_Phase (1) 3 - naMarkerFormat_Delay (1) 4 - naMarkerFormat_Real (1) 5 - naMarkerFormat_Imaginary (1) 6 - naMarkerFormat_SWR (1) 7 - naMarkerFormat_LinMagPhase (2) 8 - naMarkerFormat_LogMagPhase (2) 9 - naMarkerFormat_RealImaginary (2) 10 - naMarkerFormat_ComplexImpedance (3) 11 - naMarkerFormat_ComplexAdmittance (3) 12 - naMarkerFormat_Kelvin (1) 13 - naMarkerFormat_Fahrenheit (1) 14 - naMarkerFormat_Celsius (1)  
  
#### Return Type

|  Variant - The (parens) in the previous list of formats indicates the number
of values that are returned in a variant array  
  
#### Default

|  Not applicable  
  
#### Examples

|  YVal = mark.Value(0) 'Read 'or YVal = mark.Value(naMarkerFormat_LinMag)
'Read Reference Marker Y-axis value  
dim RefMarkerY  
RefMarkerY = app.ActiveMeasurement.GetReferenceMarker.Value( 1 )  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Value(tagNAMarkerFormat format, VARIANT *pVal)  
  
#### Interface

|  IMarker  
  
* * *

