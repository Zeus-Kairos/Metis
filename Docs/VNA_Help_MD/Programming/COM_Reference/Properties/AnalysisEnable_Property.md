##### Write/Read

|

##### [About GCA
Analysis](../../../Applications/Gain_Compression_Application.htm#Analysis)  
  
---|---  
  
## AnalysisEnable Property

* * *

#### Description

|  Set and read the (ON | OFF) state of Gain Compression Analysis.  
---|---  
  
#### VB Syntax

|  gcaMeas.AnalysisEnable = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gcaMeas |  A [GainCompressionMeas](../Objects/GainCompression_Meas_Object.md) (object)  
value |  (Boolean)  Choose from: False \- Disable GCA analysis trace. True - Enable GCA analysis trace.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  gcaMeas.AnalysisEnable = True 'Write  
analysis = gca.AnalysisEnable 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AnalysisEnable(VARIANT_BOOL* value) HRESULT
put_AnalysisEnable(VARIANT_BOOL value)  
  
#### Interface

|  IGainCompressionMeas  
  
* * *

