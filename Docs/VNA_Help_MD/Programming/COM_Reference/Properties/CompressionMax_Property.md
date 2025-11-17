##### Read-only

|

##### [About PNOP / PSAT Marker
Search](../../../S4_Collect/Markers.htm#AboutPSATnPNOP)  
  
---|---  
  
## CompressionMax Property

* * *

#### Description

|  Returns the Compression Max result of a PSat or PNOP marker search. Comp
Max = Gain Max - Linear Gain (not shown on PNOP marker readout).  
---|---  
  
####  VB Syntax

|  compMax = pMarker.CompressionMax  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
compMax |  (double) - Variable to store returned value  
pMarker |  A [PNOP](../Objects/PNOP_Object.md) (object) or a [PSaturation](../Objects/PSaturation_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
  
#### Examples

|  compMax = pMark.CompressionMax 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CompressionMax(double* pNewVal)  
  
#### Interface

|  IPNOP or IPSaturation  
  
* * *

