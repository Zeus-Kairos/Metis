##### Write/Read

|

##### [About GCA
Analysis](../../../Applications/Gain_Compression_Application.htm#Analysis)  
  
---|---  
  
## AnalysisCWFreq Property

* * *

#### Description

|  Set and return the CW frequency for a compression analysis trace.  
---|---  
  
####  VB Syntax

|  gcaMeas.AnalysisCWFreq = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gcaMeas |  A [GainCompressionMeas](../Objects/GainCompression_Meas_Object.md) (object)  
value |  (Double)  CW frequency in Hz. Choose a frequency within the range of the gain compression channel.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  gcaMeas.AnalysisCWFreq = 1e9 'Write  
cwfreq = gca.AnalysisCWFreq 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AnalysisCWFreq(Double* value) HRESULT put_AnalysisCWFreq(Double
value)  
  
#### Interface

|  IGainCompressionMeas  
  
* * *

