##### Read-only

|

##### [About Marker Search](../../../S4_Collect/Markers.md#SearchDiag1)  
  
---|---  
  
## GainMax Property

* * *

#### Description

|  Returns the GainMax result of the PNOP or PSAT marker search. Gain Max =
PMax Out - PMax In  
---|---  
  
####  VB Syntax

|  gainMax = pMarker.GainMax  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gainMax |  (double) - Variable to store returned value  
pMarker |  A [PNOP](../Objects/PNOP_Object.md) (object) or [PSaturation](../Objects/PSaturation_Object.md) (Object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
  
#### Examples

|  gainMax = pMarker.GainMax 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_GainMax(double* pNewVal)  
  
#### Interface

|  IPNOP or IPSaturation  
  
* * *

