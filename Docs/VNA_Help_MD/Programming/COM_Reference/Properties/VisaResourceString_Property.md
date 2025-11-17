##### Read-only

|

##### [About IO
Configuration](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm)  
  
---|---  
  
## VisaResourceString Property

* * *

#### Description

|  Returns the valid resource string for the specified interface type. Use
[InterfaceTypes Property](InterfaceTypes_Property.md) to read the valid
interface types for the VNA.  
---|---  
  
####  VB Syntax

|  value = IOConfig.VisaResourceString (InterfaceType)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (String) variable to store the returned information.  
IOConfig |  An [IOConfiguration](../Objects/IOConfiguration_Object.md) object.  
InterfaceType |  (String) Name of Interface Type  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = IOConfig.VisaResourceString "HISLIP" 'returns:
TCPIP0::<compID>::hislip0::INST  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get VisaResourceString(BSTR interfaceType, long visaResourceID,
BSTR* resourceString);  
  
#### Interface

|  IIOConfiguration  
  
* * *

