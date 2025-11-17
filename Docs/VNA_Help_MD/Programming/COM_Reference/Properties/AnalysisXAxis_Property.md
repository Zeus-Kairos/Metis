##### Write/Read

|

##### [About GCA
Analysis](../../../Applications/Gain_Compression_Application.htm#Analysis)  
  
---|---  
  
## AnalysisXAxis Property

* * *

#### Description

|  Sets and returns the type of data to display on the x-axis of a compression
analysis trace.  
---|---  
  
####  VB Syntax

|  gcaMeas.AnalysisXAxis = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gcaMeas |  A [GainCompressionMeas](../Objects/GainCompression_Meas_Object.md) (object)  
value |  (Enum as NAGCAAnalysisXAxis)  Choose from: naPsourceAsXAxis (0) - Power from the source. naPinAsXAxis (1) - Input power to the DUT.  
  
#### Return Type

|  Enum  
  
#### Default

|  naPinAsXAxis (1)  
  
#### Examples

|  gcaMeas.AnalysisXAxis = naPinAsXAxis 'Write  
xAxis = gca.AnalysisXAxis 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AnalysisXAxis(tagNAGCAAnalysisXAxis* value) HRESULT
put_AnalysisXAxis(tagNAGCAAnalysisXAxis value)  
  
#### Interface

|  IGainCompressionMeas  
  
* * *

