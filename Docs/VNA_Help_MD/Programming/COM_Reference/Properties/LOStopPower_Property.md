##### Write/Read

|

##### [About Swept IMDx](../../../Applications/Swept_IMDx.md)  
  
---|---  
  
## LOStopPower Property

* * *

#### Description

|  Sets or returns the Stop value of a LO Power sweep. Also set
[imdx.SweepType](SweepType_imd_Property.md) to naIMDLOPowerSweep.  
---|---  
  
####  VB Syntax

|  obj.LOStopPower (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
n |  (Long) \- LO stage number. Choose 1  
value |  (double) \- LO Stop power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -10 dBm  
  
#### Examples

|  convtr.LOStopPower(1) = -5 'Sets the LO Power sweep Stop value Stop =
convtr.LOStopPower(1) 'Reads the Stop value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LOStopPower(long LOStage, double *pVal) HRESULT
put_LOStopPower(long LOStage, double newVal)  
  
#### Interface

|  IConverter  
  
* * *

