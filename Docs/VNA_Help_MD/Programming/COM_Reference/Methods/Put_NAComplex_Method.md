##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutNAComplex Method

* * *

#### Description

|  Puts complex data into the specified location. This method forces the
channel into Hold mode to prevent the input data from being overwritten. The
data is processed and displayed. Data put in the naRawData store will be re-
processed whenever a change is made to the measurement attributes such as
format or correction. Data put in the naMeasResult store will be overwritten
by any measurement attribute changes (such as moving a marker). Note: This
method uses NAComplex which is a user-defined data type. If you cannot or
prefer not to use this data type, use the [putComplex](Put_Complex_Method.md)
method.  
---|---  
  
####  VB Syntax

|  measData.putNAComplex location, numPts, data, [format]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore) Where the Data will be put. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
numPts |  (long integer) - Number of data points in the channel  
data |  (NAComplex) - A one-dimensional array of Complex data matching the number of points in the current measurement.  
format |  (enum NADataFormat) - Optional argument. Format of the data. If unspecified, naDataFormat_Polar is assumed. Only used when the destination store is naMeasResult or naMemoryResult. 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade [Learn more about Data Format.](../../../S1_Settings/Data_Format.md)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
  
measData.putNAComplex naMemoryResult, 201, dRawComplex(0)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT putNAComplex(tagNADataStore DataStore, long lNumValues, TsComplex*
pArrayOfComplex, tagDataFormat displayFormat)  
  
#### Interface

|  IArrayTransfer  
  
* * *

