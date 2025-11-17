##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## GetData Method

* * *

#### Description

|  Retrieves variant data from the specified location in your choice of
formats. To get smoothed data from any of the specified locations, the format
must be the same as the displayed format. The VNA returns complex trace data
which is ratioed if required by the measurement parameter, such as S11 or A/B.
Otherwise it is raw receiver data, such as A or B. This method returns a
variant which is less efficient than methods available on the [IArrayTransfer
interface](../Objects/Measurement_Object.htm#IArrayTransfer). If you plan to
Put this data back into analyzer,
[putDataComplex](Put_Data_Complex_Method.md) (variant data) method requires
complex, two-dimensional data. Therefore, request the data in Polar format.
Equation Editor Notes:

  * When equation editor is active on a trace in a standard S-parameter channel, GetData returns the data from the parameter on the trace that was measured last. For example, for the equation "S22 + S33 + S11, then S33 is the last measured parameter because it uses source port 3.
  * In [applications](../../../Applications/Applications.md), if equation editor is active and the original parameter for the trace is not requested anywhere in the channel, then zeros are returned. If the original parameter is being measured within the channel, then data for the original parameter is returned.
  * In general, if an equation contains no measurement parameters, then data for the original parameter is returned.

  
---|---  
  
####  VB Syntax

|  data = meas.GetData location, format  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
meas |  A Measurement (object)  
location |  (enum NADataStore) \- Where the data you want is residing. See [Data Access Map](../../DataMapSet.md). Choose from: 0 - naRawData 1 - naCorrectedData 2 - naMeasResult 3 - naRawMemory 4 - naMemoryResult 5 - naDivisor When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md).  
format |  (enum NADataFormat) - Format in which you would like the data. It does not have to be the displayed format. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar* 4 - naDataFormat_Smith* 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade [Learn more about Data Format.](../../../S1_Settings/Data_Format.md) * Specfiy Smith or Polar formats to obtain complex data pairs, which require a two-dimensional array varData (numpts, 2) to accommodate both real and imaginary data. All scalar formats return a single dimension varData(numpts). naDataFormat_Phase and naDataFormat_PhaseUnwrapped returns degrees. However, [putDataScalar](Put_Data_Scalar_Method.md) method accepts data in radians (not degrees) and displays in degrees.  
  
#### Return Type

|  Variant array - automatically dimensioned to the size of the data  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varData As Variant  
varData = meas.GetData(naMeasResult,naDataFormat_Phase)  
'Print Data  
For i = 0 to chan.NumberOfPoints-1  
Print varData(i)  
Next i [See a C# example.](../../COM_Example_Programs/Using_CSharp.md)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getData(tagNADataStore DataStore, tagDataFormat DataFormat, VARIANT
*pData)  
  
#### Interface

|  IMeasurement  
  
* * *

