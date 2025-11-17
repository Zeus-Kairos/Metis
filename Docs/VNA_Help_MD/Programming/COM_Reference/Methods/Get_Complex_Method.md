##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetComplex Method

* * *

#### Description

|  Retrieves complex data from the specified location. See also
[getNAComplex](Get_NAComplex_Method.HTM) , [getData](Get_Data_Method.md) ,
and [getPairedData](Get_Paired_Data_Method.md) Methods  
---|---  
  
####  VB Syntax

|  measData.getComplex location, numPts, real(), imag()  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore - IArrayTransfer) - Where the data you want is residing. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
numPts |  (long integer) - Number of data points requested  
[out] - specifies number of data elements returned  
[in] - specifies the data being requested or the capacity of the arrays  
real |  (single) \- Array to store the real values  
imag |  (single) - Array to store the imaginary values  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim real(201) AS Single  
Dim imag(201) AS Single  
Dim pts as Integer  
Dim measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
measData.getComplex naCorrectedData, pts, real(0), imag(0)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  IArrayTransfer - HRESULT getComplex(tagNADataStore DataStore, long*
pNumValues, float* pReal, float* pImag)  
  
#### Interface

|  IArrayTransfer

