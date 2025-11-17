##### Read-only

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## GetDataIm Method

* * *

#### Description

|  For a specified data point, returns the imaginary part of the specified
Gain Compression data. If correction is on, corrected data are returned.
Otherwise, raw data are returned. Can be used with Smart and 2D sweeps.

  * For SMART sweep, the number of data points that are returned is always going to be the number of iteration sweeps. Use to determine the number of iteration sweeps.
  * For 2D sweeps, the number of data points returned / freq may vary. [Learn more.](../../../Applications/Gain_Compression_Application.md#Saving)

  
---|---  
  
####  VB Syntax

|  data = gca.GetDataIm stim, dPoint, param  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array in which to store returned measurement data.  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
stim |  (NAGCAIndexSelect)

  * naFrequencySelect \- for the specified frequency data point, returns all of the measured data for each power stimulus.
  * naPowerSelect \- for the specified power data point, returns all of the measured data for each frequency stimulus.

  
dPoint |  Data point (Frequency or Power) for which data is returned.  
param |  Parameter of data to return. Not case-sensitive. Choose from:

  * "pin" \- input power at each data point.
  * "pout" \- output power at each data point.
  * "gain" \- device gain (S21) at each data point.
  * "inputmatch" \- input match (S11) at each data point.
  * "DeltaGain" \- Measured Gain (watts) / Ref Gain (watts). [Learn more.](../../../Applications/Gain_Compression_Application.md#DeltaGain21)
  * "AI1" and "AI2" \- ADC measurements at the specified compression level. [Learn more](../../../S1_Settings/ADC_Measurements.md).

  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  For the fifth frequency data point, returns 'Power Output' imaginary
(phase) data from all power stimulus values. If there are 30 power sweep
points, 30 values are returned. data = gca.GetDataIm naFrequencySelect, 5,
"pout" For the 30th stimulus power data point, returns 'Power Output'
imaginary (phase) data from all frequency stimulus values. If there are 201
frequency sweep points, 201 values are returned. data = gca.GetDataIm
naPowerSelect, 30, "pout" Note: For 2D sweeps, the number of data points
returned / freq may vary. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#Saving)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetDataIm(tagNAGCAIndexSelect index_select, int index,BSTR
data_name, VARIANT* pData);  
  
#### Interface

|  IGainCompression  
  
* * *

