##### Write/Read

|

##### [About GCA
Analysis](../../../Applications/Gain_Compression_Application.htm#Analysis)  
  
---|---  
  
## AnalysisIsDiscreteFreq Property

* * *

#### Description

|  Sets and returns whether the CW frequency for the compression analysis
trace can be set to only the discrete frequencies or provides interpolation.  
---|---  
  
####  VB Syntax

|  gcaMeas.AnalysisIsDiscreteFreq = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gcaMeas |  A [GainCompressionMeas](../Objects/GainCompression_Meas_Object.md) (object)  
value |  (Boolean)  Choose from: False - Interpolated data points. True \- Discrete data points only.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gcaMeas.AnalysisIsDiscreteFreq = True 'Write  
isDisc = gca.AnalysisIsDiscreteFreq 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AnalysisIsDiscreteFreq(VARIANT_BOOL* value) HRESULT
put_AnalysisIsDiscreteFreq(VARIANT_BOOL value)  
  
#### Interface

|  IGainCompressionMeas  
  
* * *

