##### Read-only

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## MarkerAnnotation Property

* * *

#### Description

|  Returns the Y-axis marker value from the specified tuning sweep. Use
[IsMarkerOn](IsMarkerOn_Property.md) to confirm if a marker was used for the
tuning sweep.  
---|---  
  
####  VB Syntax

|  value = embedLODiag.MarkerAnnotation (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) Variable to store the returned data.  
embedLODiag |  An [EmbeddedLODiagnostic](../Objects/EmbeddedLODiagnostic_Object.md) (object)  
n |  (Long) Tuning sweep number. Use [NumberOfSweeps](NumberOfSweeps_Property.md) to find the number of sweeps taken.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data= embedLO.MarkerAnnotation 3 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT MarkerAnnotation(long sweep, BSTR* annotation);  
  
#### Interface

|  IEmbededLODiagnostic  
  
* * *

