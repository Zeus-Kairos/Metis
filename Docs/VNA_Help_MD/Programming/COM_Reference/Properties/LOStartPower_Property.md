##### Write/Read

|

##### [About Swept IMDx](../../../Applications/Swept_IMDx.md)  
  
---|---  
  
## LOStartPower Property

* * *

#### Description

|  Sets or returns the Start value of a LO Power sweep.. Also set
[imdx.SweepType](SweepType_imd_Property.md) to naIMDLOPowerSweep.  
---|---  
  
####  VB Syntax

|  obj.LOStartPower (n) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
n |  (Long) \- LO stage number. Choose 1  
value |  (double) \- LO start power in dBm.  
  
#### Return Type

|  Double  
  
#### Default

|  -20 dBm  
  
#### Examples

|  convtr.LOStartPower(1) = -5 'Sets the LO Power sweep start value start =
convtr.LOStartPower(1) 'Reads the start value  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LOStartPower(long LOStage, double *pVal) HRESULT
put_LOStartPower(long LOStage, double newVal)  
  
#### Interface

|  IConverter  
  
* * *

