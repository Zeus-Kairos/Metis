##### Read-only

|

##### [About PNOP Marker Search](../../../S4_Collect/Markers.md#PNOP)  
  
---|---  
  
## Compression Property

* * *

#### Description

|  Returns the Compression result of the PNOP marker search. Pnop Comp = Pnop
Gain - Linear Gain (not shown on marker readout).  
---|---  
  
####  VB Syntax

|  comp = pnop.Compression  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
comp |  (double) - Variable to store returned value  
pnop |  A [PNOP](../Objects/PNOP_Object.md) (object)  
  
#### Return Type

|  Double  
  
#### Default

|  Not applicable  
  
#### Examples

|  comp = pnop.Compression 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Compression(double* pNewVal)  
  
#### Interface

|  IPNOP  
  
* * *

