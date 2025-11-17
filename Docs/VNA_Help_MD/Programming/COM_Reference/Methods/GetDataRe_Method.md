##### Read-only

|

##### [About Gain
Compression](../../../Applications/Gain_Compression_Application.htm)  
  
---|---  
  
## GetDataRe Method

* * *

#### Description

|  Reads the REAL part of the data acquired from any GCA sweep. Previously 2D
sweep only. Note: For 2D sweeps, the number of data points returned / freq may
vary. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#Saving)  
---|---  
  
####  VB Syntax

|  data = gca.GetDataRe stim, dPoint, param  
  
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

|  For the fifth frequency data point, returns 'Power Output' REAL data from
all power stimulus values. If there are 30 power sweep points, 30 values are
returned. data = gca.GetDataRe naFrequencySelect, 5, "pout" For the 30th
stimulus power data point, returns 'Power Output' REAL data from all frequency
stimulus values. If there are 201 frequency sweep points, 201 values are
returned. data = gca.GetDataRe naPowerSelect, 30, "pout" Note: For 2D sweeps,
the number of data points returned / freq may vary. [Learn
more.](../../../Applications/Gain_Compression_Application.htm#Saving)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetDataRe(tagNAGCAIndexSelect index_select, int index,BSTR
data_name, VARIANT* pData);  
  
#### Interface

|  IGainCompression  
  
* * *

