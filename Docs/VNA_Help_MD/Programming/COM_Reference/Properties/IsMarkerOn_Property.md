##### Read-only

|

##### [About Embedded LO](../../../Applications/Embedded_LO.md)  
  
---|---  
  
## IsMarkerOn Property

* * *

#### Description

|  Returns whether or not a marker was used for the specified tuning sweep.  
---|---  
  
####  VB Syntax

|  value = embedLODiag.IsMarkerOn (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) Variable to store the returned data.  
embedLODiag |  An [EmbeddedLODiagnostic](../Objects/EmbeddedLODiagnostic_Object.md) (object)  
n |  Tuning sweep number. Use [NumberOfSweeps](NumberOfSweeps_Property.md) to find the number of sweeps taken.  
  
#### Return Type

|  (String)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  data= embedLO.IsMarkerOn 3 'read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT IsMarkerOn(long sweep, VARIANT_BOOL* markerOn);  
  
#### Interface

|  IEmbededLODiagnostic  
  
* * *

