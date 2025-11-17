##### Read-Only

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## Items Property

* * *

#### Description

|  Returns a list of configured external devices in the collection.  
---|---  
  
####  VB Syntax

|  array = extDevices.Items  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (array) Variable to store the returned values. Each item in the array is in the format (name:driver), where:

  * name = name of the external device
  * driver = [See a list of supported drivers.](../../../System/Configure_an_External_Device.md#Supported)

  
extDevices |  An [ExternalDevices](../Objects/ExternalDevices_Collection.md) (collection)  
  
#### Return Type

|  Variant Array  
  
#### Default

|  Not Applicable  
  
#### Examples

|  array = extDevices.Items'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_Items( VARIANT* array);  
  
#### Interface

|  IExternalDevices  
  
* * *

