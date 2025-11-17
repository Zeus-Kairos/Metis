##### Read-Only

|

##### [About External
Devices](../../../System/Configure_an_External_Device.htm)  
  
---|---  
  
## HasItem Property

* * *

#### Description

|  Returns a value indicating whether the specified external devices is
configured.  
---|---  
  
####  VB Syntax

|  value = extDevices.HasItem(name)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Boolean) Variable to store one of the following returned values. False - Item (name) is NOT present in the External Devices collection. True - Item (name) IS present in the External Devices collection.  
extDevices |  An [ExternalDevices](../Objects/ExternalDevices_Collection.md) (collection)  
name |  (String) Name of External Device for which to search the collection.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  has = extDevices.HasItem('mysource')'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_HasItem( VARIANT Index, BOOL *pVal);  
  
#### Interface

|  IExternalDevices  
  
* * *

