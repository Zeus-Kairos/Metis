##### Read-only

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## XAxisStop Property

* * *

#### Description

|  Returns the X-Axis stop value of the specified tuning sweep.  
---|---  
  
####  VB Syntax

|  value = embedLODiag.XAxisStop (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) Variable to store the returned data.  
embedLODiag |  An [EmbeddedLODiagnostic](../Objects/EmbeddedLODiagnostic_Object.md) (object)  
n |  (Long) Tuning sweep number. Use [NumberOfSweeps](NumberOfSweeps_Property.md) to find the number of sweeps taken.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data= embedLO.XAxisStop 3 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT XAxisStop (long sweep, double* start);  
  
#### Interface

|  IEmbededLODiagnostic  
  
* * *

