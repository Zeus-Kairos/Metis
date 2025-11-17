##### Write/Read

|

##### [About Vector
Averaging](../../../Applications/Spectrum_Analyzer.htm#Vector_Averaging)  
  
---|---  
  
# VectorAverageEnable Property

* * *

#### Description

|  Set and read the ON/OFF state of the vector averaging.  
---|---  
  
#### VB Syntax

|  sa.coherence.VectorAverageEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
sa.coherence |  A [SpectrumAnalyzerCoherence](../Objects/SpectrumAnalyzerCoherence.md) (object)  
value |  (Boolean) Choose from: 0 - OFF \- Vector averaging is set to OFF. 1 - ON \- Vector averaging is set to ON. [Learn about these settings](../../../Applications/Spectrum_Analyzer.md#Vector_Averaging).  
  
#### Return Type

|  Boolean  
  
#### Default

|  0  
  
#### Examples

|  sa.coherence.VectorAverageEnable = OFF  Write  
value = sa.coherence.VectorAverageEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_VectorAverageEnable(VARIANT_BOOL bEnable); HRESULT
get_VectorAverageEnable(VARIANT_BOOL* bEnable);  
  
#### Interface

|  ICoherenceSA  
  
* * *

