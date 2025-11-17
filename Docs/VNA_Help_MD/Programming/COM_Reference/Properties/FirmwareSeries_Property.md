##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## FirmwareSeries Property

* * *

#### Description

|  Returns the alpha portion of the firmware revision number. For example,
given a firmware revision number A.03.30, this command returns A.  
---|---  
  
####  VB Syntax

|  value = cap.FirmwareSeries  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) - Variable to store the returned alpha value of the firmware revision number.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.FirmwareSeries 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_FirmwareSeries(BSTR * series);  
  
#### Interface

|  ICapabilities

