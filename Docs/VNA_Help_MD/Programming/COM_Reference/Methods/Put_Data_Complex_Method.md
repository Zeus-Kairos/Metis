##### Write-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## putDataComplex Method

* * *

#### Description

|  Puts complex data into the specified location. This method forces the
channel into Hold mode to prevent the input data from being overwritten.  
---|---  
  
####  VB Syntax

|  meas.putDataComplex location, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A measurement (object)  
location |  (enum NADataStore) Where the Data will be put. Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult \- Valid ONLY when the display format is either Polar or Smith Chart. 3 - naRawMemory - See note below. 4 - naMemoryResult 5 - naDivisor \- When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md). Note: When putting data into 3 - naRawMemory: 1\. Put the analyzer in hold mode 2\. Call [DataToMemory](DataToMemory_Method.md) to initialize a memory buffer 3\. Call putDataComplex(naRawMemory, data) This ensures that the memory buffer is appropriately initialized before receiving new data.  
data |  (variant) - A two-dimensional variant array. Note: All buffers except naMeasResult and naMemoryResult require Complex data  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  ' Put 201 points worth of raw (complex) data into the measurement  
' Note that an array of complex numbers is represented by a 2-D array where
the first rank is the number of points, and the 2nd rank is always size 2 (max
index 1) representing the Real and Imag parts of the complex number.  
  
' complex array of data (2nd dimension of size 2 represents Re/Im  
Dim data(200,1) )  
For i = 0 to 200  
' Set Real part of data point i  
data(i,0) = i/200;  
' Set Imag part of data point i  
data(i,1) = i/200;  
Next  
app.ActiveMeasurement.putDataComplex naRawData, data  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT putDataComplex(tagNADataStore DataStore, VARIANT complexData)  
  
#### Interface

|  IMeasurement  
  
* * *

* * *

