##### Read-only

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## StepData Property

* * *

#### Description

|  Returns an array of data from the specified tuning sweep.  
---|---  
  
####  VB Syntax

|  value = embedLODiag.StepData (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant Array) Variable to store the returned data.  
embedLODiag |  An [EmbeddedLODiagnostic](../Objects/EmbeddedLODiagnostic_Object.md) (object)  
n |  (Long) Tuning sweep number. Use [NumberOfSweeps](NumberOfSweeps_Property.md) to find the number of sweeps taken.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data= embedLO.StepData 3 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT StepData(long sweep,VARIANT* pArray);  
  
#### Interface

|  IEmbededLODiagnostic  
  
* * *

