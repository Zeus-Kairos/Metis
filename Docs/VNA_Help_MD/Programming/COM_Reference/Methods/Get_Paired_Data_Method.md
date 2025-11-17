##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetPairedData Method

* * *

#### Description

|  Retrieves pairs of data from the specified location. Note: This method
exists on a non-default interface. If you cannot access this method, use the
[Get Data](Get_Data_Method.md) Method on IMeasurement.  
---|---  
  
####  VB Syntax

|  measData.getPairedData location, format, numPts, d1, d2  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore) - Where the data you want is residing. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md). See [Data Access Map](../../DataMapSet.md)  
format |  (enum NAPairedDataFormat) - Format in which you would like the Paired data. Choose from: 0 -naLogMagPhase \- Log magnitude and phase 1 -naLinMagPhase \- Linear magnitude and phase 2 -naRealImaginary \- Real and Imaginary Note: Selecting naRealImaginary format is the same as using the [getComplex](Get_Complex_Method.md) method  
numPts |  (long integer) - Number of data points requested  
[out] - specifies number of data elements returned  
[in] - specifies the data being requested or the capacity of the dPaired array  
d1 |  (single) - Array to store the magnitude / real values  
d2 |  (single) - Array to store the phase / imaginary values  
  
#### Return Type

|  Two Single arrays  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim logm() As Single  
Dim phase() As Single  
Public measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
Dim numpts As Long  
numPoints = app.ActiveChannel.NumberOfPoints  
ReDim logm(numPoints)  
ReDim phase(numPoints)  
  
measData.getPairedData naCorrectedData, naLogMagPhase, numPoints, logm(0),
phase(0)  
  
Print values(0), values(1)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getPairedData(tagNADataStore DataStore, tagNAPairedDataFormat
PairFormat, long* pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  IArrayTransfer

