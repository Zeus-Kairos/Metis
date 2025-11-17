##### Read-only

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## GetRaw2DData Method

* * *

#### Description

|  Returns raw data at all frequency and power data points for any GCA sweep.
Previously 2D sweep only.

  * When using SMART sweep, ALL data is returned including ALL background iteration sweeps. Use [TotalIterations](../Properties/TotalIterations_Property.md) to determine the number of iteration sweeps. The number of data points that are returned is always the number of frequency points times the number of iteration sweeps.
  * When using 2D sweeps, ALL data is returned. The number of data points returned / freq may vary. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving)

Use the standard ["get data"](../../DataTopic.md#meas) commands to return
just the displayed data results (not the background sweeps). A compression
parameter must be present. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#CompressionParams)  
---|---  
  
####  VB Syntax

|  data = gca.GetRaw2DData location, format, param  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array in which to store returned measurement data.  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
location |  (enum NADataStore) - Where the data you want is residing. Choose from: 0 - naRawData 1 - naCorrectedData  
format |  (enum NADataFormat) - Format in which you would like the data. It does not have to be the displayed format. Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag 2 - naDataFormat_Phase 3 - naDataFormat_Polar* 4 - naDataFormat_Smith* 5 - naDataFormat_Delay -- Not valid for this command. 6 - naDataFormat_Real 7 - naDataFormat_Imaginary 8 - naDataFormat_SWR 9 - naDataFormat_PhaseUnwrapped 10 - naDataFormat_InverseSmith [Learn more about Data Format](../../../S1_Settings/Data_Format.md). * Specify Smith or Polar formats to obtain complex data pairs, which require a two-dimensional array varData (numpts, 2) to accommodate both real and imaginary data. All scalar formats return a single dimension varData(numpts). naDataFormat_Phase and naDataFormat_PhaseUnwrapped returns degrees.  
param |  (String) Parameter of data to return. Not case-sensitive. The specified parameter need NOT be displayed. However, a compression parameter must be present. [Learn more.](../../../Applications/Gain_Compression_Application.md#CompressionParams) Choose from:

  * "pin" \- (CompIn21) Input power at the compression point.
  * "pout" \- (CompOut21) Output power at the compression point.
  * "gain" \- (CompGain21) Device gain (S21) at the compression point.
  * "inputmatch" \- (CompS11) Input match at the compression point.
  * "DeltaGain" \- (DeltaGain21) Measured Gain (watts) / Ref Gain (watts). [Learn more.](../../../Applications/Gain_Compression_Application.md#DeltaGain21)
  * "AI1" and "AI2" \- ADC measurements at the specified compression level. [Learn more](../../../S1_Settings/ADC_Measurements.md).

  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data = gca.GetRaw2DData naRawData, naDataFormat_Real, "pin"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetRaw2DData(tagNADataStore location, tagNADataFormat format, BSTR
data_name, VARIANT* pData);  
  
#### Interface

|  IGainCompression  
  
* * *

