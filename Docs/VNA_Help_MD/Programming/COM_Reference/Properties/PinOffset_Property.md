##### Write-Read

|

##### [About PNOP Marker Search](../../../S4_Collect/Markers.md#PNOP)  
  
---|---  
  
## PinOffset Property

* * *

#### Description

|  Sets and returns the PinOffset value used to calculate various PNOP
parameters. Also set [BackOff Property](BackOff_Property.md). A sweep must be
executed (single or continuous) and [SearchPowerNormalOperatingPoint
Method](../Methods/SearchPowerNormalOperatingPoint_Method.htm) must be sent
before reading marker results. To turn off the PNOP markers, either turn them
off individually or
[DeleteAllMarkers](../Methods/DeleteAllMarkers_Method.md). To search a [User
Range](User_Range_Property.htm) with the PNOP search, first activate marker 1.
The user range used with the PNOP search only applies to marker 1 searching
for the linear gain value. The other markers may fall outside the user range.  
---|---  
  
####  VB Syntax

|  pnop.PinOffset = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pnop |  A [PNOP](../Objects/PNOP_Object.md) (object)  
value |  (double) \- PinOffset value in dB. Choose any number between:-500 and 500  
  
#### Return Type

|  Double  
  
#### Default

|  0 dB  
  
#### Examples

|  pinOffs = pnop.PinOffset 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_PinOffset(double newVal); HRESULT get_PinOffset(double*
pNewVal)  
  
#### Interface

|  IPNOP  
  
* * *

