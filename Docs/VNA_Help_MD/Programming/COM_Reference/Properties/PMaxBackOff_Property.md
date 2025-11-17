##### Write-Read

|

##### [About PSAT Marker Search](../../../S4_Collect/Markers.md#PSat)  
  
---|---  
  
## PMaxBackOff Property

* * *

#### Description

|  Sets and returns the backoff value used to calculate various PSAT
parameters. A sweep must be executed (single or continuous) and
[SearchPowerSaturation Method](../Methods/SearchPowerSaturation_Method.md)
must be sent before reading marker results. To turn off the PSAT markers,
either turn them off individually or
[DeleteAllMarkers](../Methods/DeleteAllMarkers_Method.md). To search a [User
Range](User_Range_Property.htm) with the PSAT search, first activate marker 1.
The user range used with the PNOP search only applies to marker 1 searching
for the linear gain value. The other markers may fall outside the user range.  
---|---  
  
####  VB Syntax

|  pSat.PMaxBackOff = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pSat |  A [PSaturation](../Objects/PSaturation_Object.md) (object)  
value |  (double) \- Backoff value in dB. Choose any number between:-500 and 500  
  
#### Return Type

|  Double  
  
#### Default

|  0 dB  
  
#### Examples

|  backoff = pSat.PMaxBackOff 'Read [See example
program](../../COM_Example_Programs/Setup_PNOP_and_PSAT_Marker_Search.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_PMaxBackOff(double newVal); HRESULT get_PMaxBackOff(double*
pNewVal)  
  
#### Interface

|  IPSaturation  
  
* * *

