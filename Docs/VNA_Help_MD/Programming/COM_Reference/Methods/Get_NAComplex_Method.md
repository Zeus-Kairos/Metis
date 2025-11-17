##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetNAComplex Method

* * *

#### Description

|  Retrieves complex data from the specified location.  
See also [getComplex](Get_Complex_Method.md) and
[getData](Get_Data_Method.md) Method.  
---|---  
  
####  VB Syntax

|  measData.getNAComplex location, numPts, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore) - Where the data you want is residing. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
numPts |  (long integer) - Number of data points requested  
[out] - specifies number of data elements returned  
[in] - specifies the data being requested or the capacity of the dComplex
array  
data |  (NAComplex) \- A one-dimensional array of NaComplex to store the data.  
  
#### Return Type

|  NAComplex  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim dComplex(201) AS NaComplex  
Dim measData As IArrayTransfer  
Dim pts as Long  
Set measData = app.ActiveMeasurement  
measData.getNAComplex naCorrectedData, pts, dComplex(0)  
Notes |  The data is stored as Real and Imaginary (Re and Im) members of the NaComplex user defined type. You can access each number individually by iterating through the array. For i = 0 to NumPts-1  
dReal (i) = dcomplex (i).Re  
dImag (i) = dcomplex (i).Im  
Next i  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getNAComplex(tagNADataStore DataStore, long* pNumValues, TsComplex*
pComplex)  
  
#### Interface

|  IArrayTransfer

