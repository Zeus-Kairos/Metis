##### Read-only

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## NumberOfSweeps Property

* * *

#### Description

|  Returns the number of tuning sweeps used for the latest embedded LO
measurement.  
---|---  
  
####  VB Syntax

|  value = embedLODiag.NumberOfSweeps  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) Variable to store the returned data.  
embedLODiag |  An [EmbeddedLODiagnostic](../Objects/EmbeddedLODiagnostic_Object.md) (object)  
  
#### Return Type

|  (Long)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data= embedLODiag.NumberOfSweeps 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NumberOfSweeps(long * numSweeps);  
  
#### Interface

|  IEmbededLODiagnostic  
  
* * *

