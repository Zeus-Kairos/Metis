##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
## getDataByString Method

* * *

#### Description

|  Retrieves variant data from the specified location in your choice of
formats. The VNA returns complex trace data which is ratioed if required by
the measurement parameter, such as S11 or A/B. Otherwise it is raw receiver
data, such as A or B. Equation Editor Notes:

  * When equation editor is active on a trace in a standard S-parameter channel, GetData returns the data from the parameter on the trace that was measured last. For example, for the equation "S22 + S33 + S11, then S33 is the last measured parameter because it uses source port 3.
  * In [applications](../../../Applications/Applications.md), if equation editor is active and the original parameter for the trace is not requested anywhere in the channel, then zeros are returned. If the original parameter is being measured within the channel, then data for the original parameter is returned.
  * In general, if an equation contains no measurement parameters, then data for the original parameter is returned.

  
---|---  
  
####  VB Syntax

|  data = meas.getDataByString location, format  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (variant) \- Array to store the data.  
meas |  (object) - A Measurement object  
location |  (string)  Name of the buffer to be read. Choose from: "naRawData" "naCorrectedData" "naMeasResult" "naRawMemory" "naMemoryResult" "naDivisor" \- When reading data from, or writing data to, the normalization divisor, you must first create a divisor trace using [DataToDivisor Method](DataToDivisor_Method.md). See [Data Access Map](../../DataMapSet.md)  
format |  (enum NADataFormat) \- Format in which you would like the data. It does not have to be the displayed format. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar 4 - naDataFormat_Smith 5 - naDataFormat_Delay 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith 11 - naDataFormat_Kelvin 12 - naDataFormat_Fahrenheit 13 - naDataFormat_Centigrade [Learn more about Data Format.](../../../S1_Settings/Data_Format.md) * Specify Smith or Polar formats to obtain complex data pairs, which require a two-dimensional array varData (numpts, 2) to accommodate both real and imaginary data. All scalar formats return a single dimension varData(numpts).  
  
#### Return Type

|  Variant array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  meas.getDataByString naMeasResult, naDataFormat_Phase  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT getDataByString( BSTR location, tagDataFormat dataFormat, VARIANT *
pData );  
  
#### Interface

|  IMeasurement  
  
* * *

