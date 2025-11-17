##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutDataScalar Method

* * *

#### Description

| Puts formatted variant scalar data into the measurement result buffer. The
data will be immediately processed and displayed. Subsequent changes to the
measurement state will be reflected on the display. Always precede this
command by setting the format on the measurement to be consistent with the
format of the data being sent to the analyzer. In this way, the display
annotation will be correct. Execution of this command does not change the
display format.  
---|---  
  
####  VB Syntax

| meas.putDataScalar format, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas | A measurement (object)  
format | (enum NADataFormat) Format of the data. This value is presently ignored by the VNA. Data is always presented in the current format. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade Notes:

  * The [getData](Get_Data_Method.md) (variant) method includes a "format" argument, which allows scalar (one-dimensional) data. To put data back into the "raw" data buffer using this (putDataComplex) method, specify Polar format when using the getData method.
  * Phase format accepts data in radians (not degrees) and displays in degrees. To convert to degrees: radians * (57.29577951308233) = degrees. The getData method returns degrees if the request is for phase data.

  
data | (variant) \- A 1-dimension array of single precision floating point numbers.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| ' Put 201 points worth of scalar data into the measurement  
' 200 is max index, so 0 to 200 is 201 points  
Dim data(200) ' array of 201 (scalar) data points  
' Fill the array  
For i = 0 to 200  
data(i) = i/200  
Next  
app.ActiveMeasurement.putDataScalar 0, data  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT putDataScalar(tagNADataStore DataStore, VARIANT scalarArray)  
  
#### Interface

| IMeasurement  
  
* * *

