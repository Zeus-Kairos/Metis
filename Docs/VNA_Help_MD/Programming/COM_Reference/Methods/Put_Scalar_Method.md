##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutScalar Method

* * *

#### Description

|  Puts Scalar data in the Measurement Result buffer. The putScalar array is
not processed by the analyzer; it is just displayed. Any change to the
measurement state (changing the format, for example) will cause the putScalar
data to be overwritten with the data processed from the raw data buffer.  
---|---  
  
####  VB Syntax

|  measData.putScalar, format, numPts, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object.  
format |  (enum NADataFormat) Format of the data. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade [Learn more about Data Format.](../../../S1_Settings/Data_Format.md) Note: Smith, InverseSmith, and Polar formats are not allowed.  
numPts |  (integer) - Number of values. Usually the number of points in the trace (chan.NumberOfPoints).  
data |  (single) \- A one-dimensional array of Scalar data matching the number of points in the current measurement.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
  
measData.putScalar naDataFormat_LogMag, 201, dScalar(0)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT putScalar/(tagDataFormat eFormat, long lNumValues, float*
pArrayOfScalar)  
  
#### Interface

|  IArrayTransfer  
  
* * *

