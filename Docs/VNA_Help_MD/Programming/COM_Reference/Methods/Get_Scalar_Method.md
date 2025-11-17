##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetScalar Method

* * *

#### Description

|  Retrieves scalar data (ONE number per data point) from the specified
location. Note: This method exists on a non-default interface. If you cannot
access this method, use the [Get Data](Get_Data_Method.md) Method on
IMeasurement.  
---|---  
  
####  VB Syntax

|  measData.getScalar location, format, numPts, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore) - Where the data you want is residing. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
format |  (enum NADataFormat) \- Format in which you would like the data. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade Note: Polar, Smith, and Inverse Smith are invalid formats for this command. See [Get Complex Method](Get_Complex_Method.md). [Learn more about Data Format.](../../../S1_Settings/Data_Format.md)  
numPts |  (long integer) - Number of data points requested  
[out] - specifies number of data elements returned  
[in] - specifies the data being requested or the capacity of the dScalar array  
data |  (single) - Array to store the scalar data.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim dScalar() As Single  
Dim measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
Dim numpts as Long  
numpts = app.ActiveChannel.NumberOfPoints  
ReDim dScalar(numPoints)  
  
measData.getScalar naCorrectedData, naDataFormat_LogMag, numpts, dScalar(0)  
Print dScalar(0), dScalar(1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getScalar(tagNADataStore DataStore, tagNADataFormat DataFormat,
long* pNumValues, float* pVals)  
  
#### Interface

|  IArrayTransfer  
  
* * *

