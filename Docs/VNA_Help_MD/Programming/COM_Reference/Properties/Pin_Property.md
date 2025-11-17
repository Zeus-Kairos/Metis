##### Read-only

|

##### [About PNOP / PSAT Marker Search](../../../S4_Collect/Markers.md#PNOP)  
  
---|---  
  
## Pin Property

* * *

#### Description

|  Returns the Pin result of a PNOP or PSAT marker search. PNOP In = Marker 4
X-axis value PSAT In = Marker 2 X-axis value  
---|---  
  
####  VB Syntax

|  pIn = pMark.Pin  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pIn |  (double) - Variable to store returned value  
pMark |  A [PNOP](../Objects/PNOP_Object.md) (object) or [PSaturation](../Objects/PSaturation_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
  
#### Examples

|  pIn = pMark.Pin 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Pin(double* pNewVal)  
  
#### Interface

|  IPNOP or IPSaturation  
  
* * *

