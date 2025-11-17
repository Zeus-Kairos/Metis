##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## PutComplex Method

* * *

#### Description

|  Puts real and imaginary data into the specified location. This method
forces the channel into Hold mode to prevent the input data from being
overwritten. Learn more about [reading and writing Cal Data using
COM.](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)
Data put in the raw data store will be re-processed whenever a change is made
to the measurement attributes such as format or correction. Data put in the
measurement results store will be overwritten by any measurement attribute
changes. See also [putNAComplex](Put_NAComplex_Method.md)  
---|---  
  
####  VB Syntax

|  measData.putComplex location, numPts, real(), imag(), [format]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
measData |  An IArrayTransfer interface which supports the Measurement object  
location |  (enum NADataStore) Where the Data will be put. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor - When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
numPts |  (long integer) - Number of data points in the channel  
real() |  (single) - Array containing real data values  
imag() |  (single) -Array containing imaginary data values  
format |  (enum NADataFormat) optional argument - display format of the real and imaginary data. Only used if destination is naMeasResult or naMemoryResult buffer. If unspecified, data is assumed to be in naDataFormat_Polar 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade [Learn more about Data Format.](../../../S1_Settings/Data_Format.md)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim measData As IArrayTransfer  
Set measData = app.ActiveMeasurement  
  
measData.putComplex naMemoryResult, 201, real(0),imag(0),naDataFormat_SWR  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT putComplex( tagNADataStore DataStore, long lNumValues, float*
pReal, float* pImag, tagDataFormat displayFormat)  
  
#### Interface

|  IArrayTransfer  
  
* * *

