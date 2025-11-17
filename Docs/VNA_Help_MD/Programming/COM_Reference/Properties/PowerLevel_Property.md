##### Write/Read

|

##### [About GainCompressionCal](../../../Applications/GCA_Cal.md)

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## PowerLevel Property

* * *

#### Description

|  Set and read the power level at which to perform the Source Power Cal
portion of a Gain Compression Calibration or a SweptIMD Cal.  
---|---  
  
####  VB Syntax

|  object.PowerLevel = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  A [GainCompressionCal](../Objects/GainCompressionCal_Object.md) (object) A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object)  
value |  (Double) - Power level in dB. Choose a value from +30 to (-30). [Learn about choosing a power level.](../../../Applications/GCA_Cal.md#SourceCal)  
  
#### Return Type

|  Double  
  
#### Default

|  0  
  
#### Examples

|  gca.PowerLevel = -5 'Write  
pLevel = imd.PowerLevel 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_PowerLevel(double* pVal) HRESULT put_PowerLevel(double newVal)  
  
#### Interface

|  IGainCompressionCal ISweptIMDCal  
  
* * *

