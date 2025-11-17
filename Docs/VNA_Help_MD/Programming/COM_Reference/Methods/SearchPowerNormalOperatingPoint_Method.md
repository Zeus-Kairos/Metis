##### Write-only

|

##### [About PNOP Marker Search](../../../S4_Collect/Markers.md#PNOP)  
  
---|---  
  
## SearchPowerNormalOperatingPoint Method

* * *

#### Description

|  Initiates a PNOP marker search. Turns on and sets markers 1, 2, 3, and 4 to
calculate various PNOP parameters. First set
[BackOff](../Properties/BackOff_Property.md) and
[PinOffset](../Properties/PinOffset_Property.md). To turn off these markers,
either turn them off individually or
[DeleteAllMarkers.](Delete_Marker_Method.md) To search a
[UserRange](../Properties/User_Range_Property.md), first activate marker 1
and set the desired UserRange. Then send the SearchPowerNormalOperatingPoint
command. The user range applies only to marker 1 searching for the max value.
The other markers may fall outside the user range.  
---|---  
  
####  VB Syntax

|  pnop.SearchPowerNormalOperatingPoint( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pnop |  A [PNOP](../Objects/PNOP_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  pnop.SearchPowerNormalOperatingPoint [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SearchPowerNormalOperatingPoint()  
  
#### Interface

|  IPNOP  
  
* * *

