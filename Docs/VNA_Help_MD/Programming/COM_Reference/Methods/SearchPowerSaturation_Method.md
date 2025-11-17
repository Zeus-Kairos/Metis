##### Write-only

|

##### [About PSAT Marker Search](../../../S4_Collect/Markers.md#PSat)  
  
---|---  
  
# SearchPowerSaturation Method

* * *

#### Description

|  Initiates a Power Saturation marker search. Turns on and sets markers 1, 2,
and 3 to calculate various Power Saturation parameters. First set
[PMaxBackOff](../Properties/PMaxBackOff_Property.md). To turn off the Power
Saturation markers, either turn them off individually or use [DeleteAllMarkers
Method](DeleteAllMarkers_Method.htm) To search a User Range with the PSAT
search, first activate marker 1 and set the desired [User
Range](../Properties/User_Range_Property.htm). Then send this command. The
user range used with the PSAT search only applies to marker 1 searching for
the linear gain value. The other markers may fall outside the user range.  
---|---  
  
####  VB Syntax

|  pSat.SearchPowerSaturation( )  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pSat |  A [PSaturation](../Objects/PSaturation_Object.md) (object)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  pSat.SearchPowerSaturation [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SearchPowerSaturation()  
  
#### Interface

|  IPSaturation  
  
* * *

